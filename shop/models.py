from django.db import models
from core.models import CreateUpdateStatusAbstractModel
from django.utils import timezone

class Item(CreateUpdateStatusAbstractModel):
    name = models.CharField(max_length=20, unique=True)
    unit_price = models.FloatField()

    def __str__(self):
        return self.name

class Offer(CreateUpdateStatusAbstractModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    offer_price = models.FloatField()
    valid_from = models.DateTimeField(default=timezone.now)
    valid_till = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} {self.item.name} for {self.offer_price}"