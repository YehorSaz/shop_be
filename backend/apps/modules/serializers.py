from rest_framework import serializers

from pytube import Playlist

from core.dataclasses.module_dataclass import Module

from apps.modules.models import ModuleModel


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleModel
        fields = ('id', 'name', 'preview_playlist', 'updated_at', 'created_at')
        extra_kwargs = {
            'preview_playlist': {
                'write_only': True
            }
        }


class ModuleDetailsSerializer(ModuleSerializer):
    def to_representation(self, instance: Module):
        urls_dict = {'preview_links': None}

        if instance.preview_playlist:
            urls = Playlist(instance.preview_playlist)
            urls_dict = {'preview_links': [link for link in urls]}

        representation = super().to_representation(instance)
        representation |= urls_dict
        return representation


class ModuleResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleModel
        fields = ('id', 'name', 'updated_at', 'created_at')
