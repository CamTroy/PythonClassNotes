import requests
from bs4 import BeautifulSoup

url = "https://www.ebay.com/itm/387585671842?_skw=wooper+poster"

headers = {
    'Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0'
}

resp = requests.get(url)
# print(resp.content)
soup = BeautifulSoup(resp.content, "html5lib")


# Shit by tag
def print_all_elements_by_tag(tag_name):

    elements = soup.find_all(tag_name)
    print("found", len(elements), " ", tag_name)
    for element in elements:
        print(element)


# Specific shit
def find_elements_by_class(element_name, class_name):

    elements = soup.find_all(element_name, class_=class_name)
    print("Found", len(elements), "with the class ", class_name)
    for element in elements:
        print(element)

def price_find():

    text = "$"
    index = text.find('$')
    length = len(text)
    # print(text())

find_elements_by_class("div", "x-price-primary")