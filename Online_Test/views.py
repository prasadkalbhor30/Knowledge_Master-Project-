from django.shortcuts import render
from Online_Test.models import *
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import random
# Create your views here.

# This is local functions





def checksess(req):
    try:
        email=req.session['email']
        return 1
    except:
        return 0

def check_topic(correct,ql,qd,topic):
    if topic == 'C-language':
        for c in ql:
            q=c_language.objects.get(qno=c)
            qd.append(q)
            correct.append(q.ans)
    if topic == 'C++-language':
        for c in ql:
            q=cpp_language.objects.get(qno=c)
            qd.append(q)
            correct.append(q.ans)
    if topic == 'Python':
        for c in ql:
            q=python.objects.get(qno=c)
            qd.append(q)
            correct.append(q.ans)
    if topic == 'Java':
        for c in ql:
            q=java.objects.get(qno=c)
            qd.append(q)
            correct.append(q.ans)
    if topic == 'Javasctipt':
        for c in ql:
            q=javascript.objects.get(qno=c)
            qd.append(q)
            correct.append(q.ans)
                    


def test_data(topic):
    if topic == 'C-language':
        q=list(c_language.objects.all())
    if topic == 'C++-language':
        q=list(cpp_language.objects.all())
    if topic == 'Python':
        q=list(python.objects.all())
    if topic == 'Java':
        q=list(java.objects.all())
    if topic == 'Javasctipt':
        q=list(javascript.objects.all())
    return q


# This is view functions

def onlineTest(request):
    try:
        email=request.session['email']
        print(email)
        return render(request, 'online_test/test-section.html',{'user':checksess(request)})
    except:
        return HttpResponseRedirect('http://localhost:8000/sign-in/')

def startTest(request, topic):
    res = render(request, 'online_test/start_test.html',{'tesr':topic,'user':checksess(request)})
    return res

def testPage(request, course):
    questions=test_data(course)
    random.shuffle(questions)
    que=questions[:10]
    res = render(request, 'online_test/test_page.html',{'questions':que , 'topic':course,'user':checksess(request)})
    return res

def checkTest(request, course):
    qno_list=[]
    u_ans=[]
    c_ans=[]
    q_data=[]
    total_attempts=0
    total_right=0
    total_wrong=0
    for k in request.POST:
        if k.startswith('qno'):
            qno_list.append(int(request.POST[k]))
        elif k.startswith('ans'):
            a=request.POST[k]
            u_ans.append(a)
            if a!='0':
                total_attempts+=1
    a=zip(u_ans,c_ans)
    check_topic(c_ans,qno_list, q_data, course)
    for u,c in a:
        if u==c:
            total_right+=1
    total_wrong=total_attempts-total_right
    main=zip(q_data,u_ans,c_ans)
    data={
        'questions':main,
        't_right':total_right,
        't_wrong':total_wrong,
        't_attempt':total_attempts
    }
    res=render(request, 'online_test/result.html',data)
    return res

        






def addQuestion(request):
    res = render(request, 'online_test/new_question.html')
    return res

def saveQuestion(request):
    question=programmingQ()
    question.que = request.POST['qst']
    question.optiona = request.POST['optiona']
    print(request.POST['red',"off"])
    question.optionb = request.POST['optionb']
    question.optionc = request.POST['optionc']
    question.optiond = request.POST['optiond']
    question.ans = request.POST['ans']
    question.save()
    return HttpResponseRedirect('http://localhost:8000/online-test/view-questions/')

def viewQuestion(request):
    questions=programmingQ.objects.all()
    res = render(request, 'online_test/view_questions.html',{'questions':questions})
    return res

def editQuestion(request):
    qNo=request.GET['qno']
    question=programmingQ.objects.get(qno=int(qNo))
    return render(request, 'online_test/edit_question.html',{'question':question})

def saveeditedQuestion(request):
    question = programmingQ()
    question.qno = request.POST['qno']
    question.que = request.POST['qst']
    question.optiona = request.POST['optiona']
    question.optionb = request.POST['optionb']
    question.optionc = request.POST['optionc']
    question.optiond = request.POST['optiond']
    question.ans = request.POST['ans']
    question.save()
    return HttpResponseRedirect('http://localhost:8000/online-test/view-questions/')

def deleteQuestion(request):
    qNo=request.GET['qno']
    question=programmingQ.objects.get(qno=int(qNo))
    question.delete()
    return HttpResponseRedirect('http://localhost:8000/online-test/view-questions/')


    
