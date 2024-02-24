from django import forms

class Form(forms.Form):
    location = forms.CharField(widget=forms.TextInput(attrs={"id": "location", "class": "field"}), max_length=85)

    item = forms.CharField(widget=forms.TextInput(attrs={"id": "item", "class": "field"}), max_length=30)

    description = forms.CharField(widget=forms.Textarea(attrs={"id": "itemDesc", "class": "field"}), max_length=250)