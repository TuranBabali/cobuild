from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)
    
    def get_projects(self):
        return Project.objects.filter(category=self)

class Project(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False,unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    image1 = models.ImageField(blank=False,null=False,upload_to='works/project')
    image2 = models.ImageField(blank=True,null=True,upload_to='works/project')
    image3 = models.ImageField(blank=True,null=True,upload_to='works/project')


    def __str__(self):
        return "{}".format(self.name)