from django.urls import path, re_path

from .views import UrlListView, UrlShortener, UrlRedirectView, UrlCountView, UrlPopularView

app_name = 'shortener'

urlpatterns = [
    path('', UrlListView.as_view(), name='url-list'),
    re_path(r'^shortener/(?P<full_url>.+)$', UrlShortener.as_view(), name='short-url'),
    path('<url_hash>/', UrlRedirectView.as_view(), name='url-redirect'),
    path('urls/count/', UrlCountView.as_view(), name='url-count'),
    path('urls/popular/', UrlPopularView.as_view(), name='urls-popular'),
]
