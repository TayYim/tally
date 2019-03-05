from django.urls import path
from . import views

app_name = 'group_tally'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_records', views.get_records, name='get_records'),
    path('add_record', views.add_record, name='add_record'),
    path('clear_records', views.clear_records, name='clear_records'),
    path('get_expense', views.get_expense, name='get_expense'),
]
