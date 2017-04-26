#python builtin
from logging import getLogger

#django here
from django.contrib.auth import get_user_model,authenticate

#third party package here
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings

User = get_user_model()
logger = getLogger('project')
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserSerializer(serializers.ModelSerializer):
    """user serializer"""
    pu = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id','name','pu']


class UserCreateSerializer(serializers.ModelSerializer):
    """usr crate serialize"""
    password = serializers.CharField(write_only = True)

    def create(self,validated_data):
        """custom user"""
        name = validated_data['name']
        email = validated_data['email']
        user = User.objects.create(name=name,email=email)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_password(self,value):
        """check password"""
        if len(value) < 6:
            raise serializers.ValidationError("the password at least 6 long,please try again.")
        return value

    def validate_name(self,value):
        """validate user name"""
        queryset = User.objects.all()
        name_list = [user.name for user in queryset]
        if value in name_list:
            raise serializers.ValidationError("user with this name already exists.")
        return value


    class Meta:
        model = User
        fields = ['email','name','password']


class UserLoginSerializer(serializers.ModelSerializer):
    """user login serailzie"""
    email = serializers.EmailField(label='Email Address')
    class Meta:
        model = User
        fields = ['email','password']
        extra_kwargs = {
            "password":{"write_only":True},
        }

    def validate_email(self,data):
        user = User.objects.filter(email=data)
        if not user:
            raise serializers.ValidationError("user with this name not exists.")
        return data


class UserLoginTokenSerializer(JSONWebTokenSerializer):
    """user login serailzie"""
    def validate_email(self,data):
        if not data:
            raise serializers.ValidationError("This field may not be blank.")
        user = User.objects.filter(email=data)
        if not user:
            raise serializers.ValidationError("user with this name not exists.")
        return data

    def validate_password(self,data):
        if not data:
            raise serializers.ValidationError("This field may not be blank. ")
        return data

    def validate(self, attrs):
        """override the validate method"""
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }
        print(credentials.values())
        logger.info('credentails values {}'.format(credentials.values()))
        if all(credentials.values()):
            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = 'the username or password may not be true please try again.'
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "{username_field}" and "password".')
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)
        #return super(UserLoginTokenSerializer,self).validate(attrs)
