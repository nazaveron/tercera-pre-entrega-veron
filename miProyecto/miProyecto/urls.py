from django.contrib import admin
from django.urls import path, include
from miProyecto.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="Inicio"),
    path('cinema/', include("cinema.urls"))

]
