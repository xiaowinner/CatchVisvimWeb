import re
import GeneralCaptureMethod
from pymongo import MongoClient
from BeautifulSoup import BeautifulSoup 

MONGO_CONN = MongoClient('localhost', 27017)
db = MONGO_CONN.visvim
p = db.commodity

# key = hdn006
current_page = 1

# key = REG
page_reg = None

DOWNLOAD_URL = 'https://shop.visvim.tv/jp/jp/top/'
FIRST_URL = 'https://shop.visvim.tv/jp'

def parse_html(html):

    global current_page
    global page_reg

    soup = BeautifulSoup(html)
    item_div = soup.find('div', attrs = {'class': 'selectItemBoxes clearfix'})
    form_reg = soup.find('form', attrs = {'id': 'f1'})
    reg_input =  form_reg.find('input', attrs = {'id': 'REG'})
    
    if page_reg is None:
        page_reg = reg_input['value'].encode('raw_unicode_escape')
        print(page_reg)

    # discovered commodity
    item_list = item_div.findAll('a')

    item_div = soup.find('div', attrs = {'class': 'selectItemBoxes clearfix'})

    # find page
    page_div = soup.find('div', attrs = {'id': 'pageLinks'})
    page_next_a = page_div.find('a', attrs = {'class': 'pageLinkRight'})
    
    if page_next_a is None:
        print("== page is end ==")
        current_page = None
    else:
        current_page += 1


    commodity_list = []

    for detail in item_list:
        commodity_js = detail['href']
        id_array = re.findall(r'\'\d+\'', commodity_js)
        commodity_number, commodity_id = id_array
        commodity_color = detail.find('div', attrs = {'style': 'color'})
        commodity_img = detail.find('img')['src']
        commodity_name = detail.find('span', attrs = {'class': 'itemText'}).getText()
        commodity = {
            'id': commodity_id,
            'img': commodity_img,
            'name': commodity_name,
            'color': commodity_color,
            'number': commodity_number
        }
        commodity_list.append(commodity)
    print(commodity_list)
    return commodity_list


def request_first_page(url):

    html = GeneralCaptureMethod.get_page(url)
    results = parse_html(html)
    request_next_page(DOWNLOAD_URL)

def request_next_page(url):

    while current_page:
        parameters = {
            "REG": page_reg,
            "hdn006": current_page,
        }
        html = GeneralCaptureMethod.post_page(url, parameters)
        results = parse_html(html)
        print(current_page)


def main():
    request_first_page(FIRST_URL)


if __name__ == '__main__':
    main()