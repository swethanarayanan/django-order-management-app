from django.urls import path,re_path
from . import views # Import the views
urlpatterns = [
	re_path(r'^$', views.AppRaw),
	path('result/',views.getrows_db)
	]