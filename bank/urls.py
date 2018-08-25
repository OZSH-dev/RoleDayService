from django.urls import path

from . import views

urlpatterns = [
    path('', views.transactions, name='transactions_root_list'),
    path('modify', views.modify_transaction_state, name='transactions_modify_handler')
]