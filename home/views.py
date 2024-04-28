from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from home.models import Article, Category
from account.models import User
from account.mixins import AuthorAccessMixin

class HomeBlogView(View):
    def get(self, request):
        article = Article.objects.filter(status='p')
        category = Category.objects.filter(status=True)
        paginator = Paginator(article, 3)
        page_number = request.GET.get('page', 1)
        try:
            posts = paginator.page(page_number)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            posts = paginator.page(1)

        
            

        return render(request, 'home/index.html', {'art': posts, 'cat': category })
    
    
class DetaileBlogView(DetailView):
    template_name = 'home/article-single.html'
    context_object_name = 'detaile'  
     
    def get_object(self):
        slug = self.kwargs.get('slug')
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk, slug=slug, status='p')
    
class DetaileBlogPreView(AuthorAccessMixin, DetailView):
    template_name = 'home/article-single.html'
    context_object_name = 'detaile'  
     
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)
    
    
    
class CategoryBlogView(View):
    def get(self, request, slug):
        category = get_object_or_404(Category,slug=slug, status=True)
        return render(request, 'home/category.html', {'category': category})
    

class AuthorList(ListView):
    paginate_by = 6
    template_name = 'home/author_list.html'

    
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.authers.all()
    
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['author'] = author
        return context