from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})
    
    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)    
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        
        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})    

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
    
    def delete(self, request, pk):
        try:
            instance = Women.objects.get(pk=pk)
        except Women.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"post": f"Women id: {pk} is deleted"})
       