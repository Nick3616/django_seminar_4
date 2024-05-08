from django import forms

from .models import Commodity

class CommodityForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField()
    quantity = forms.IntegerField()
    image = forms.ImageField(required=False)
    
    class Meta:
        model = Commodity
        fields = ['name', 'description', 'price', 'quantity', 'image']

class CommodityUpdateForm(forms.ModelForm):
    class Meta:
        model = Commodity
        fields = '__all__'


