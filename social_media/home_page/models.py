from django.db import models
from django.conf import settings
from PIL import Image


User = settings.AUTH_USER_MODEL


class PostLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    Timestamp = models.DateTimeField(auto_now_add=True)


class CommentLikes(models.Model):
    user_of_comment = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment = models.ForeignKey('PostComments', on_delete=models.CASCADE)
    Timestamp = models.DateTimeField(auto_now_add=True)


class PostComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    Timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True, through=CommentLikes)

    class Meta:
        ordering = ['comment','id']

    def __str__(self):
        return '%s' % (self.comment)


class Post(models.Model):
    comment = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    likes = models.ManyToManyField(User, related_name='poat_likes', blank=True, through=PostLikes)

    post_description = models.CharField(max_length=204)

    photo = models.ImageField(upload_to='uploded_post')
    Timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    @property
    def is_comment(self):
        return self.comment is not None

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        try:
            if img.height > settings.PHOTO_SIZE or img.weight > settings.PHOTO_SIZE:
                output_size = (settings.PHOTO_SIZE, settings.PHOTO_SIZE)
                img.thumbnail(output_size)
                img.save(self.photo.path)
        except Exception as e:
            print(e)

    def serialize(self, requst):
        return {"id": self.id, "post_description": self.post_description, "photo": settings.MEDIA_URL + str(self.photo),
                "likes": self.likes.all().count(), "user": f"{requst.user}"}
