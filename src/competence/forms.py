from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    nom = forms.CharField(label='Nom', widget=forms.TextInput(attrs={'class': 'form-control border-0 py-3', 'placeholder': 'Votre Nom'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control border-0 py-3', 'placeholder': 'Votre Email'}))
    telephone = forms.CharField(label='Téléphone', widget=forms.TextInput(attrs={'class': 'form-control border-0 py-3', 'placeholder': 'Votre Numéro de Téléphone'}))
    project = forms.CharField(label='Projet', widget=forms.TextInput(attrs={'class': 'form-control border2 py-3', 'placeholder': 'Votre Projet'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'w-100 form-control border-0 py-3', 'placeholder': 'Votre Message'}))

    class Meta:
        model = ContactMessage
        fields = ['nom', 'email', 'telephone', 'project', 'message']