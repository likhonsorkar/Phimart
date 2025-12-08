from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializers


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'email', 'password','address', 'phone']
class UserSerializer(BaseUserSerializers):
    class Meta(BaseUserSerializers.Meta):
        fields = ['id', 'first_name', 'last_name', 'email','address', 'phone']

