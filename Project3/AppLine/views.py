# Create your views here.
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.db import connection # connection module for Database operations
from AppLine.models import Item
from AppLine.models import Stock
from AppLine.models import Warehouse
from AppLine.forms import OrderManagementForm
from django.db import IntegrityError
from ast import literal_eval

def AppLine(request):
	if request.method == 'GET':  
		form = OrderManagementForm()
		return render(request, 'AppLine/home.html', {'form': form})
	
def fulfillLineOrderAndDelivery(request):
	item = literal_eval(request.POST.get('item', ''))
	warehouse = literal_eval(request.POST.get('warehouse', ''))
	quantity = request.POST.get('quantity', '')
	action = request.POST.get('action', '')
    
	try:
		stock = Stock.objects.get(w_id=warehouse['w_id'], i_id = item['i_id'])
		current_qty = int(stock.s_qty)
		quantity = int(quantity)
		
		if action == 'LINE_ORDER':
			new_qty = current_qty - quantity	
		elif action == 'DELIVERY':
			new_qty = current_qty + quantity
			
		Stock.objects.update(s_qty = new_qty)
		response = "Your {} has been accepted".format(action)
	except Stock.DoesNotExist:
		response = 'No stock found'
	except IntegrityError:
		response = 'Insufficient stock'
	
	response_meta = dict()
	response_meta['Item Name'] = item['i_name']
	response_meta['Warehouse Name'] = warehouse['w_name']
	response_meta['Action'] = action
	response_meta['Stock Before'] = current_qty
	response_meta['Stock After'] = new_qty
	return render(request,'AppLine/results.html', {'response': response, 'dict': response_meta})