import json
from django.shortcuts import render
import rest_framework.status as http_status
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from shop.models import Item, Offer
from shop.serializers import OfferSerializer, ItemSerializer
from django.views import View
from django.shortcuts import render
from shop.utils import calculate_total
from collections import Counter
from django.db.models import Q
# Create your views here.


class OfferView(View):
    def __init__(self, **kwargs):
        self.template_name = 'offer_management.html'

    def get(self, request):
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)
        offers_data = json.dumps(serializer.data)
        
        items = Item.objects.all().order_by('-id')
        return render(request, self.template_name, {
            'offers': offers_data,
            'items': items,
            'current_date': timezone.now()
        })

    def post(self, request):
        data = {}
        try:
            serializer = OfferSerializer(data=request.POST)
            offers = Offer.objects.all()
            offer_serializer = OfferSerializer(offers, many=True)
            data = {
                "offers": json.dumps(offer_serializer.data),
                "items": Item.objects.all().order_by('-id'),
                "current_date" : timezone.now()
            }

            if serializer.is_valid():
                serializer.save()
                data['message'] = "Item added successfully!"
            else:
                data['errors'] = serializer.errors
        except Exception as e:
            data['errors'] = f"Error: {str(e)}"
        
        return render(request, self.template_name, data)
        


class AddItemView(View):
    def __init__(self, **kwargs):
        self.template_name = 'items_manager.html'

    def get(self, request):
        items = Item.objects.all().order_by('-id')
        serializer = ItemSerializer(items, many=True)
        return render(request, self.template_name, {
            'items': json.dumps(serializer.data),
            'current_date': timezone.now()
        })

    def post(self, request):
        data = {}
        try:
            serializer = ItemSerializer(data=request.POST)
            items = Item.objects.all().order_by('-id')
            items_serializer = ItemSerializer(items, many=True)

            data = {
                'items': json.dumps(items_serializer.data)
            }

            if serializer.is_valid():
                serializer.save()
                data['message'] = "Item added successfully!"
            else:
                data['errors'] = serializer.errors
        except Exception as e:
            data['errors'] = f"Error: {str(e)}"

        return render(request, self.template_name, data)


class CheckoutView(View):
    def __init__(self, **kwargs):
        self.template_name = 'checkout.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            items = request.POST.get('cart', '')
            total_price = calculate_total(items.upper())
            data = {
                'cart': items,
                'total_price': total_price
            }
        except Exception as e:
            data = {
                'cart': items,
                'errors' : {str(e)}
            }

        return render(request, self.template_name, data)
        
