from django.shortcuts import render
from .models import *
from .forms import BlogForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView, CreateView, UpdateView

# Create your views here.


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})


def detail_blog(request, blog_id):
    if request.method == 'GET':
        try:
            blog = get_object_or_404(Blog, id=blog_id)  # ok
            print(blog)
            blogform = CommentForm(request.GET, instance=blog)
            comments_blog = BlogComments.objects.filter(blog_id=blog_id)
            print(comments_blog)
            return render(request, 'blog/detail_blog.html', {'blog': blog, 'form': blogform, 'comentarios': comments_blog})
        except:
            return render(request, 'blog/detail_blog.html', {'blog': blog, 'form': blogform, 'comments': comments_blog, 'error': 'Error creando el comentario'})
    else:
        try:
            blog = get_object_or_404(Blog, id=blog_id)
            comments_blog = BlogComments.objects.filter(blog_id=blog_id)
            blogform = CommentForm(request.POST, instance=blog)
            comment = CommentForm(request.POST)
            new_comment = comment.save(commit=False)
            new_comment.user = request.user
            new_comment.blog_id = blog_id
            new_comment.save()
            return render(request, 'blog/detail_blog.html', {'blog': blog, 'form': blogform, 'comentarios': comments_blog})
        except:
            return render(request, 'blog/detail_blog.html', {'blog': blog, 'form': blogform, 'comentarios': comments_blog, 'error': 'Error actualizando el comentario'})


@login_required
def create_blog(request):
    if request.method == "GET":
        return render(request, 'blog/create_blog.html', {"form": BlogForm})
    else:
        try:
            blogform = BlogForm(request.POST)
            new_blog = blogform.save(commit=False)
            new_blog.autor = request.user
            new_blog.save()
            return redirect('blog')
        except ValueError:
            return render(request, 'blog/create_blog.html', {"form": blogform, "error": "Error al crear el blog"})


class delete_blog(DeleteView):
    model = Blog
    template_name = 'blog/delete_blog.html'
    success_url = '/'
    context_object_name = 'blog'


class update_blog(UpdateView):
    model = Blog
    template_name = 'blog/update_blog.html'
    success_url = '/'
    context_object_name = 'blog'
    fields = ['titulo', 'subtitulo', 'seccion',
              'cuerpo', 'imagen', 'referencia']
