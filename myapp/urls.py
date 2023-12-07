from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.index, name="index"),
    path('services', views.services, name="services"),
    path('about_us', views.about_us, name="about_us"),
    path('order/<int:service_id>', views.order, name="order"),
    path('services/<int:id>', views.services_show, name="service_index"),
    path('doctors/<int:id>', views.doctor_schedule),

]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
