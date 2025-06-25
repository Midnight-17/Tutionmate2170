# forms.py
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import teacher, subjects
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CreateTeacherForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
    image = forms.ImageField(required=True)
    min_rate = forms.IntegerField(required=True, min_value=0, max_value=5000)
    max_rate = forms.IntegerField(required=True, min_value=0, max_value=10000)
    phone_number = forms.CharField(
    widget=forms.TextInput(attrs={'placeholder': 'Enter 8-digit phone number'}),
    label="Phone Number",
    max_length=8,
    min_length=8
)

    
    subjects = forms.ModelMultipleChoiceField(
        queryset=subjects.objects.all(),
         widget=forms.SelectMultiple(attrs={'size': 5}),
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'image', 'min_rate', 'max_rate', 'subjects']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already registered.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")
        
        min_rate = cleaned_data.get("min_rate")
        max_rate = cleaned_data.get("max_rate")
        if min_rate is not None and max_rate is not None:
            if max_rate <= min_rate:
                raise ValidationError("Max rate must be greater than min rate.")


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]