from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    #checkt of de usercreation al is ingevuld, als dat zo is ga je naar de homepage, zo niet returnt pagina terug
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #f'x' is een Fstring
            messages.success(request, f'Je account is aangemaakt, {username}! Je kan nu inloggen.')
            return redirect('login')
    else:
        form =  UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')