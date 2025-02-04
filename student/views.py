from django.shortcuts import render
from datetime import datetime,timedelta
# Create your views here.
def setcookie(request):
   response=render(request,'setcookie.html')
   # response.set_cookie('name','Swet' ,max_age=20)
   response.set_cookie('name','Swet' ,expires=datetime.utcnow()+timedelta(days=2))
   return response




def getcookie(request):
#    name=request.COOKIES['name']kk
   name=request.COOKIES.get('name')
   return render (request,'getcookie.html',{'nm':name})


def delcookie(request):
   response=render(request,'delcookie.html')
   response.delete_cookie('name')
   return response

