from rest_framework import serializers

class BaseModelSerializer(serializers.ModelSerializer):
    """
    Base serializer with common functionality
    """
    class Meta:
        abstract = True
    
    def validate(self, attrs):
        """
        Add common validation logic
        """
        return super().validate(attrs)
