from rest_framework import serializers

from apps.modules.models import ModuleModel, ModulePreviewVideosModel


class ModulePreviewVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModulePreviewVideosModel
        fields = ('id', 'link', 'updated_at', 'created_at')


class ModuleSerializer(serializers.ModelSerializer):
    previews = ModulePreviewVideoSerializer(many=True, read_only=True)

    class Meta:
        model = ModuleModel
        fields = ('id', 'name', 'updated_at', 'created_at', 'previews')
