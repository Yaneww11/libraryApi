from django.contrib.auth import get_user_model
from rest_framework import serializers


UserModel = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username','email', 'password']
        # One way to hide password in response
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            **validated_data
        )

        return user

    # Another way to hide password in response
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation.pop('password', None)
    #     return representation

class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class LoginResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
    message = serializers.CharField()

class LogoutRequestSerializer(serializers.Serializer):
    refresh = serializers.CharField()

class LogoutResponseSerializer(serializers.Serializer):
    message = serializers.CharField()