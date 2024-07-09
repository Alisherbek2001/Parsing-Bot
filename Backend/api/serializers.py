from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # file_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'file', 'created_at', 'updated_at']

    # def get_file_url(self, obj):
    #     if obj.file:
    #         return self.context['request'].build_absolute_uri(obj.file.url)
    #     return None