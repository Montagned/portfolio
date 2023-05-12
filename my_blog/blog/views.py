from datetime import date

from django.shortcuts import render

all_posts = [
    {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author":"Davide",
    "date": date(2021, 7, 21),
    "title": "Hiking!",
    "excerpt": "Go hiking in the mountains is the best way to resource my mind and find new inspiration.",
    "content": """
            When the sun is shining I can do anything; 
            no mountain is too high, no trouble too difficult to overcome.

            Wilma Rudolph
            """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Davide",
        "date": date(2022, 3, 10),
        "title": "My passion for Programming!",
        "excerpt": "Coding is a great way to challenge your mind and in the meanwhile be creative!",
        "content": """
          The more highly adapted an organism becomes, 
          the less adaptable it is to any new change.

          Ronald Fischer
        """
    },
    {
        "slug": "music-management",
        "image": "orchestra.jpg",
        "author": "Davide",
        "date": date(2023, 8, 5),
        "title": "Make music happen!",
        "excerpt": "Organizing events and help others realizing their dreams is really fulfilling!",
        "content": """
          Management is about persuading people to do things they do not want to do, 
          while leadership is about inspiring people to do things 
          they never thought they could.

          Steve Jobs
        """
    },
    {
    "slug": "playing-great-music",
    "image": "music.jpg",
    "author":"Davide",
    "date": date(2021, 7, 21),
    "title": "Playing great music",
    "excerpt": "Playing in an orchestra is like being part of a masterpiece. It'a hard work but it can be great fun too!",
    "content": """
            Music means different things to different people and sometimes 
            even different things to the same person at different moments of his life.

            Daniel Baremboim
    """
    }
]

def get_date(post):
    # return post.get('date') # other possibility of extracting data from dictionary
    return post['date']

# def get_post(slug):
#     for post in all_posts:
#         if post["slug"] == slug:
#             return post
    
# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_post = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_post
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

# def post_detail(request, slug):
#     actual_post = get_post(slug)
#     return render(request, "blog/post-detail.html",{
#        "post": actual_post
#     })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
