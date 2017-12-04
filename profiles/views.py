from django.shortcuts import (
    render, 
    redirect
)
from django.contrib.auth.forms import (
    UserCreationForm, 
    UserChangeForm, 
    PasswordChangeForm, 
    PasswordResetForm
)


from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .forms import (
    RegistrationForm, 
    EditForm
)
# Create your views here.

def register(request):
    #post form
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/profile')
    
    #get form
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request,'registration.html', args)
        
# Create your views here.
@login_required
def home(request):
    
    nummer = [1,42,1337]
    name = 'Dokne Abreke'

    args ={'name': name, 'nums':nummer}
    return render(request,'home.html', args)

@login_required
def view_profile(request):
    args ={'user':request.user}
    return render(request, 'profile.html',args)
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form= EditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')

    else:
        form = EditForm(instance=request.user)
        args = {'form':form }
        return render(request, 'edit_profile.html', args)

@login_required
def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')

        else:
            return redirect('/profile/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request,"change-password.html" ,args)

def reset_password(request):
    if request.method=='POST':
        form = PasswordResetForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')

    else:
        form = PasswordResetForm(request.POST, user=request.user)
        args = {'form': form}
        return render(request,"change-password.html" ,args)
