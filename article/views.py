# -*- coding: utf-8 -*-
from django.http.response import Http404
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from article.forms import CommentForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.contrib import auth


def articles(request):
    return render_to_response('article/articles.html',
                              {'articles': Article.objects.all(), 'username': auth.get_user(request).username})


def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect('/articles/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect('/articles/')
            response.set_cookie(article_id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/articles/')


def article(request, article_id):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article/article.html', args)


def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)