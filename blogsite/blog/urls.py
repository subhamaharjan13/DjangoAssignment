from django.urls import path
from .views import (list_all_blog, detail_view_of_blog, 
                    create_blog_info, update_blog_info, delete_blog_info)

urlpatterns = [
    #blog/list
    path('list/', list_all_blog),
    path('create/', create_blog_info),
    path('detail/<int:blog_id>/', detail_view_of_blog),
    path('update/<int:blog_id>/', update_blog_info),
    path('delete/<int:blog_id>/', delete_blog_info),
]