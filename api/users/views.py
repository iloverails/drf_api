from rest_framework import (
    views,
    status,
    response,
    generics
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserSerializer
)

from django.contrib.auth import logout
from api.permissions import (
    IsAdmin,
    IsTenant,
    IsLandlord,
    IsReviewer
)
from .models import User


class UserRegistrationView(views.APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            return response.Response({
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'user': serializer.data
            }, status=status_code)


class UserLoginView(views.APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_200_OK

            return response.Response({
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'username': serializer.data['username'],
                    'email': serializer.data['email'],
                    'role': serializer.data['role']
                }
            }, status_code)


class HelloView(views.APIView):
    permission_classes = (IsAuthenticated, IsAdmin, )

    @staticmethod
    def get(request):
        content = {'message': 'Hello, World!'}
        return response.Response(content)


class UserLogoutView(views.APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request):
        logout(request)
        # token = RefreshToken(request.data['refresh'])
        # token.blacklist()
        return response.Response(status=status.HTTP_200_OK)


class UsersListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = UserSerializer
    queryset = User.objects.all()
