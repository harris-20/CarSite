from django import forms
from carapp.models import OrderVehicle
#from carapp.models import ContactUs
class OrderVehicleForm(forms.ModelForm):
    class Meta:
        model = OrderVehicle
        fields = ['vehicle', 'buyer', 'quantity']
        widgets = {'buyer': forms.Select}
        labels = {'quantity': 'Vehicle Ordered Label'}  # Written this way to check it on the page

class ContactForm(forms.Form):
    ID=forms.IntegerField()
    name = forms.CharField(max_length=30)
    email=forms.EmailField()
    subject=forms.CharField(max_length=30)
    reason= forms.CharField(widget=forms.Textarea)
    message=forms.CharField(widget=forms.Textarea)