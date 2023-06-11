from django.shortcuts import render,redirect
from django.contrib.auth import login

from .form import * 
# Create your views here.



def register (request):
    form = UserRegistrationForm()

    if request.method =='POST': 
       # créez une nouvelle instance du formulaire UserRegistrationForm
       #  en utilisant les données soumises par l'utilisateur
       #  (request.POST).

        form = UserRegistrationForm(request.POST) 
        
        if form.is_valid():
            user=form.save()
            login(request,user)

            return redirect('events_listC')
    return render(request,'registration/login.html',{'form': form})


# def login (request):
#     form=LoginForm()
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user= authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('events_listC')
#     return render(request,'registration/login.html',{'form': form})
