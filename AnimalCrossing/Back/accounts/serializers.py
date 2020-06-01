from rest_framework import serializers
from .models import User
from django.core.validators import ValidationError

from django.db.models import Q



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username']
class UserLoginSerializer(serializers.ModelSerializer):

    token = serializers.CharField(allow_blank=True,read_only=True)
    username = serializers.EmailField(required=False, allow_blank=True)
    email = serializers.EmailField(label='Email Address',required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
        'username',
        'email',
        'password',
        'token',
        ]
        extra_kwargs = {'password':{"write_only":True}}

        def validate(self, data):

            email = data.get("email", None)
            username = data.get("username", None)
            password = data.get("password",None)

            if not email and not username :
                raise ValidationError("A username and email is required to login")

            user = User.objects.filter(
            Q(email=email)|
            Q(username=username)
            ).distinct()

            if user.exists() and user.count() == 1:
                user_obj = user.first()
            else:
                raise ValidationError("A username/email is not valid")

            if user_obj:
                if not user_obj.check_password(password):
                    raise ValidationError("Incorrect credentials please try again")

            return data
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username']
            
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user