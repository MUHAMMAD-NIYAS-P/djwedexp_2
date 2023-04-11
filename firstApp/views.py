from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def user_view(request):
    users = User.objects.all()
    return render(request, 'firstApp/user_view.html', { 'users':users })
