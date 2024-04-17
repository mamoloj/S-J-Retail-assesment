from rest_framework import viewsets , status
from rest_framework.permissions import IsAuthenticated
from .models import Product , User
from .serializers import ProductSerializer , ProductCreateSerializer  , UserSerializer
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



class SignupViewSet(viewsets.ViewSet):  # Make sure to inherit from ViewSet
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD),
        },
        required=['username', 'email', 'password']
    ),
    responses={200: 'User created successfully'}
    )

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(owner=user, is_deleted=False)


    def get_serializer_class(self):
        # Use different serializer for creation
        if self.action == 'create':
            return ProductCreateSerializer
        return ProductSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
