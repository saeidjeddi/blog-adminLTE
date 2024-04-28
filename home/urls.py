from django.urls import path
from home import views as home


app_name = 'home'
urlpatterns = [
    path('dateile/<int:pk>/<slug:slug>', home.DetaileBlogView.as_view(), name='dateile'),
    path('preview/<int:pk>', home.DetaileBlogPreView.as_view(), name='previw'),
    path('category/<slug:slug>', home.CategoryBlogView.as_view(), name='category'),
    path('author/<slug:username>', home.AuthorList.as_view(), name="author"),

    path('', home.HomeBlogView.as_view(), name='index'),
    
]