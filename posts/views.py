"""posts views"""
# django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#forms
from posts.forms import PostForm

#models
from posts.models import Post

# posts = [
#     {
#         'name': 'hola',
#         'user': 'Erika muñoz',
#         'timestamp': datetime.now().strftime('%b/%dth, %Y - %H:%M hrs'),
#         'photo': 'https://www.laughtard.com/wp-content/uploads/2019/02/50-Funny-Animal-Pictures-That-You-Need-In-Your-Life-37.jpg',
#         'picture': 'https://picsum.photos/200/200/?image=1036',
#     },
#     {
#         'name': 'hola',
#         'user': 'Tony Villegas',
#         'timestamp': datetime.now().strftime('%b/%dth, %Y - %H:%M hrs'),
#         'photo': 'https://www.laughtard.com/wp-content/uploads/2019/02/50-Funny-Animal-Pictures-That-You-Need-In-Your-Life-37.jpg',
#         'picture': 'https://picsum.photos/200/200/?image=903',
#     }
# ]

@login_required
def list_posts(request):
    """listing existing posts"""
    profile = request.user.profile
    posts = Post.objects.all().order_by('-created')

    return render(
        request = request,
        template_name='posts/feed.html',
        context={
            'profile':profile,
            'posts':posts,
            'user':request.user,
        }
    )

@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )

