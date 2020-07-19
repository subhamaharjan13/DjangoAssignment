from django.urls import path
from .views import (list_all_blog, detail_view_of_blog, 
                    create_blog_info, update_blog_info, delete_blog_info, list_all_author, add_author)

urlpatterns = [
    #webapp/list
    path('list/', list_all_blog),
    path('create/', create_blog_info),
    path('add-author/', add_author),
    path('author/', list_all_author),
    path('detail/<int:user_id>/', detail_view_of_blog),
    path('update/<int:user_id>/', update_blog_info),
    path('delete/<int:user_id>/', delete_blog_info),
]