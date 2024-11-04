from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('interlockgo.urls')),  # Include the URLs from your InterlockGo app
]