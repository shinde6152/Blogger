from django.db import models

# create your models here



class contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=30)
    message = models.TextField()


    @staticmethod
    def get_contacts_data():
        return contacts.objects.all()
