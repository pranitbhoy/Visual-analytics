from django.shortcuts import render
import random
import re

from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'home/base.html')

def login(request):
    return render(request,'home/login.html')

def select(request):
    val = request.GET["div"]

    if val == "5":
        global captcha
        captcha = ""
        count = 0
        while count < 6:
            list = ["@", "#", ]
            for i in range(48, 57, 1):
                list.append(chr(i))
            for j in range(65, 90, 1):
                list.append(chr(j))
            for i in range(48, 57, 1):
                list.append(chr(i))
            for k in range(97, 122, 1):
                list.append(chr(k))
            count = count + 1
            value = random.choice(list)
            captcha = captcha + value

        list = {"cap": captcha}
        return render(request, 'home/fasttag.html', context=list)
    elif val == "0" or val == "1" or val == "2" or val == "3" or val == "4":
        return render(request, 'home/fpage.html')


def log(request):
    global username
    username = request.POST['user']
    password = request.POST['pass']
    ecap = request.POST['ch']
    pattern = ("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$")

    result = re.findall(pattern, password)

    if len(username) < 10 and len(username) < 12 :
        list = {"cap": captcha,"msg":"check user id"}
        return render(request, 'home/popup.html', context=list)
    if not (result):
        list = {"cap": captcha, "msg": "use strong pass"}
        return render(request, 'home/popup.html', context=list)
    elif ecap!= str(captcha):
        list = {"cap": captcha, "msg": "incorrect CAPTCHA"}
        return render(request, 'home/popup.html', context=list)


    elif ecap == str(captcha):
        print( username, password)
        ins = User(username=username, password=password)
        ins.save()

        list = {"cap": captcha, "user": username}
        return render(request, 'home/user.html', context=list)


def refresh(request):
    global captcha
    captcha = ""
    count = 0
    while count < 6:
        list = ["@", "#", ]
        for i in range(48, 57, 1):
            list.append(chr(i))
        for j in range(65, 90, 1):
            list.append(chr(j))
        for i in range(48, 57, 1):
            list.append(chr(i))
        for k in range(97, 122, 1):
            list.append(chr(k))
        count = count + 1
        value = random.choice(list)
        captcha = captcha + value

    list = {"cap": captcha}
    return render(request, 'home/fasttag.html', context=list)

def recharge(request):
    global captcha
    captcha = ""
    count = 0
    while count < 6:
        list = ["@", "#", ]
        for i in range(48, 57, 1):
            list.append(chr(i))
        for j in range(65, 90, 1):
            list.append(chr(j))
        for i in range(48, 57, 1):
            list.append(chr(i))
        for k in range(97, 122, 1):
            list.append(chr(k))
        count = count + 1
        value = random.choice(list)
        captcha = captcha + value

    list = {"cap": captcha}
    return render(request, 'home/recharge.html', context=list)


def user(request):
    user = {"user": username}
    return render(request,'home/user.html', context=user)

def user1(request):
    user={"user":username}
    return render(request,'home/user2.html',context=user)

def name(request):
    return render(request, 'home/user.html')


def name1(request):
    return render(request, 'home/user2.html')

def recharge1(request):
    global captcha
    captcha = ""
    count = 0
    while count < 6:
        list = ["@", "#", ]
        for i in range(48, 57, 1):
            list.append(chr(i))
        for j in range(65, 90, 1):
            list.append(chr(j))
        for i in range(48, 57, 1):
            list.append(chr(i))
        for k in range(97, 122, 1):
            list.append(chr(k))
        count = count + 1
        value = random.choice(list)
        captcha = captcha + value

    list = {"cap": captcha,"user":username}
    return render(request, 'home/user2.html', context=list)


def refresh1(request):
    global captcha
    captcha = ""
    count = 0
    while count < 6:
        list = ["@", "#", ]
        for i in range(48, 57, 1):
            list.append(chr(i))
        for j in range(65, 90, 1):
            list.append(chr(j))
        for i in range(48, 57, 1):
            list.append(chr(i))
        for k in range(97, 122, 1):
            list.append(chr(k))
        count = count + 1
        value = random.choice(list)
        captcha = captcha + value

    list = {"cap": captcha,"user":username}
    return render(request, 'home/user.html', context=list)





