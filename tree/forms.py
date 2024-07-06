# tree/forms.py

from django import forms
from .models import FamilyMember

class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = ['name', 'birth_date', 'child_number', 'parent', 'spouse', 'sex']
