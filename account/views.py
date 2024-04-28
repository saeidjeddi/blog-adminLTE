from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FieldsMixin, FormValidMixin, AuthorAccessMixin, SuperUserAccessMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth import logout
from account.models import User

from home.models import Article
from account.forms import ProfileForm



class ArticleList(LoginRequiredMixin, ListView):
	paginate_by = 3
	template_name = "registration/home.html"
 
	def get_queryset(self):
		if self.request.user.is_superuser:
			return Article.objects.all()
		else:
			return Article.objects.filter(author=self.request.user)

class ArticleCreateView(LoginRequiredMixin, FieldsMixin, FormValidMixin ,CreateView):
    model = Article
    template_name = 'registration/article_update.html'
    

class ArticleUpdateView(LoginRequiredMixin, FieldsMixin, FormValidMixin, AuthorAccessMixin ,UpdateView):
    model = Article
    template_name = 'registration/article_update.html'
    

class ArticleDelete(SuperUserAccessMixin, DeleteView):
	model = Article
	success_url = reverse_lazy('account:home')
	template_name = "registration/article_confirm_delete.html"



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
    
    
    
class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'registration/profile.html'
    form_class = ProfileForm

    success_url = reverse_lazy('account:profile')
    
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
    
    def get_form_kwargs(self):
        kwargs = super(ProfileView, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs  
