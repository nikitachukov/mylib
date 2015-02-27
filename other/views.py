from django.shortcuts import render
import platform
from django.contrib.auth.decorators import login_required
from pyicloud import PyiCloudService
from django.shortcuts import render_to_response
import django
import logging


@login_required
def osinfo(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    logger = logging.getLogger(__name__)
    logger.debug(ip)

    return render_to_response("osinfo.html", {'osinfo': {
        'nodename': platform.node(),
        'version': platform.python_implementation() + platform.python_version(),
        'arch': platform.system() + ' ' + platform.version() + ' ' + platform.architecture()[0],
        'processor': platform.processor(),
        'django': 'Django ' + django.get_version(),
        'clientip': str(ip)}})


@login_required
def iphone_location(request):
    from django.conf import settings


    api = PyiCloudService(settings.ICLOUD_USER, settings.ICLOUD_PASSWORD)
    for index, item in enumerate(api.devices):
        if item.status()['name'] == 'Iphone_nikitos':
            location = item.location()

            return render_to_response("map.html",
                                      {'location':
                                           {'latitude': str(location['latitude']),
                                            'longitude': str(location['longitude']),
                                            'horizontalAccuracy': str(location['horizontalAccuracy'])

                                           }})

# Create your views here.
