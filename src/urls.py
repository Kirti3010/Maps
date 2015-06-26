# step 7th
from django.conf.urls import url

from src import views

urlpatterns = [
	url(r'',views.maps, name = "maps")
]