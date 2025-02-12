from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total > 0 and total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY
    else:
        delivery = 0

    grand_total = total + delivery    

    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "grand_total": grand_total,
    }

    return context