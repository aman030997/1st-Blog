from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mypoll/post_list.html', {'posts':posts})
def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request, 'mypoll/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'mypoll/post_edit.html', {'form': form})
