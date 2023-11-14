from django.shortcuts import render
from datetime import date

posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountains.jpg',
        'author': 'Shashank',
        'date': date(2023, 11, 3),
        'title': 'Mountain Hiking',
        'excerpt': """There\'s nothing like then views when 
                    hiking in the mountains! 
                    And I wasn\'t even prepared for 
                    what happened whilst I was enjoying the view!""",
        'content': """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Quisquam, unde corporis ducimus odio quas ipsa? Dicta recusandae iure, 
                    corporis atque ea harum ratione animi ullam.
                    Culpa dolores cumque eveniet totam?

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Quisquam, unde corporis ducimus odio quas ipsa? Dicta recusandae iure, 
                    corporis atque ea harum ratione animi ullam.
                    Culpa dolores cumque eveniet totam?

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Quisquam, unde corporis ducimus odio quas ipsa? Dicta recusandae iure, 
                    corporis atque ea harum ratione animi ullam.
                    Culpa dolores cumque eveniet totam?
                    """,
    },
    {
        'slug': 'programming-guy',
        'image': 'coding.jpg',
        'author': 'Shashank',
        'date': date(2023, 11, 3),
        'title': 'Programming',
        'excerpt': """There\'s nothing like then views when 
                    hiking in the mountains! 
                    And I wasn\'t even prepared for 
                    what happened whilst I was enjoying the view!""",
        'content': """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Quisquam, unde corporis ducimus odio quas ipsa? Dicta recusandae iure, 
                    corporis atque ea harum ratione animi ullam.
                    Culpa dolores cumque eveniet totam?

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Quisquam, unde corporis ducimus odio quas ipsa? Dicta recusandae iure, 
                    corporis atque ea harum ratione animi ullam.
                    Culpa dolores cumque eveniet totam?

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Quisquam, unde corporis ducimus odio quas ipsa? Dicta recusandae iure, 
                    corporis atque ea harum ratione animi ullam.
                    Culpa dolores cumque eveniet totam?
                    """,
    },
    {
        'slug': 'wood-exploring',
        'image': 'woods.jpg',
        'author': 'Shashank',
        'date': date(2023, 11, 3),
        'title': 'Woods Exploring',
        'excerpt': """There\'s nothing like then views when 
                    hiking in the mountains! 
                    And I wasn\'t even prepared for 
                    what happened whilst I was enjoying the view!""",
        'content': """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Quisquam, unde corporis ducimus odio quas ipsa? Dicta recusandae iure, 
                    corporis atque ea harum ratione animi ullam.
                    Culpa dolores cumque eveniet totam?

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Quisquam, unde corporis ducimus odio quas ipsa? Dicta recusandae iure, 
                    corporis atque ea harum ratione animi ullam.
                    Culpa dolores cumque eveniet totam?

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Quisquam, unde corporis ducimus odio quas ipsa? Dicta recusandae iure, 
                    corporis atque ea harum ratione animi ullam.
                    Culpa dolores cumque eveniet totam?
                    """,
    }
]

def get_date(post):
    return post['date']

def index(request):
    sorted_posts = sorted(posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', 
                  context={
                      'posts': latest_posts,
                  })

def all_posts(request):
    return render(request, 'blog/all-posts.html', 
                  context={
                      'all_posts': posts,
                  })

def post_detail(request, slug):
    identified_post = next(post for post in posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html',
                  context={
                      'post': identified_post,
                  })