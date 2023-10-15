from django.db import models

# Create your models here.

class Blog(models.Model):
    postId=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    head0=models.CharField(max_length=500,default="")
    category=models.CharField(max_length=500,default="")
    desc0=models.CharField(max_length=5000,default="")
    head1=models.CharField(max_length=500,default="")
    desc1=models.CharField(max_length=5000,default="")
    head2=models.CharField(max_length=500,default="")
    desc2=models.CharField(max_length=5000,default="")
    pubDate=models.DateField()
    thumbnails=models.ImageField(upload_to='blog/images',default="")

    def __str__(self):
        return self.title
