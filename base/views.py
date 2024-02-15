from django.shortcuts import render
from django.http import  HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect
from .models import Images

# Create your views here.
@login_required(login_url='/login')
def home(request):
    images = request.user.images.all()

    context = {
        'images':images
    }
    return render(request,'base/home.html',context)


def login_view(request):
    if request.method =='POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        
    return render(request,'base/login.html')

@login_required(login_url='/login')
def upload(request):
    if request.method=='POST':
        image = request.FILES.get('file')
        created_image = Images.objects.create(user=request.user,image=image)

        if created_image:
            return redirect('home')
        
    return render(request,'base/upload.html')

def logoutUser(request):
    logout(request)
    return redirect('login')