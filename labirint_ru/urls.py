from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LoginView, LogoutView
)

import debug_toolbar

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Index
    path('index/', include('books.urls')),

    # Login
    path(
        'accounts/login/',
        LoginView.as_view(
            template_name='accounts/login.html'
        ),
        name='login'
    ),

    # Logout
    path(
        'accounts/logout/',
        LogoutView.as_view(),
        name='logout'
    )
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    urlpatterns.append(
        path(
            '__debug__/',
            include(debug_toolbar.urls),
        )
    )
