from urllib.parse import urlparse
result = urlparse("http://www.python.org:80/guido/python.html;philosophy?overall=3#n10")



#GET방식

from urllib.request import urlopen

html = urlopen("http://www.example.com")
print(html.read(500)) #read()는 얼마만큼의 문자를 표시할지 결정한다.


#POST방식
html = urlopen("http://www.example.com","query=python")
print(html.read(500))


#request 클래스를 활용한 post방식

import urllib.parse
import urllib.request
import json


request = urllib.request.Request("http://www.example.com") #요청 호스트명
request.header="Content-Type text/plain" #요청 헤더

data = {'query':'python'} #post로 전송하기위한 쿼리
data=json.dumps(data)
data=str(data)
data=data.encode('ascii')  #data는 바이트여야함!!!
request.data = data


html = urllib.request.urlopen(request)

print(html.read(500))


