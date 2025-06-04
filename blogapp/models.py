from django.db import models

# Create your models here.
class Catagory(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Catagory,on_delete=models.CASCADE)

    def __str__(self):
        return self.title