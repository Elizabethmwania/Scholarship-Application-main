from django.db.models import fields
from rest_framework import serializers
from sponsoredApplications.models import SponsoredApplications


class SponsoredApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsoredApplications
        fields = "__all__"

def get_image_url(self, obj):
    return obj.image.url


