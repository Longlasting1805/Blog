from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100,
                             default='')
    content = models.CharField(max_length=1000,
                               default='')
    author = models.CharField(max_length=100,
                              default='')
    comment = models.TextField(max_length=1000,
                               unique=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    date = models.DateTimeField(null=True,
                                blank=True)
    post = models.ForeignKey(Blog, related_name='BlogPost', on_delete=models.CASCADE)

    def __str__(self):
        return self.post.comment
