from django.contrib.auth import views
from django.urls import path

from .views import (
    ArticleList, 
    ArticleCreateView, 
    ArticleUpdateView, 
    ArticleDelete, 
    LogoutView, 
    ProfileView,
    
)

app_name = 'account'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns += [
	path('', ArticleList.as_view(), name="home"),
    path('article/create', ArticleCreateView.as_view(), name='articlecreate'),
    path('article/update/<int:pk>', ArticleUpdateView.as_view(), name='articleupdate'),
    path('article/delete/<int:pk>', ArticleDelete.as_view(), name="article-delete"),
    path('profile', ProfileView.as_view(), name='profile'),


] 