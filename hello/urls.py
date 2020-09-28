from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>', views.greet, name='greet'),
    path('nweni/', views.nweni, name='nweni'),
    path('painglay/', views.painglay, name='painglay'),
]
