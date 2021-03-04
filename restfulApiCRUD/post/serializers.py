from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    username= serializers.SerializerMethodField()
    class Meta:
        model= Post
        fields= ['username', 'title', 'content', 'slug', 'image', 'created', 'modifiedBy']

    def get_username(self, obj):
        return str(obj.user.username)
    
class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields= ['title', 'content', 'image']

    '''
    def validate_title(self, value):
        if value == 'deneme':
            raise serializers.ValidationError('Not valid')
        return value

    def validate(self, attrs):
        if attrs['title'] == 'deneme':
            raise serializers.ValidationError('Not valid')
        return value
    '''