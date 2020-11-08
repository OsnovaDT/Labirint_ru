from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordChangeDoneView
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
    ),

    # Password change
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='accounts/password_change.html'
        ),
        name='password_change'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='accounts/'
                'password_changed.html'
        ),
        name='password_change_done'
    ),
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
