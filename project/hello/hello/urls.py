from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Welcome to the Jobportal Admin"
admin.site.site_title = "Jobportal-A hub for jobs"
admin.site.index_title = "Welcome to the Jobportals"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
