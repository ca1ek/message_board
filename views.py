from django.http import Http404
from django.shortcuts import render_to_response, render
from django.template.context_processors import csrf
from django.views.generic.base import TemplateView
from django.core.exceptions import ObjectDoesNotExist

from .models import *
from .forms import PostForm


# Create your views here.

def forums(request):
    all_forums = Forum.objects.filter(parent=None)

    return render_to_response('index.html', {'forums': all_forums})

def forum(request, forum_slug):
    forum = Forum.objects.get(slug=forum_slug)
    parent_of = Forum.objects.filter(parent=forum)
    threads = Thread.objects.filter(forum=forum)
    can_make_forums = request.user.has_perm('message_board.add_forum')
    can_make_threads = request.user.has_perm('message_board.add_thread')

    c = {'forums': parent_of, 'threads': threads, 'forum': forum, 'can_forum': can_make_forums, 'can_thread': can_make_threads}

    return render_to_response('index.html', c)

def thread(request, thread_slug):
    thread = Thread.objects.get(slug=thread_slug)
    posts = Post.objects.filter(thread=thread)
    user = request.user
    can_make_posts = request.user.has_perm('message_board.add_post')

    c = {'thread': thread, 'posts': posts, 'user': user, 'can_post': can_make_posts}

    return render_to_response('thread.html', c)

def new_post(request, thread_slug, post_id=None):
    c = {}
    thread = Thread.objects.get(slug=thread_slug)
                            
    if request.method == 'POST':
        user = request.user
        form = PostForm(request.POST)
        try:
            reply_to = Post.objects.get(id=post_id)
        except ObjectDoesNotExist:
            reply_to = None

        if form.is_valid():
            data = form.cleaned_data
            post = Post(written_by=user, thread=thread, content=data['content'], reply_to=reply_to)
            post.save()       

        c['thread'] = thread
        c['post'] = post
    else:         
        c['thread'] = thread
        c['show_form'] = True
        c.update(csrf(request))  # add CSRF token to dict

    return render_to_response('newpost.html', c)
