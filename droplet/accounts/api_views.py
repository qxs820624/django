#python builtin here
from logging import getLogger

#django package here
from django.contrib.auth import get_user_model
User = get_user_model()
logger = getLogger('project')

#third party package here
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework_jwt.views import ObtainJSONWebToken,JSONWebTokenAPIView
from rest_framework_jwt.settings import api_settings
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

#self define package here
from .serializers import UserSerializer,UserCreateSerializer,UserLoginSerializer,UserLoginTokenSerializer

class UserList(generics.ListAPIView):
    """use cbv method"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """user detail api"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUserView(generics.CreateAPIView):
    """user create api"""
    model = User
    serializer_class = UserCreateSerializer
    permisson_classes = (AllowAny)


class UserLoginView(APIView):
    permission_class = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self,request):
        data = request.data
        serialize = UserLoginSerializer(data=data)
        if serialize.is_valid(raise_exception=True):
            return Response(serialize.data,status = HTTP_200_OK)
        return Response(serialize.errors,status=HTTP_400_BAD_REQUEST)

from django.views.decorators.csrf import csrf_exempt

class UserLoginTokenAPIView(JSONWebTokenAPIView):
    """user login obtain json token"""
    serializer_class = UserLoginTokenSerializer

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        logger.info('the request data:{}'.format(request.data))
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)

            return Response(response_data,status=HTTP_200_OK)
            #response['Access-Control-Allow-Origin'] =

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)