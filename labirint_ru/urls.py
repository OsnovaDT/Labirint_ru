from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordChangeDoneView, PasswordResetView,
    PasswordResetDoneView, PasswordResetCompleteView,
    PasswordResetConfirmView
)

from books.views import SignUpView

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

    # Sign up
    path(
        'sign_up',
        SignUpView.as_view(),
        name='sign_up'
    ),

    # Password reset
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='accounts/reset_password/'
                'reset_password.html',
            subject_template_name='accounts/reset_password/'
                'email_subject.txt',
            email_template_name='accounts/reset_password/'
                'email_message.html'
        ),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='accounts/reset_password/'
            'email_sent.html',
        ),
        name='password_reset_done'
    ),
    path(
        'password_reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='accounts/reset_password/'
            'reset_password_confirm.html',
        ),
        name='password_reset_confirm'
    ),
    path(
        'password_reset_complete/',
        PasswordResetCompleteView.as_view(
            template_name='accounts/reset_password/'
            'reset_password_complete.html',
        ),
        name='password_reset_complete'
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
