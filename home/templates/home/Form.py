from django import forms

class Form(forms.Form):
    location = forms.CharField(widget=forms.TextInput(attrs={"id": "location"}), max_length=85)

    item = forms.CharField(widget=forms.TextInput(attrs={"id": "item"}), max_length=30)

    description = forms.CharField(widget=forms.Textarea(attrs={"id": "itemDesc"}), max_length=250)
    
    contact = forms.CharField(widget=forms.TextInput(attrs={"id": "contact"}), max_length=25)