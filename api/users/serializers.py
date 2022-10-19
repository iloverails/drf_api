from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.exceptions import TokenError
from django.db.models import Q
from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_blank=True)
    username = serializers.CharField(allow_blank=True)
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    @staticmethod
    def auth(username, email, password, **kwargs):
        try:

            user = User.objects.get(Q(username=username) | Q(email=email))
            if user:
                user.set_password(password)
            return user
        except User.DoesNotExist:
            return None

    def validate(self, data):
        email = data['email']
        username = data['username']
        password = data['password']

        user = self.auth(username=username, email=email, password=password)
        print(user)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                'role': user.role,
                'username': user.username
            }
            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField(read_only=True)

    default_error_messages = {
        'bad_token': 'Token is invalid or expired'
    }

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, attrs):
        self.refresh = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.refresh).blacklist()
        except TokenError:
            self.fail('bad_token')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
