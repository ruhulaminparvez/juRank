from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views

admin.site.site_header = "Admin Panel"
admin.site.site_title = "My Admin Portal"
admin.site.index_title = "Welcome to My Admin Panel"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('blog/<int:blog_id>', views.blog_details, name="blog_details"),
    path('contact/', views.contact, name='contact'),
    path('schedule/', views.schedule, name='schedule'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)