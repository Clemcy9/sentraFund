from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CustomRegistrationSerializer(RegisterSerializer):
    fullname = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'fullname', 'email', 'password1', 'password2']

    def save(self, request):
        user = super().save(request)
        user.set_full_name(self.validated_data.get('fullname',''))
        user.save()
        return user
    
class CustomUserDetailSerializer(UserDetailsSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_superuser']