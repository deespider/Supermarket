import json
import rest_framework.status as http_status
from core.views import BaseShopView
from shop.models import Item, Offer
from shop.serializers import OfferSerializer, ItemSerializer
from shop.utils import calculate_total


class OfferView(BaseShopView):
    
    template_name = "offer_management.html"

    def get(self, request):
        serializer = OfferSerializer(Offer.objects.all(), many=True)
        offers_data = json.dumps(serializer.data)
        items = Item.objects.all().order_by("-id")
        data = self.get_context_data({
            "offers": offers_data,
            "items": items,
        })
        return self.render(request, data)

    def post(self, request):
        data = {}
        try:
            serializer = OfferSerializer(data=request.POST)
            offers = Offer.objects.all()
            offer_serializer = OfferSerializer(offers, many=True)
            data = self.get_context_data({
                "offers": json.dumps(offer_serializer.data),
                "items": Item.objects.all().order_by("-id"),
            })

            if serializer.is_valid():
                serializer.save()
                data["message"] = "Item added successfully!"
            else:
                data["errors"] = serializer.errors
        except Exception as e:
            data["errors"] = f"Error: {str(e)}"
        
        return self.render(request, data)
        


class AddItemView(BaseShopView):
    
    template_name = "items_manager.html"

    def get(self, request):
        items = Item.objects.all().order_by("-id")
        serializer = ItemSerializer(items, many=True)
        data = self.get_context_data({
            "items": json.dumps(serializer.data),
        })
        return self.render(request, data)

    def post(self, request):
        data = {}
        try:
            serializer = ItemSerializer(data=request.POST)
            items = Item.objects.all().order_by("-id")
            items_serializer = ItemSerializer(items, many=True)

            data = self.get_context_data({
                "items": json.dumps(items_serializer.data)
            })

            if serializer.is_valid():
                serializer.save()
                data["message"] = "Item added successfully!"
            else:
                data["errors"] = serializer.errors
        except Exception as e:
            data["errors"] = f"Error: {str(e)}"

        return self.render(request, data)


class CheckoutView(BaseShopView):
    template_name = "checkout.html"

    def get(self, request):
        return self.render(request)

    def post(self, request):
        items = request.POST.get("cart", "")
        data = self.get_context_data({"cart": items})
        try:
            data["total_price"] = calculate_total(items.upper())
        except Exception as e:
            data["errors"] = str(e)

        return self.render(request, data)
        
