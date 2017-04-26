from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend,FilterSet
import django_filters.rest_framework

from .models import Package
from .serializers import PackageSerializer,PackageallSerializer

@api_view(['GET'])
def api_root(request,format=None):
    """api root"""
    return Response({
        'users':reverse('userlist',request = request,format=format),
        'packages':reverse('api_package',request=request,format=format),
    })


class PackageAPI(APIView):
    """the package api"""
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request):
        package = Package.objects.all()
        serializer = PackageSerializer(package,many=True)
        return Response(serializer.data,status=HTTP_200_OK)


class PackageFilter(FilterSet):
    """package filter"""
    class Meta:
        model = Package
        fields = {'name': ['exact', 'icontains'],}

class PackageAllAPI(generics.ListAPIView):
    """filter api by user"""
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    #filter_backends = (DjangoFilterBackend,)
    #filter_fields = ['name','status']
    filter_class = PackageFilter

    # def get_queryset(self):
    #      username = self.request.query_params.get('username',None   )
    #      package = Package.objects.filter(user_id__name = username)
    #      return package