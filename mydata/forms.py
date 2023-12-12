from django import forms

   
 

    
class MessageForm(forms.Form):
    name=forms.CharField(label="Name",max_length=100, widget=forms.TextInput(attrs={'autocomplete':'name'}))
    email=forms.CharField(label='Email Address', widget=forms.TextInput(attrs={'autocomplete':'email'}))
    subject=forms.CharField(max_length=100)
    message=forms.CharField(widget=forms.Textarea(attrs={ 'rows':7}))
   
   