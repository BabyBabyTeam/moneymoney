# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bs4 import BeautifulSoup
import json
import random
import requests
import re

def get_item_info():
    items = ["닌텐도 3ds", "또봇 4단합체 쿼트란",
            "뽀로로 프리미엄 다기능 붕붕카", "아이폰6",
            "아이스쿨 똑똑한 꼬마버스 타요",  "곰인형",
            "파포 달리는 그린 티렉스", "레고 디럭스 기차 세트", 
            "레고 스타워즈 임페리얼 스타 디스트로이어", "짜장면", "에르메스백",
            "샤넬백"]
    
    # request
#    URL = ""
   
    # parsing ( element, class )
    for cnt in range(10):
        # item extraction
        random.randrange(1, len(items))
        query = items[random.randrange(1, len(items))]

        URL = "http://shopping.naver.com/search/all_search.nhn?query="+query
        r = requests.get(URL)
        soup = BeautifulSoup(r.text)

        try:
            item = soup.find("li", attrs={"class":"_model_list"})    
            name_tag = item.find("a", attrs={"class":"tit"})
            image_url_tag = item.find("img", attrs={"class":"_productLazyImg"})
            price_tag = item.find("span", attrs={"class":"num _price_reload"})
        except AttributeError:
            print query
            if cnt is 9:
                return -1
            else:
                continue
        break
    
    # parsing  ( attribute )
    name = name_tag.text
    item_url = name_tag['href']
    name = re.sub('[\t\r\n  ]', '', name)
    image_url = image_url_tag['src']
    price = price_tag.text
    
    # parsing ( re, )
    name = re.sub('[\t\r\n  ]', '', name)

    # save the parsed data into the dict variable
    item_data = {"name" : name, "image_url" : image_url, "price" : price,
                    "item_url" : item_url,}

    return item_data

def home(request):
    money_value = ''
    res_message = ''
    
    if 'money_value' in request.GET:
        money_value = int(re.sub('[^(\d+)]', '', request.GET['money_value']))

        # get item
        item_info = get_item_info()
        if item_info is -1:
            return HttpResponse("Please check broken crawling pages")
        price = int(re.sub('[^(\d+)]', '', item_info['price']))
        
        if money_value >= price:
            num_of_product = str(money_value / price)
            res_message = "그 돈으로 이거 " + num_of_product + \
                                    "개 살 수 이써"
        else:
            required_money = str(price - money_value)
            res_message = required_money + "원 더모아 친구"

        return render(request, "home.html", {'item_name' : item_info['name'],
                'item_price' : item_info['price'], 
                'item_url' : item_info['item_url'],
                'image_url' : item_info['image_url'],
                'res_message' : res_message},)

    return render(request, "home.html")





