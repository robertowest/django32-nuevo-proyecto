from django.urls import path

from . import views

app_name = 'persona'

urlpatterns = [
    path('', views.PersonaList.as_view(), name='list'),
    path('ver/<int:pk>', views.PersonaDetail.as_view(), name='view'),
    path('nuevo', views.PersonaCreate.as_view(), name='new'),
    path('editar/<int:pk>', views.PersonaUpdate.as_view(), name='edit'),
    path('eliminar/<int:pk>', views.PersonaDelete.as_view(), name='delete'),
]
