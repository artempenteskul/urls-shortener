from django.db.models import Count
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Url
from .serializers import UrlSerializer, RegistrationSerializer


class RegistrationView(generics.CreateAPIView):
    """
        registers new user
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer


class UrlListView(generics.ListAPIView):
    """
        returns the list of all urls
    """
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class UrlShortener(generics.CreateAPIView):
    serializer_class = UrlSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        url = Url.objects.filter(url=request.data['url'], user=request.user).first()
        if url:
            short_url = url.short_url
            return Response(short_url)
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            url = serializer.save(user=request.user, scheme=request.scheme, hostname=request.get_host())
            short_url = url.short_url
            return Response(short_url, status=status.HTTP_201_CREATED)


class UrlRedirectView(generics.ListAPIView):
    """
        redirects to the full url through short url
    """
    def get(self, request, **kwargs):
        url = Url.objects.get(url_hash=kwargs['url_hash'])
        url = url.url
        return HttpResponseRedirect(url)


class UrlCountView(generics.ListAPIView):
    """
        counts the number of urls
    """
    def get(self, request, **kwargs):
        urls_count = Url.objects.count()
        content = {'urls_count': urls_count}
        return Response(content)


class UrlPopularView(generics.ListAPIView):
    """
        returns ten most popular shortened urls
    """
    @method_decorator(cache_page(60 * 5))
    def get(self, request, **kwargs):
        urls_popular = Url.objects.values('url').annotate(total=Count('id', distinct=True)).order_by('-total')[:10]
        content = {'urls_popular': urls_popular}
        return Response(content)
