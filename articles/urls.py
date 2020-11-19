from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('index', views.article_views,  name='article'),
    path('create', views.create_article, name='create'),
    path(r'^(?P<slug>[\W-]+)/$',views.article_details, name="detail")
]