from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    
class BlogTag(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    tag = models.CharField(max_length=20)
    
    def __str__(self):
        return self.tag

class BlogAsset(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    asset = models.ImageField(upload_to="blog/assets/")
    
class BlogLike(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['blog', 'user'], name='max_one_comment_per_user')
        ]

    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog.title}'
    
class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
class Reply(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Reply by {self.user.username}'