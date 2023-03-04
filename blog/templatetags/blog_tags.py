from django import template
from django.db.models import Count
from taggit.models import Tag
from ..models import Post

register = template.Library()

@register.simple_tag
def comment_count(post_id):
    post = Post.objects.get(id=post_id)
    return post.comments.filter(active=True).count()


@register.inclusion_tag('snippets/used_tags.html')
def show_used_tags(count=20):
    used_tags = Post.tags.all()[:count]
    print(type(used_tags))
    return {'used_tags': used_tags}

@register.inclusion_tag('snippets/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.inclusion_tag('snippets/most_commented_posts.html')
def show_most_commented_posts(count=5):
    most_commented_posts = Post.published.filter(comments__active=True).annotate(
               total_comments=Count('comments')
           ).order_by('-total_comments')[:count]
    return {'most_commented_posts': most_commented_posts}

