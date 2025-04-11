from collections import Counter
from django.db.models import Q
from django.utils import timezone
from shop.models import Item, Offer



def calculate_total(cart):
    """
    Function to calculate total amount based on cart input and offers

    Parameters
    ----------
    cart : Queryset

    Returns
    -------
    total : float

    Raises
    ------
    ValueError
    """
    total = 0
    item_map = {}
    for name in cart:
        item_map[name] = item_map.get(name, 0) + 1
    total = 0
    now = timezone.now()
    item_lookup = {item.name: item for item in Item.objects.all()}

    for name, frequency in item_map.items():
        item = item_lookup.get(name)
        if not item:
            raise ValueError(f"Invaild Item or Item Doesn't exists: '{name}'")
        offers = Offer.objects.filter(
            Q(item=item) &
            Q(valid_from__lte=now) &
            (Q(valid_till__gte=now) | Q(valid_till__isnull=True))
        ).order_by('-id')

        offer_exists = False
        for offer in offers:
            if frequency >= offer.quantity:
                offer_group = frequency // offer.quantity
                remainder = frequency % offer.quantity
                total += offer_group * offer.offer_price + remainder * item.unit_price
                offer_exists = True
                break

        if not offer_exists:
            total += frequency * item.unit_price
    return total