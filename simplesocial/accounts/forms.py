from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model() # get the user model that is currently active

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name" # customize what the labels will display for these attributes
        self.fields["email"].label = "Email address"   # this is not a requirement, but this is the way to do it if you want to 
