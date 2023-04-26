from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'html/home.html')

def login(request):


    email = str(request.POST['email'])
    password = str(request.POST['pw'])

    print(email,password)
    if email=='wakeflo@gmail.com' and password=='test@123':
        return render(request, 'html/base.html')
    else:
        return render(request, 'html/test.html')
