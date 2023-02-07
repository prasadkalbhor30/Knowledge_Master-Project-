from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
def checksess(req):
    try:
        email=req.session['email']
        return 1
    except:
        return 0

def courses(request):
    res = render(request, 'courses/courses.html',{'user':checksess(request)})
    return res




    