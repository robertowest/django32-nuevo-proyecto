from django.urls import path
from . import views

app_name = __package__.split('.')[1]    # en template: request.resolver_match.app_name

urlpatterns = [
    path('', views.DiccionarioTemplateView.as_view(), name='index'),
    path('listado/', views.DiccionarioListView.as_view(), name='list'),
    path('crear/', views.DiccionarioCreateView.as_view(), name='create'),
    path('<int:pk>/', views.DiccionarioReadView.as_view(), name='read'),
    path('<int:pk>/modificar/', views.DiccionarioUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.DiccionarioDeleteView.as_view(), name='delete'),
]
