from django.urls import path

from movie_app import views

urlpatterns = [

    path('',views.home,name='home'),
    path('details/<int:id>',views.detailse,name='details'),
    path('add',views.add,name='add'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')
]
