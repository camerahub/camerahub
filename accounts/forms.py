from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean(self, *args, **kwargs):
        # Normal cleanup
        cleaned_data = super(UserCreationForm, self).clean(*args, **kwargs)
        return cleaned_data
        
    def save(self, commit=True):
        # Saves the email, first_name and last_name properties, after the normal save behavior is complete.
        user = super(UserCreationForm, self).save(commit)
        if user:
            user.email = self.cleaned_data['email']
            user.set_password(self.cleaned_data['password1'])
            if commit:
                user.save()
        return user