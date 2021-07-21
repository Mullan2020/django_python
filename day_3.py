import django
django.get_version()

    #모델 예시
from django.db import models

#흔히 sql 테이블 만들듯이 한다.
class Person(model.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    #뷰
from django.http import HttpResponse
import datetime

#함수를 작성한다
def current_datetime(request):
	now = datetime.datetime.now()
    html = "<html><bodt> 현재시각은 %s입니다. </body><html>" %now
    return HttpResponse(html)
    #에러객체
    #return HttpResponseNotFound('<h1>Page not found</h1>')
