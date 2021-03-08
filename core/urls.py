from django.urls import path
from .views import item_list, home
app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
]
