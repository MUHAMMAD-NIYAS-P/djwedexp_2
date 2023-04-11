from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.


def register_user(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Registration successfull!"))
            return redirect('user-view')

    else:
        form = UserRegistrationForm()
        return render(request, 'users/register_user.html', { 'form':form })
