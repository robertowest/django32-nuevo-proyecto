from django.urls import path
from django.views.generic import TemplateView

from books import views

# https://simpleisbetterthancomplex.com/tutorial/2016/11/15/how-to-implement-a-crud-using-ajax-and-json.html

# __package__.split('.')[1]    # en template: {{request.resolver_match.app_name}}
app_name = 'books'

urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('', views.book_list, name='book_list'),
    # path('create/', views.book_create, name='book_create'),
    # path('<int:pk>/update/', views.book_update, name='book_update'),
    # path('<int:pk>/delete/', views.book_delete, name='book_delete'),


    path('', views.BookTemplateView.as_view(), name='index'),
    path('listado/', views.BookListView.as_view(), name='list'),
    path('crear/', views.BookCreateView.as_view(), name='create'),
    path('<int:pk>/', views.BookReadView.as_view(), name='read'),
    path('<int:pk>/modificar/', views.BookUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.BookDeleteView.as_view(), name='delete'),
]
