from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, UserProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

# General: This class meta gives us a nested namespace for configration and keeps the configurations at one place.
# And within the configuration we’re saying that the model that will be affected is the User-model.
# Hiermee kan de profile geupdate worden.
    class Meta:
        # We’re going to specify the model that we want this form to interact with.
        # So the model is going to be ‘User’. Because whenever this form validates its going to create a new user.
        model = User
        # These are the fields that are going to be shown on our form.
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('locatie', 'telefoon')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# Hiermee kan de profile-image geupdate worden.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
