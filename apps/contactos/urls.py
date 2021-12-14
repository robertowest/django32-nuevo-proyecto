from django.urls import path

from . import views


app_name = __package__.split('.')[1]

urlpatterns = [
    path('', views.MyTemplateView.as_view(), name='index'),
    # path('listado/', views.MyListView.as_view(), name='list'),    # sin filtro
    path('listado/', views.MyFilterView.as_view(), name='list'),    # con filtro
    path('crear/', views.MyCreateView.as_view(), name='create'),
    path('<int:pk>/', views.MyReadView.as_view(), name='read'),
    path('<int:pk>/modificar/', views.MyUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.MyDeleteView.as_view(), name='delete'),
]
