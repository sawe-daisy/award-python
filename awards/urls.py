from . import views
from django.urls import path, re_path , include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router= routers.DefaultRouter()

urlpatterns=[
    path('', views.index, name='gram-landing'),
    path(r'ratings/', include('star_ratings.urls', namespace='ratings')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/',views.register, name='registration'),
    path('search/', views.searchprofile, name='search'),
    path('post/', views.PostCreateView, name='post-create'),
    path('profile/',views.profile, name='profile'),
    path('like/<int:pk>/', views.like_image, name='like_post'),
    path('api/projects',views.ProjectList.as_view()),
    path('api/profiles',views.ProfileList.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)