from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

# Kullanıcı bilgilerini serileştiren serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Kullanıcıyı create_user metoduyla oluşturuyoruz
        user = User.objects.create_user(**validated_data)
        return user

# Kullanıcı kayıt işlemleri için serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Yeni kullanıcı oluşturulurken create_user kullanılarak şifre düzgün şekilde hashlenir.
        user = User.objects.create_user(**validated_data)
        return user
