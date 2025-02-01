from django.contrib import admin
from django.urls import path, include
from faq_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')), 
    path('faq/', include('faq_app.urls')),  
    path('', views.home, name='home'),  
]

