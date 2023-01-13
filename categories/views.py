from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.filter(
        kind_major=Category.CategoryKindMajorChoices.CONTENTS,
    )
