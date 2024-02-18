from django.db import models

class country_list(models.Model):
    country = models.CharField(max_length=30)


class country(models.Model):
    country_name = ForeignKey(country.on_delete=models.CASCADE)
    image = models.ImageField(upload_to="belize/")
    heading = models.CharField(max_length=40)
    description = models.TextField()
    image2 = models.ImageField(upload_to="belize/")
    heading2 = models.CharField(max_length=40)
    description2 = models.TextField()

    @staticmethod
    def get_all_country():
        return country.objects.all()
