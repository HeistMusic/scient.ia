from django.urls import path
from A_Inicio.views import A_Inicio


urlpatterns = [
    path('', A_Inicio.as_view(), name='A_Inicio '),
]
