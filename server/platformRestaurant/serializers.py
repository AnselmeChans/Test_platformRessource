from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_student', 'is_teacher')


class CustomRegisterSerializer(RegisterSerializer):
    is_student = serializers.BooleanField()
    is_teacher = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('user_firstname', 'user_lastname', 'user_email', 'user_password', 'user_birthdate')

    def get_cleaned_data(self):
        return {
            'user_firstname': self.validated_data.get('user_firstname', ''),
            'user_lastname': self.validated_data.get('user_lastname', ''),
            'user_email': self.validated_data.get('user_email', ''),
            'user_password': self.validated_data.get('user_password', ''),
            'user_birthdate': self.validated_data.get('user_birthdate', ''),
            'user_birthdate': self.validated_data.get('user_birthdate', ''),
            'is_particular': self.validated_data.get('is_particular', ''),
            'is_enterprise': self.validated_data.get('is_enterprise', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_student = self.cleaned_data.get('is_enterprise')
        user.is_teacher = self.cleaned_data.get('is_particular')
        user.save()
        adapter.save_user(request, user, self)
        return user


class TokenSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ('key', 'user', 'user_type')

    def get_user_type(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data
        is_particular = serializer_data.get('is_particular')
        is_enterprise = serializer_data.get('is_enterprise')
        return {
            'is_particular': is_particular,
            'is_enterprise': is_enterprise
        }