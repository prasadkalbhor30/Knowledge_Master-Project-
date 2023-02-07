from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from Online_Test.models import user
from Online_Test.models import sub_Category , Category,main_test_Categories

def checksess(req):
    try:
        email=req.session['email']
        return 1
    except:
        return 0

def home(request):
    all_cat=list(main_test_Categories.objects.all().order_by("Heading"))


    data={
        "categories":all_cat,
        'user':checksess(request)
    }
    res=render(request, 'Home/index.html',data)
    return HttpResponse(res)

def about(request):
    res = render(request, 'Home/about.html',{'user':checksess(request)})
    return res
    
def contact(request):
    res = render(request, 'Home/contact.html',{'user':checksess(request)})
    return res

def signUp(request):
    try:
        error=request.GET['error']
        print("error=",error)
    except:
        error=None
    res= render(request, 'Home/signup.html',{'error':error})
    return res

def save_User(request):
    email=request.POST['email']
    name=request.POST['name']
    pwd=request.POST['pass']
    all_usr=list(user.objects.all())
    for u in all_usr:
        if email==u.email:
            return HttpResponseRedirect('http://localhost:8000/sign-up/?error=0')
    u=user()
    x=checkPass(pwd)
    print("this is result : ",x)
    if x:
        u.email=email
        u.name=name
        u.pwd=pwd
        u.save()
    else:
        return HttpResponseRedirect('http://localhost:8000/sign-up/?error=1')
    return HttpResponseRedirect('http://localhost:8000/sign-in/')
    
def signIn(request):
    try:
        error=request.GET['error']
    except:
        error=None
    res = render(request, 'Home/signin.html',{'error':error})
    return res

def logOut(request):
    request.session.clear()
    print("this is that :",request.session)
    return HttpResponseRedirect('http://localhost:8000/')

def validateUser(request):
    try:
        usr=user.objects.get(email=request.POST['email'],pwd=request.POST['pass'])
        request.session['email']=usr.email
        request.session['name']=usr.email
        request.session['pwd']=usr.pwd
        return HttpResponseRedirect('http://localhost:8000/',{"user":usr})
    except:
        return HttpResponseRedirect('http://localhost:8000/sign-in/?error=1')






        
# def save_User(request):
#     email=request.POST['email']
#     pwd=request.POST['pass']
#     all_user=list(user.objects.all())
#    

def checkPass(pwd):
    if len(pwd)<7:
        return False

    for i in pwd:
        if i.isalpha():
            break
    else:
        return False

    for i in pwd:
        if i.isnumeric():
            break
    else:
        return False

    sp_char="[@_!$%^&*()<>?/\|}{~:]#"
    for i in sp_char:
        if i in pwd:
            break
    else:
        return False
    return True

