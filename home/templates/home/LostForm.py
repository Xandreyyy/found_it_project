from django import forms

class LostForm(forms.Form):
    local = forms.CharField(max_length=85)
    item = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    contact = forms.CharField(max_length=30)