from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=10)
    contents = models.TextField(editable=True)
    url = models.URLField(editable=True)
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
