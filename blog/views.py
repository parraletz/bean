from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext


from .models import Posts, Categorias

# Create your views here.

def PostList(request):
    articulo = Posts.objects.all().order_by('agregado')
    ctx = {"articulo":articulo}
    return render_to_response('blog/home.html', ctx, context_instance=RequestContext(request))

def PostDetail(request, slug):
    articulo = get_object_or_404(Posts, slug=slug)
    ctx = {"articulo":articulo}
    return render_to_response('blog/PostDetail.html', ctx, context_instance=(RequestContext(request)))
    
