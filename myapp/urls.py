from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet ,  SignupViewSet



urlpatterns = []
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'signup', SignupViewSet, basename='signup')



urlpatterns += router.urls
