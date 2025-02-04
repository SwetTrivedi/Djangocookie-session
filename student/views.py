from django.shortcuts import render,HttpResponse

# Create your views here.

def setsessions(request):
    request.session['name']='Swet'
    # request.session['lname']='Trivedi'
    # request.session.set_expiry(600)
    # request.session.set_expiry(0)
    # request.session.set_expiry(0)
    # request.session.set_expiry(5)
    return render(request,"setsession.html")


def getsessions(request):
    if 'name' in request.session:
        name=request.session['name']
        request.session.modified=True
    # name=request.session.get('name')
    # lname=request.session.get('lname')
    # keys=request.session.keys()
    # items=request.session.items()
    # age=request.session.setdefault("age",'20')

        return render(request,"getsession.html",{"name":name})#,#'lname':lname,'keys':keys,'items':items,'age':age})
    else:
        return HttpResponse("Your Session Out ......")


def delsessions(request):
    # if 'name' in request.session:
    #     del request.session['name']
        request.session.flush()
        request.session.clear_expired()
        return render(request,'delsession.html')
