from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage.as_view(), name='homepage'),
    path('blog/', views.blogView.as_view(), name='blog'),
    path('blog/<slug:slug>', views.blogdetail.as_view(), name='blogdetail'),
]