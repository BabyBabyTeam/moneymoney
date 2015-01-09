# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup
import json
import random
import requests
import re

def get_item_info():
    
    items = ["강아지분양", "닌텐도 3ds", "또봇 4단합체 쿼트란",
            "뽀로로 프리미엄 다기능 붕붕카", "저금통", "아이폰6",
            "아이스쿨 똑똑한 꼬마버스 타요",  "곰인형",
            "파워레인저 다이노포스장난감", "파포 달리는 그린 티렉스",
            "레고 디럭스 기차 세트", "레고 스타워즈 임페리얼 스타 디스트로이어",
            "짜장면", "에르메스백", "샤넬백"]
    
#Item extraction
    random.randrange(1, len(items))
    query = items[random.randrange(1, len(items))]

    #request
    URL = "http://shopping.naver.com/search/all_search.nhn?query="+query
    r = requests.get(URL)
    
    #parsing
    soup = BeautifulSoup(r.text)
    item = soup.find("li", attrs={"class":"_model_list"})
    item_data = []
    
    name_tag = item.find("a", attrs={"class":"tit"})
    name = name_tag.text
    name = re.sub('[\t\r\n  ]', '', name)

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

def home(request):

    money_value = ""
    
    if 'money_value' in request.GET:
        money_value = request.GET['money_value']

#get item
        item_info = get_item_info()
        """        
        if int(money_value) >= int(item_info['price']):
            num_of_product = str(int(momey_value) / int(item_info['price']))
            string = "그 돈으로 이거 " + num_of_product + "개 살 수 이써"
        else:
            string = str(int(item_info['price']) - int(money_value)) + "원 더모아 친구"
        """ 

        return render(request, "home.html", {'item_name' : item_info['name'],
                'item_price' : item_info['price'], 
                'item_url' : item_info['item_url'],
                'image_url' : item_info['image_url']})


    return render(request, "home.html")





