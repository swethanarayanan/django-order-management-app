# Create your views here.
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.db import connection # connection module for Database operations
from AppORM.models import Item
from AppORM.models import Stock
from AppORM.models import Warehouse

def AppORM(request):
	# Renders 'AppORM/forms.html' template with empty dictionary
	return render(request,'AppORM/forms.html',{})
	
def getrows_db(request):
	if request.method == 'GET':                                      
		# values sent via GET by the user
		form = request.GET.get('regex_id','')		
		
		#Retrieving results using Query Set
		results = Item.objects.filter(i_name__regex=form).values_list()
		
		context = {'records': results}
		return render(request,'AppORM/results.html',context)