from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate


from .models import User, Info, Room


# User Serializer
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(
                        username=validated_data['username'], 
                        email=validated_data['email'], 
                        password=validated_data['password'])

        return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")


class InfoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Info 
        field = "__all__"

class RoomSerialiser(serializers.ModelSerializer):
    class Meta: 
        model = Room 
        field = "__all__"
        