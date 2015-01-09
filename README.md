Money Money
===
`우리들의 세뱃돈, 무엇을 살 수 있을까?`

디버깅 1. ValueError: invalid literal for int() with base 10:
---
`돈계산할 때에 ',' 기호를 깜빡했다.`

디버깅 2. parsing -> Nonetype error
---
`requests로 받은 네이버 쇼핑 검색 결과 URL 중 일부는 2차 파싱 후 
BeatifulSoup의 인스턴스가 가지는 find method가 없었다. ( 오류 발생 )
이유를 몰라서 직접 테스트를 해보니 특정 URL은 파싱할 때 쓰는 특정 class를 가지고 있지 않아
Nonetype이 리턴되는 거였다.
`

```python
In [26]: req = requests.request('GET', "http://shopping.naver.com/search/all_search.nhn?query=저금통")

In [27]: bs.find("li", attrs={"class":"_model_list"})

In [28]: req = requests.request('GET', "http://shopping.naver.com/search/all_search.nhn?query=저금통")

In [29]: bs = BeautifulSoup(req.text)

In [30]: bs.find("li", attrs={"class":"_model_list"})

In [31]: req = requests.request('GET', "http://shopping.naver.com/search/all_search.nhn?query=저금통")

In [32]: bs = BeautifulSoup(req.text)

In [33]: type(bs.find("li", attrs={"class":"_model_list"}))
Out[33]: NoneType

In [34]: req = requests.request('GET', "http://shopping.naver.com/search/all_search.nhn?query=강아지분양")

In [35]: bs = BeautifulSoup(req.text)

In [36]: type(bs.find("li", attrs={"class":"_model_list"}))
Out[36]: NoneType

In [37]: req = requests.request('GET', "http://shopping.naver.com/search/all_search.nhn?query=아이폰6")

In [38]: bs = BeautifulSoup(req.text)

In [39]: type(bs.find("li", attrs={"class":"_model_list"}))
Out[39]: bs4.element.Tag
```
