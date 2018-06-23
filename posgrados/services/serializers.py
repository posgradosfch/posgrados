from django.contrib.auth.models import User, Group
from rest_framework import serializers


from .models import Usuario2, Rol,Permiso, RolPermiso, Noticia

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario2
        fields= '__all__'
        extra_kwargs ={'contrasena': {'write_only': True, 'required': True}}

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'

class RolPermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolPermiso
        fields = '__all__'

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'