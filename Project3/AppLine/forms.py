from django import forms
from AppLine.models import Item
from AppLine.models import Warehouse
from django.db.models.functions import Lower

class OrderManagementForm(forms.Form):
	CHOICES = (
        ('LINE_ORDER', 'Line Order'),
        ('DELIVERY', 'Delivery')
        )
	item = forms.ModelChoiceField(queryset=Item.objects.values('i_id', 'i_name').order_by(Lower('i_name')))
	warehouse = forms.ModelChoiceField(queryset=Warehouse.objects.values('w_id','w_name').order_by(Lower('w_name')))
	action = forms.ChoiceField(choices=CHOICES)
	quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'size':'1000000'}))

	