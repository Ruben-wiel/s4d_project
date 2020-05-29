from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField()
    biography = forms.CharField()

# algemeen: This class meta gives us a nested namespace for configration and keeps the configurations at one place.
# And within the configuration we’re saying that the model that will be affected is the User-model.
    class Meta:

        # We’re going to specify the model that we want this form to interact with.
        # So the model is going to be ‘User’. Because whenever this form validates its going to create a new user.
        model = User

# These are the fields that are going to be shown on our form.
        fields = ['username', 'email', 'phone', 'password1', 'password2']

#"a model form allows us to create a form that will work with a specific database model
#in this case we want a form that will update our user model."
#hiermee kan de profile geupdate worden.

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('location', 'age')




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


#hiermee kan de profile-image geupdate worden.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']