from django.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
    path('index/', views.index,name='index'),
    path('create/', views.create,name='create'),
    path('update/', views.update,name='update'),
    path('delete/', views.delete,name='delete'),
    path('getdate/',views.get_date,name='get_date'),

]
url = urlpatterns
