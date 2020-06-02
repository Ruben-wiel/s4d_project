from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserProfileForm


def register(request):
    # checkt of de usercreation al is ingevuld.
    # Als dat zo is ga je naar de homepage,
    # zo niet returnt pagina terug.
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            # f'x' is een Fstring
            messages.success(
                request, f'Je account is aangemaakt, {username}! Je kan nu inloggen.')
            return redirect('login')
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'users/register.html', context)
# Forms u_form en p_form zijn toegevoegd aan de profile view.


@login_required
def profile(request):
    # Post request met de data van de form, door de instance=request.user.
    # Zorgt er voor dat er daadwerkelijk ook iets wordt aangepast in de database.
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,  # is voor de image data
                                   instance=request.user.profile)
        # Als beide forms valid zijn wordt de database pas opgeslagen.
        if u_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Je profiel is bijgewerkt!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
