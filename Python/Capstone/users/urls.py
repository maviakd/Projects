from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView

urlpatterns = [

	#path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
	path('profile/', user_views.profile, name='profile'),
	path('register/', user_views.register, name='register'),
	path('', PostListView.as_view(), name='user_list'),
	path('<int:pk>/', PostDetailView.as_view(), name='user_detail'),
	path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
	path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
	path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
