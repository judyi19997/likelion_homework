from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>',views.detail, name = "detail"),
    path('new',views.new, name = "new"),
    path('create',views.create, name = "create"),
    path('update/<int:select_id>',views.update, name = "update"),
    path('edit/<int:select_id>',views.edit, name = "edit"),
    path('delete/<int:select_id>',views.delete, name = 'delete'),
    path('commenting/<int:select_id>',views.commenting, name = 'commenting')
]