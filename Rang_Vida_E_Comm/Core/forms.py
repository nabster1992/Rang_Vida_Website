from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from django import forms: Import the base forms module from Django, which provides tools for working with HTML forms.
# from django.contrib.auth.forms import UserCreationForm: Import the UserCreationForm class, a built-in form provided by Django for user registration.
# from django.contrib.auth.models import User: Import the User model from the django.contrib.auth.models module, which represents user information.

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

#     Define a nested Meta class within SignUpForm. This class provides additional configuration for the form.
# model = User: Specify that the form is associated with the User model.
# fields: List the fields that should be included in the form. In this case, it includes the fields from UserCreationForm (username, password, and password2) as well as the custom fields (first_name, last_name, and email).
# In summary, the SignUpForm extends the built-in UserCreationForm and adds custom fields (first_name, last_name, and email). The form is associated with the User model, and it specifies the fields to include in the form. This form is suitable for user registration in a Django application.