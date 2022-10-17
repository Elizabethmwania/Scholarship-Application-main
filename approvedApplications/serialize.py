from django.db.models import fields
from rest_framework import serializers
from approvedApplications.models import ApprovedApplications


class ApprovedApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovedApplications
        fields = "__all__"

def get_image_url(self, obj):
    return obj.image.url


