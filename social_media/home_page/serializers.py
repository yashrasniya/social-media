from rest_framework import serializers
from .models import Post, PostComments
from django.conf import settings

#-----------------Comment----Serializers------------------------------------




class PostCommentActionSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validated_action(self, value):
        value = value.lower().strip()
        if not value in settings.POST_ACTION_OPTION:
            raise serializers.ValidationError("this is not valid")
        return value



class PostCommentCreateSerializers(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = PostComments
        fields = ['id', 'post','comment', 'likes']

    def get_likes(self, obj):
        return obj.likes.count()

    def validate_content(self, value):
        if len(value) > settings.MAX_LENGTH:
            raise serializers.ValidationError("comment is very long")
        return value



class PostCommentSerializers(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    is_like = serializers.SerializerMethodField("_get_is_like")

    class Meta:
        model = PostComments
        fields = ['id', 'post', 'comment', 'likes', 'is_like']

    def _get_is_like(self, obj):
        qs = PostComments.objects.all().filter(id=obj.id).first().likes.all()
        request = self.context.get('request', None)
        if request:
            for a in qs:
                return a == request.user
        return False

    def get_likes(self, obj):
        return obj.likes.count()






#-----------------Post----Serializers------------------------------------
class PostCreateSerializers(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'post_description', 'photo', 'likes']

    def get_likes(self, obj):
        return obj.likes.count()

    def validate_content(self, value):
        if len(value) > settings.MAX_LENGTH:
            raise serializers.ValidationError("post_discription is very long")
        return value



class PostActionSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validated_action(self, value):
        value = value.lower().strip()
        if not value in settings.POST_ACTION_OPTION:
            raise serializers.ValidationError("this is not valid")
        return value

class PostSerializers(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    comment = PostCreateSerializers(read_only=True)
    post_comment = serializers.SerializerMethodField("_get_comments")
    is_like = serializers.SerializerMethodField("_get_is_like")

    class Meta:
        model = Post
        fields = ['id', 'post_description', 'photo', 'likes', 'is_comment', 'comment', 'post_comment', 'is_like']
        # fields='__all__'
        depth = 1

    def get_likes(self, obj):
        return obj.likes.count()

    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return str(request.user)

    def _get_is_like(self, obj):
        qs = Post.objects.all().filter(id=obj.id).first().likes.all()
        request = self.context.get('request', None)
        if request:
            for a in qs:
                return a == request.user
        return False

    def _get_comments(self, obj):
        id = obj.id
        data_ = PostComments.objects.filter(post=id)
        request = self.context.get('request', None)
        array = PostCommentSerializers(data_, many=True,context={'request': request}).data

        done, index, new_array = [], [], []
        for a in range(len(array)):
            max = 0
            for b in range(len(array)):
                if array[b]['id'] > max:
                    if array[b]['id'] not in done:
                        max = array[b]['id']
                        index.append(b)
            done.append(max)
            new_array.append(array[index[-1]])

        return new_array

    def get_post_description(self, obj):
        post_description = obj.post_description
        if obj.is_comment:
            post_description = obj.comment.post_description
        return post_description
