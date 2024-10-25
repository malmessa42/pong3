from django.urls import path

from . import views

urlpatterns = [
	# path('see/', views.home, name='home1'),
	# path('', views.test, name='home2'),

	path('', views.home, name='home'),
]