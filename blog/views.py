from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.utils import timezone
from .forms import Postform

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts})

def post_view(request,pk):
	post=get_object_or_404(Post,pk=pk)
	return render(request,'blog/post_view.html',{'post':post})

def new_post(request):
	if request.method=="POST":
		form=Postform(request.POST)
		if form.is_valid():
			post= form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect('post_view',pk=post.pk)
	else:form=Postform()
	
	return render(request,'blog/new_post.html',{'form':form})

def edit_post(request,pk):
	post=get_object_or_404(Post,pk=pk)
	if request.method=='POST':
		form = Postform(request.POST,instance=post)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect('post_view',pk=post.pk)
	else:form=Postform(instance=post)
	return render(request,'blog/new_post.html',{'form':form})


def del_post(request,pk):
	post=get_object_or_404(Post,pk=pk)
	post.delete()
	return redirect('post_list')
