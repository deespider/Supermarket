from django.urls import path
from shop.views import OfferView, AddItemView

urlpatterns = [
    path('add-item/', AddItemView.as_view(), name='add_item'),
    path('offers/', OfferView.as_view(), name='offers_create_view'),
]