from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    # path('api/', include('todo.urls')), 
    path('api/todo', include(router.urls)),
    # path('api/todo/', include('todo.urls')),  # Use the correct URL pattern


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
