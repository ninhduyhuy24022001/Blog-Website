from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('post/', include('post.urls'))
]

# static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)