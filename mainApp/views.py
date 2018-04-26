from .models import *
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = ('id','quantity')

@api_view(['GET'])
def product(request):
    p = Product.objects.all()
    s = ProductSerializer(p,many=True)
    return Response(s.data)
