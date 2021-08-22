from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from rest_framework.authtoken.views import obtain_auth_token

handler404 = 'home_page.views.error_404'
# handler404 = 'home_page.views.error_404'
urlpatterns = [
    path('', views.home, name='Home'),
    path('api/post/data/<int:post_id>', views.post_data, name='Post'),
    path('post/post-id=<int:post_id>', views.one_post_view, name='Post'),
    path('api/post/do_comment', views.post_comment_saver, name='Do comment'),
    path('404', views.error_404, name='Post'),
    path('post/delete/<int:post_id>', views.post_delete_view, name='Delete'),
    path('api/post/action', views.post_action, name='action'),
    path('api/post_comment/action', views.post_comment_likes, name='comment action'),
    path('api/post_detial_view/', views.post_detial_view, name='Post'),
    path('api/post_upload', views.PostCreateView, name='Post Upload'),
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]



