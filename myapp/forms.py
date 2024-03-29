from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": ""})
    )
    subject = forms.CharField(widget=forms.TextInput(attrs={}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message"})
    )  