from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    #checkt of de usercreation al is ingevuld, als dat zo is ga je naar de homepage, zo niet returnt pagina terug
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            #f'x' is een Fstring
            messages.success(request, f'Account created for {username}!')
            return redirect('web-home')
    else:
        form =  UserCreationForm()
    return render(request, 'users/register.html', {'form': form})