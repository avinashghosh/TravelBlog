from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('blog', views.blog),
    path('filtered', views.filtered),
    path('addpost', views.addpost),
]
