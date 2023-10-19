from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request):
    """DRF API View"""
    instance= Product.objects.all().order_by("?").last()
    data = {}
    
    if instance:
        # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={'content-type': 'application/json'})
