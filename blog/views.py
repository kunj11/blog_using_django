from django.shortcuts import render

posts = [
    {
        'author': 'dummy1',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 15, 2019'
    },
    {
        'author': 'dummy2',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 15, 2019'
    },
    {
        'author': 'dummy3',
        'title': 'Blog post 3',
        'content': 'Third post content',
        'date_posted': 'April 15, 2019'
    },

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
