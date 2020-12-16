from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def home(request):
    post = Post.objects.all()

    data = {
        'posts': post
    }

    return render(request, template_name='blogs/home.html', context=data)





def createpost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-url')

    data = {
        'form': form
    }
    return render(request, template_name='blogs/createpost.html', context=data)
