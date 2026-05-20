from rest_framework.viewsets import ModelViewSet

from product.models import Category
from product.serializers.category_serializer import CategorySerializer


# ✅ CORRETO
from rest_framework.permissions import AllowAny

class CategoryViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all().order_by('id')