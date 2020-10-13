from django import forms
from .models import Hobby
from .models import portfolio
from .models import contact



class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['Hobby_name', 'Hobby_desc', 'Hobby_image']



class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['contact_name', 'contact_email', 'contact_message']