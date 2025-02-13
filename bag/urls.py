from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag_view, name='bag_view'),
    path('add/<item_id>', views.add_to_bag, name='add_to_bag'),
    path('update/<item_id>', views.update_bag, name='update_bag'),
]