from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), 
            on_delete=models.CASCADE,)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                                related_name='comments',
                                )
    comment = models.TextField()
    name = models.CharField(max_length=80)
    created_on =  models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    # author = models.ForeignKey(get_user_model,
    #         on_delete=models.CASCADE,
    #         )
    # date = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)

    def get_absolute_url(self):
        return reverse_lazy('home')