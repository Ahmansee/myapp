from django.urls import path
from . import views
from articles import views as art_views

app_name = 'blog'


urlpatterns = [ 
    path('index', art_views.article_views,  name='home'),
    path('contactUs', views.info, name='contacts'),
    path('', views.login_views, name='loginuser'),
    path('logoutuser', views.logout_views, name='logoutuser'),
    path('category', views.catagory,  name='catagory'),
]
