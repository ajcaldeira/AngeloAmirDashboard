
from django.shortcuts import render

def index(request):
    posts = [
    {
        'author': 'Amir Salar',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'John Beg',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
    ]
    my_content = {
        "posts": posts
    }
    return render(request,'DashboardsProject/index.html', my_content)