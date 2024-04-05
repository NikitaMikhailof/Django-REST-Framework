from .models import Women
from rest_framework import generics
from .serializers import WomenSerializer


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

