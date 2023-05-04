"""posts views"""
# django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, FileResponse

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






@login_required
def mostrar_documento_protegido(request, path):
    """
    When trying to access :
    myproject.com/media/uploads/passport.png

    If access is authorized, the request will be redirected to
    myproject.com/protected/media/uploads/passport.png

    This special URL will be handle by nginx we the help of X-Accel
    LINK: https://b0uh.github.io/protect-django-media-files-per-user-basis-with-nginx.html
    """
    access_granted = False
    try:
        #sessionid = request.session.session_key
        user = request.user
        # Usuario admin de Django

        if user.is_authenticated:
            access_granted = True

        if access_granted:
            response = HttpResponse()
            # Content-type will be detected by nginx
            response['Content-Type'] = ''
            response['X-Accel-Redirect'] = '/protectedMedia/' + path
            return response
        else:
            return HttpResponseForbidden('Not authorized to access this media.')

    except Exception as err:
        print(err)
        return HttpResponseForbidden('Error al acceder al recurso.')
        