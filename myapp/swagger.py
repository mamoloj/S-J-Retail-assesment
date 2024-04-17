from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="My API SAMPLE for ASSESMENT",
        default_version='v1',
        description="Description of my API",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="test@test.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,), 
)
