from django.http import Http404
from django.shortcuts import render_to_response, render
from django.template.context_processors import csrf

from .models import Forum, Thread, Post
from .forms import PostForm


# Create your views here.

def forums(request):
    all_forums = Forum.objects.filter(parent=None)

    return render_to_response('index.html', {'forums': all_forums})

def forum(request, forum_slug):
    forum = Forum.objects.get(slug=forum_slug)
    parent_of = Forum.objects.filter(parent=forum)
    threads = Thread.objects.filter(forum=forum)

    return render_to_response('index.html', {'forums': parent_of, 'threads': threads, 'forum': forum})

def thread(request, thread_slug):
    thread = Thread.objects.get(slug=thread_slug)
    posts = Post.objects.filter(thread=thread)

    return render_to_response('thread.html', {'thread': thread, 'posts': posts,})

def new_post(request, thread_slug):
    c = {}
    thread = Thread.objects.get(slug=thread_slug)
    if request.method == 'POST':
        q = request.POST.dict()
        user = request.user

        post = Post(written_by=user, thread=thread, content=q['content'])
        post.save()

        c['thread'] = thread
        c['post'] = post
    else:              
        c['thread'] = thread
        c['show_form'] = True
        c.update(csrf(request)) # add CSRF token to dict


    return render_to_response('newpost.html', c)