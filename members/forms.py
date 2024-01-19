from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    is_chef = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "is_chef")

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["is_chef"].widget.attrs.update({"class": "form-check-input"})

    def clean(self):
        cleaned_data = super().clean()
        if not self.is_valid():
            print(self.errors)
        return cleaned_data


class ChefRegistrationForm(forms.Form):
    agree = forms.BooleanField(required=True)