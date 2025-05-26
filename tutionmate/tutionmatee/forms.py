# forms.py
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import teacher, subjects

class CreateTeacherForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = teacher
        fields = ['name', 'subjects', 'min_rate', 'max_rate', 'image', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password and Confirm Password do not match.")
