# coding=utf-8
from .models import Setup

__author__ = 'alexy'


def site_settings(request):
    query = Setup.objects.first()
    return {
        'SITE_SETTINGS': query,
    }
