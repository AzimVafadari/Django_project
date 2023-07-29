from django.shortcuts import render

posts = [
    {
        'author': 'Tesla',
        'title': 'blog post 1',
        'content': 'first post comment',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Trump',
        'title': 'blog post 2',
        'content': 'first post comment',
        'date_posted': 'August 27, 2018'
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')

# blog -> template -> blog -> template.html
