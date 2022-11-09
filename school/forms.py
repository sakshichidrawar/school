from django import forms
from school.models import firstclass,secondclass,thirdclass,fourthclass

class firstform(forms.ModelForm):
    class Meta:
        model=firstclass
        fields='__all__'
class secondform(forms.ModelForm):
    class Meta:
        model=secondclass
        fields='__all__'

class thirdform(forms.ModelForm):
    class Meta:
        model=thirdclass
        fields='__all__'

class fourthform(forms.ModelForm):
    class Meta:
        model=fourthclass
        fields='__all__'