from django import forms
from .models import participant
  
class ParticipantForm(forms.ModelForm):
  
    class Meta:
        model = participant
        fields = ['image','name', 'details','post']
        