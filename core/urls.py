from django.views.generic import TemplateView
from django.conf.urls import url

from core.views import ActionFeed

app_name = 'core'
urlpatterns = [
    url(r'^$', ActionFeed.as_view(template_name='feed.html')),
]
