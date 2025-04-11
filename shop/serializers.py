from rest_framework import serializers
from shop.models import Item, Offer


class OfferSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True)
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())

    class Meta:
        model = Offer
        fields = ['id', 'item', 'item_name', 'quantity', 'offer_price', 'valid_from', 'valid_till']

    def validate(self, data):
        if data.get('valid_till') and data.get('valid_till') <= data.get('valid_from'):
            raise serializers.ValidationError("valid_till must be after valid_from")
        return data
    


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'unit_price']

    # def validate(self, data):
    #     if data['valid_until'] <= data['valid_from']:
    #         raise serializers.ValidationError("valid_until must be after valid_from")
    #     return data