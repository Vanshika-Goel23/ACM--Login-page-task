


from django.contrib import admin
from django.urls import path
from users import views as users_views
from django.contrib.auth import views as auth_views


urlpatterns = [
        path('admin/', admin.site.urls),
        path('signup/',users_views.register, name="Sign-up"),
        path('login/',auth_views.LoginView.as_view(template_name='users/Login.html'),name="Login"),
        path('home/',users_views.home,name='home_page'),
        path('signout/',auth_views.LogoutView.as_view(template_name='users/Logout.html'), name="Sign-out"),
]