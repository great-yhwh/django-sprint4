from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.views.static import serve

from blog.views import RegistrationView

handler403 = 'pages.views.csrf_failure'
handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        '',
        include(
            'blog.urls',
            namespace='blog'
        )
    ),
    path(
        'pages/',
        include(
            'pages.urls',
            namespace='pages'
        )
    ),
    path(
        'auth/',
        include(
            'django.contrib.auth.urls',
        )
    ),
    path('auth/registration/',
         RegistrationView.as_view(),
         name='registration'
    ),
]

urlpatterns += [
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
