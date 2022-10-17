from django.db.models import fields
from rest_framework import serializers
from applicationDetails.models import Applications


class ApplicationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applications
        fields = "__all__"

def get_image_url(self, obj):
    return obj.image.url


