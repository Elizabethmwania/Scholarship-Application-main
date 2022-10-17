from djoser.serializers import UserCreateSerializer

from django.contrib.auth import get_user_model
UserDetails = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = UserDetails
        fields = ('id','email', 'name','phone_number','role', 'password')