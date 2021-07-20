#import urllib2
#print (urllib2.urlopen( "http://www.exaple.com").read())

#요청을 바로 출력하는 클라이언트 요청 코드를 작성했다.


from urllib.request import urlopen
html  = urlopen("http://www.example.com")
print (html.read())
