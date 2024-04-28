from django import template
from home.models import Category
  
register = template.Library()
  
@register.inclusion_tag('home/partiasl/category.html')
def category():
    return {
        'category': Category.objects.filter(status=True)
    }
