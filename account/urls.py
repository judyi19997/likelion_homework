from django.urls import path, include
from . import views

urlpatterns = [
    path('login_page',views.make_login, name = "login"),
    path('logout_page',views.make_logout, name = "logout"), 
    path('signup_page',views.make_register, name = "signup")   
] 
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #media url