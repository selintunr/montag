from django import forms
from webPage1.models import contactFormModel, subFormModel


class contactForm(forms.ModelForm):
    username = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "İsminiz*"}))
    phone = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Telefonunuz*"}))
    email = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "E-Posta Adresiniz*"}))
    subject = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Konu*"}))
    message = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Mesajınız*"}))

    class Meta:
        model = contactFormModel
        fields = ('username', 'phone', 'email', 'subject', 'message')



class subForm(forms.ModelForm):
    email = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "E-Posta Adresiniz*"}))

    class Meta:
        model = subFormModel
        fields = ('email', )



################################################################

class contactForm2(forms.ModelForm):
    username = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Name*"}))
    phone = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Phone number *"}))
    email = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Mail Adress*"}))
    subject = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Subject*"}))
    message = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Message*"}))

    class Meta:
        model = contactFormModel
        fields = ('username', 'phone', 'email', 'subject', 'message')



class subForm2(forms.ModelForm):
    email = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Mail Adress*"}))

    class Meta:
        model = subFormModel
        fields = ('email', )