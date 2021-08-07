
from django.contrib import admin
from django.urls import path,include
from fapp.views import home as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v),
    path('',include('fapp.urls'))
]
