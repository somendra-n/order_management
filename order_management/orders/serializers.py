# orders/serializers.py

from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.
    Converts Order instances into JSON format and
    validates data when creating/updating orders via API.
    """

    class Meta:
        # Specify the model to serialize
        model = Order
        
        # Fields to include in the serialized output and input validation
        fields = ['id', 'title', 'description']
        # 'id' is included so the client knows the unique identifier of each order
