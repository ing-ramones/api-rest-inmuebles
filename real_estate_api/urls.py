from django.urls import path
from real_estate_api import views

urlpatterns = [
    path('estates/', views.estateList, name='list'),
    #path('estates/<int:pk>', views.estateFindById, name='detail'),
    #path('estates/', views.estateCreate, name='create'),
    #path('estates/<int:pk>', views.estateUpdateById, name='update'),
]
