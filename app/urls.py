from django.urls import path
from app import views

urlpatterns = [
    path('estates/', views.estateList, name='estate-list'),
    path('estate/<int:pk>', views.estateFindById, name='estate-detail'),
    path('estate/', views.estateCreate, name='create-estate'),
    path('estates/<int:pk>', views.estateUpdateById, name='update'),
    path('companies/', views.companyCreate, name='create-company'),
    path('companies/', views.companyList, name='company-list'),
    path('companies/<int:pk>', views.companyFindById, name='company-detail'),
]
