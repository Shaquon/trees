from django import forms
from dropbox.models import File
from django.contrib.auth.models import User

class NewUserForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)


class AddFileForm(forms.ModelForm):
    model = File
    fields = ['name', 'parent', 'folder']
    def __init__(self, user, * args, **kwargs):
        super(AddFileForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = File.objects.filter(
            folder=True, user=user
        )