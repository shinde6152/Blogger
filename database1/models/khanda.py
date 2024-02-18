from django.db import models


#   Database of khanda

class favourite(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name



class khanda(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class country(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name




class fieldtype(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Blog(models.Model):
    khanda=models.ForeignKey(khanda,on_delete=models.CASCADE,default=1)
    country=models.ForeignKey(country,on_delete=models.CASCADE,default=1)
    field_type=models.ForeignKey(fieldtype,on_delete=models.CASCADE)
    favourite_type = models.ForeignKey(favourite,on_delete=models.CASCADE,default=1)
    image11 = models.ImageField(upload_to="belize/")
    heading = models.CharField(max_length=80)
    description = models.TextField()
    image22 = models.ImageField(upload_to="belize/")
    heading2 = models.CharField(max_length=80)
    description2 = models.TextField()

    @staticmethod
    def get_all_Blog():
        return Blog.objects.all()


    @staticmethod
    def get_Blog_by_country_id(list1):
        if list1:
            return Blog.objects.filter(country_id=list1)
        else:
            Blog.objects.all()

    def get_type_by_id(ids):
        if ids != None:
            return Blog.objects.filter(field_type=ids)
        else:
            print("Please select ids")

    def get_type_by_list(i):
        if i != None:
           return Blog.objects.filter(field_type=i)
        else:
            print("Please get ids")

    def get_data_by_field_id(field_id):
        if field_id != None:
            return Blog.objects.filter(field_type=field_id)
        else:
            blog.objects.all()

    def get_data_by_favourite(i):
        if i != None:
            return Blog.objects.filter(favourite_type=i)
        else:
            Blog.objects.all()

    def get_Blog_by_destination_id(country_id):
        if  country_id:
            return Blog.objects.filter(country=country_id)
        else:
            Blog.objects.all()

    def get_Blog_by_dest_id(dest_id):
        if dest_id:
            return Blog.objects.filter(heading2=dest_id)
        else:
            Blog.objects.all()


    def get_Blog_by_category_data(dest_id):
        if dest_id:
            return Blog.objects.filter(heading2=dest_id)
        else:
            Blog.objects.all()


    def get_data_by_country(home_data):
        if home_data != None:
            return Blog.objects.filter(heading2=home_data)
        else:
            Blog.objects.all()

    def get_Blog_by_blog_data(blog):
        if blog:
            return Blog.objects.filter(heading=blog)
        else:
            Blog.objects.all()


