from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Test by Liju to test a name field for testing the APIView"""
    name = serializers.CharField(max_length=9)

    
