from django.db import models
from django.urls import reverse_lazy 
from django.utils import timezone
from django.utils.html import format_html
from account.models import User

from ckeditor_uploader.fields import RichTextUploadingField

class ArticleManager(models.Manager):
	def published_art(self):
		return self.filter(status='p')

        
 

class Article(models.Model):
	STATUS_CHOICES = (
		('d', 'پیش‌نویس'),		 # draft
		('p', "منتشر شده"),		 # publish
  		('i', "در انتظار تایید"),		 # 
		('b', "رد شده"),		 # 

	)
 
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authers', null=True, blank=True)
	title = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, db_index=True)
	category = models.ManyToManyField('Category', related_name='articles')
	description = RichTextUploadingField()
	thumbnail = models.ImageField(upload_to="images")
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	is_special = models.BooleanField(default=False)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	objects = ArticleManager()

	class Meta:
		ordering = ['-updated', '-created','-publish']
  
	def category_pub(self):
		return self.category.filter(status=True)

	def thumbnail_tag(self):
		return format_html("<img style='width: 100%; height: 80px; ' src='{}'>".format(self.thumbnail.url))
	thumbnail_tag.short_description = 'thumbnail'
 
	def category_to_str(self):
		return ' ,'.join([category.title for category in self.category.filter(status=True)])
	category_to_str.short_description = 'category'
 
	def get_absolute_url(self):
		return reverse_lazy('account:home')

	def __str__(self):
		return self.title


class Category(models.Model):
	title = models.CharField(max_length=200, db_index=True, unique=True)
	slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)
	created = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)
	position = models.PositiveSmallIntegerField(default=1)


	class Meta:
		ordering = ['position','-created',]
  
	
    
	def __str__(self):
		return self.title