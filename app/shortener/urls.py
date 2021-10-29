from django.urls import path, re_path

from .views import UrlListView, UrlShortener, UrlRedirectView, UrlCountView, UrlPopularView

app_name = 'shortener'

urlpatterns = [
    path('', UrlListView.as_view(), name='url-list'),
    path('shortener/', UrlShortener.as_view(), name='shortener'),
    path('<url_hash>/', UrlRedirectView.as_view(), name='url-redirect'),
    path('urls/count/', UrlCountView.as_view(), name='urls-count'),
    path('urls/popular/', UrlPopularView.as_view(), name='urls-popular'),
]
