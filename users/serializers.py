from rest_framework import serializers

from dj_rest_auth.registration.serializers import RegisterSerializer

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from .models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(
        max_length=30,
        required=True,
    )
    last_name = serializers.CharField(
        max_length=30,
        required=True,
    )

    def get_cleaned_data(self):
        return {
            "username": self.validated_data.get("username", ""),
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data["password1"], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
                )
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user
