from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from .views import AddPostView


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    # title tag that will go to html
    title_tag = models.CharField(max_length=255, default=title)
    # check for meta tags for SEO!!!

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # this name is in the error - it has to be named like this
        return reverse('article-detail', args=(str(self.id)))


