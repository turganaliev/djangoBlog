from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text