# !/usr/bin/python
# coding: utf-8
import requests
from bs4 import BeautifulSoup
import json

def get_item_info(query):
    #request
    URL = "http://shopping.naver.com/search/all_search.nhn?query="+query
    r = requests.get(URL)
    
    #parsing
    soup = BeautifulSoup(r.text)
    item = soup.find("li", attrs={"class":"_model_list"})
    item_data = []
    
    name_tag = item.find("a", attrs={"class":"tit"})
    name = name_tag.text
    item_url = name_tag['href']
    
    image_url_tag = item.find("img", attrs={"class":"_productLazyImg"})
    image_url = image_url_tag['src']

    price_tag = item.find("span", attrs={"class":"num _price_reload"})
    price = price_tag.text

    item_data.append(
            {
                "name" : name,
                "image_url" : image_url,
                "price" : price,
                "item_url" : item_url,
            }
        )
    
    #save json to file
    #with open('items.json', 'w') as outfile:
    #    json.dump(item_data, outfile)

    return item_data[0]
