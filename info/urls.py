from django.urls import path
from .views import index, blood_entry

app_name = 'info'

urlpatterns = [
    path('', index, name='home'),
    path('blood-entry/', blood_entry, name='blood-entry'),

]