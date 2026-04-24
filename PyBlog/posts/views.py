from  django.shortcuts import render
from django.http import  HttpResponseNotFound
from  .models import Post , Comment

def post_list(request):
    posts =Post.objects.all()
    context={'posts':posts}
    return render(request,'posts/post_list.html',context=context)

def post_detail(request,post_id):
    try:
        post =Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return HttpResponseNotFound("Post is not exist")
    comments= Comment.objects.filter(post=post)
    context={'post':post ,'comments': comments}
    return render(request,'posts/post_detail.html',context=context)
