from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",'username', 'email','phone', 'password')
    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'],
                        username=validated_data['username'],
                        phone=validated_data['phone'],
                        password=validated_data['password']
                                        )
        return user