from django.db import models

class belize(models.Model):
    image = models.ImageField(upload_to="belize/")
    heading = models.CharField(max_length=40)
    description = models.TextField()
    image2 = models.ImageField(upload_to="belize/")
    heading2 = models.CharField(max_length=40)
    description2 = models.TextField()

    def __str__(self):
        return self.heading

    @staticmethod
    def get_all_belize():
        return belize.objects.all()

