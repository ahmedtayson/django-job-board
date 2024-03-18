from django.db import models

def Image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

class job(models.Model):
    x = [
        ('full time','full time'),
        ('part time','part time'),
    ]
    name = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15,choices=x)
    description = models.TextField(max_length=100)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Image_upload)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=25)
        
    def __str__(self):
        return self.name




# Create your models here.
