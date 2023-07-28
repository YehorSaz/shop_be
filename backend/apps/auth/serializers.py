import os

from rest_framework import serializers


class UserActivationResponseSerializer(serializers.Serializer):
    url = serializers.CharField(default=f'{os.environ.get("FRONTEND")}/auth/activate/<token>')
