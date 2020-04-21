from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('quiz/', include('QnA.urls')),
    path('admin/', admin.site.urls),
]
