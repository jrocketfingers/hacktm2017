from django.shortcuts import render
from django.views.generic import ListView

from core.models import Action


class ActionFeed(ListView):
    """Actively list all available actions."""
    model = Action
    template_name = "feed.html"

    # TODO: consider filtering
