"""
ASGI config for covid_19_find_chinese_roommate_website project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'covid_19_find_chinese_roommate_website.settings')

application = get_asgi_application()
