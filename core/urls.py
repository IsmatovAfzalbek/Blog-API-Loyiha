from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('app_accounts.urls')),
    path('api/posts/', include('app_posts.urls')),
    path('api/comments/', include('app_comments.urls')),
    path('api/likes/', include('app_likes.urls')),
    path('api/categories/', include('app_categories.urls')),
]

urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
