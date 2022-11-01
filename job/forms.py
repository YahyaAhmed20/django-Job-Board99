

from django import forms
from .models import Apply,Job





class ApplyForm(forms.ModelForm):
    class Meta: 
        model=Apply
        fields=['name','email','website','cv','cover_letter']
        
class Jobform(forms.ModelForm):
    class Meta:
        model=Job
        fields='__all__'
        exclude=('owner','slug')
    