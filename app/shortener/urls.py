from django.urls import path

from .views import UrlListView, UrlShortener, UrlRedirectView, UrlCountView, UrlPopularView, RegistrationView

app_name = 'shortener'

urlpatterns = [
    path('', UrlListView.as_view(), name='url-list'),
    path('shortener/', UrlShortener.as_view(), name='shortener'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('<url_hash>/', UrlRedirectView.as_view(), name='url-redirect'),
    path('urls/count/', UrlCountView.as_view(), name='urls-count'),
    path('urls/popular/', UrlPopularView.as_view(), name='urls-popular'),
]
