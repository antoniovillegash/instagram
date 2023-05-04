"""instagram URLs module """
#django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path


from instagram.views import views as local_views
from posts import views as posts_views
from users import views as users_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/',local_views.hello_world, name='hello_world'),
    path('sorted/',local_views.sort_integers, name='sort'),
    path('hi/<str:name>/<int:age>',local_views.say_hi, name='hi'),

    path('',posts_views.list_posts, name='feed'),
    path('posts/new/',posts_views.create_post, name="create_post"),

    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup_view, name='signup'),
    path('users/me/profile/', users_views.update_profile, name='update_profile' ),
    re_path(r'^media/(?P<path>.*)', posts_views.mostrar_documento_protegido, name='serve_protected_document'),
    
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
