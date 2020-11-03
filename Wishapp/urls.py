from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login_Reg),
    path('register', views.Register),
    path('login', views.Login),
    path('success', views.Success),
    path('logout', views.Logout),
    path('wishes', views.wishes),
    path('new', views.new),
    path('edit/<int:id>', views.edit),
    path('stats', views.stats),
    path('new_wish', views.new_wish),
    path('grant', views.grant),
    path('update/<int:id>', views.update),
    path('delete', views.delete),
    path('like', views.like)
]