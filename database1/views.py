from django.shortcuts import render
from database1.models.khanda import khanda,Blog,fieldtype,favourite
from database1.models.khanda import country
from database1.models.countries import belize
from database1.models.contact import contacts

# Create your views here.



#                                          discovering new methods



# list(i.id for i in coun)                                                        it contains all id of country
# field_name = field_type.objects.values_list('name', flat=True)        #         help to access all ids





#                                         repeatable objects

field_name = fieldtype.objects.all()
blog = Blog.objects.all()
country = country.objects.all()




#                                          reptable input fields
# Assuming 'country' is your model name
# country_objects = country.objects.values_list('id', flat=True)









def homepage(request):
    field_name = fieldtype.objects.all()
    khandas=khanda.objects.all()
    blog=Blog.objects.all()
    field_name = fieldtype.objects.all()
    search_field = request.POST.get('search')
    no= 6
    # print(search_field)

    ids = 1
    if ids != None:
        type = Blog.get_type_by_id(ids)
    else:
        print("Please select view ids")

    ids = 2
    if ids != None:
        second = Blog.get_type_by_id(ids)
    else:
        print("Please select view ids")




    #
    # ids = field_type.objects.values_list('id', flat=True
    # list1=list(i for i in ids)
    # len_list1 = len(list1)-1          # length of list1
    #
    # while list1 !=None:
    #     i = list1[len_list1]
    #     if i != None:
    #         type = Blog.get_type_by_list(i)
    #     else:
    #             print("Please select")
    #     len_list1 = len(list1)-1
    #

    data={
        'khandas': khandas,
        'type': type,
        'second':second,
        'field_name': field_name,
        'country' : country,
        'no':no,
    }


    return render(request,'home.html',data)


def blogs(request):
    field_name = fieldtype.objects.all()
    blog = belize.objects.all()
    favo_id = favourite.objects.values_list('id', flat=True)
    for i in favo_id:
        if i==1:
            blog = Blog.get_data_by_favourite(i)
        else:
            pass

    data = {
        'blog': blog,
        'field_name': field_name,
        'country': country,
    }

    return render(request,'blogs.html',data)

def post(request):
    dest_id = request.GET.get("dest_id")
    category_data = request.GET.get("category_data")
    home_data = request.GET.get("home_data")
    blog = request.GET.get("blog")



    if category_data != None:
        if category_data != None:
            blog_data = Blog.get_Blog_by_category_data(category_data)
        else:
            print('category data is not')


    elif dest_id != None:
        if dest_id != None:
            blog_data = Blog.get_Blog_by_dest_id(dest_id)
        else:
            print('dest_id is not')

    elif home_data != None:
        if home_data != None:
            blog_data = Blog.get_data_by_country(home_data)
        else:
            print('home data is not')

    elif blog != None:
        if blog != None:
            blog_data = Blog.get_Blog_by_blog_data(blog)
        else:
            print('blog data is not')


    else:
        blog_data = Blog.objects.all()




    data = {
        'field_name': field_name,
        'country': country,
        'blog_data' : blog_data,
        # 'category_data' : category_data,

    }
    return render(request,'post.html',data)


def destination(request):
    khan = khanda.objects.all()
    a=1
    b=2
    list1 = 1
    country_id = request.GET.get("country_id")


    if country_id != None:
        blog_data =Blog.get_Blog_by_destination_id(country_id)
    else:
        blog_data = Blog.objects.all()





    if list1:
        blog=Blog.get_Blog_by_country_id(list1)
    else:
        blog=Blog.get_all_Blog()

    data = {
        'blog': blog,
        'field_name': field_name,
        'blog_data': blog_data,
        'country': country,

    }

    return render(request,'destination.html',data)


def categories(request):
    field_id = request.GET.get("field_id")
    print(field_id)
    if field_id != None:
        blog = Blog.get_data_by_field_id(field_id)
    else:
        blog= Blog.objects.all()

    data = {
        'field_name': field_name,
        'blog': blog,
        'country': country,

    }
    return render(request,'categories.html',data)



def about(request):

    data = {
        'field_name': field_name,
    }

    return render(request,'about.html',data)


def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, email, subject, message)

        contact_obj=contacts(name=name,email=email,subject=subject,message=message)
        contact_obj.save()

    data = {
        'field_name': field_name,
        'country': country,
    }
    return render(request,'contact.html',data)















    #
    # Products = product.get_all_products()
    # categories = category.objects.all()
    # category_id=request.GET.get("category")
    # if category_id:
    #     Products=product.get_product_by_category_id(category_id)
    # else:
    #     Products =product.get_all_products()
    #
    # data ={
    #     'categories': categories,
    #     'Products':Products
    # }

