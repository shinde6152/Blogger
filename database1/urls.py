from django.urls import path
from database1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage),
    path('blogs',views.blogs,name='blogs'),
    path('post',views.post,name='post'),
    path('destination',views.destination,name='destination'),
    path('categories',views.categories,name='categories'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
