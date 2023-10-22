from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request):
    """DRF API View"""
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        print(serializer.data)
        return Response(serializer.data)
    return Response({'invalid data': 'not a good data'}, status=400)
