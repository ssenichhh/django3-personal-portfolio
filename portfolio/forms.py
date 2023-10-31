from django import forms
from .models import ContactMessage

# class HomeForm(forms.Form):
#     post = forms.CharField()
#
# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = ContactMessage
#         fields = ('name', 'email', 'message')

class HomeForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'message')
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        #     'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        #
        # }
        # lables = {
        #     'name': "",
        #     'email': "",
        #     'message': "",
        # }
