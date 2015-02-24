from django.shortcuts import render
import platform
from django.contrib.auth.decorators import login_required
from pyicloud import PyiCloudService
from django.shortcuts import render_to_response
import django

@login_required
def osinfo(request):
    return render_to_response("library/osinfo.html", {'osinfo': {
        'nodename': platform.node(),
        'version': platform.python_implementation() + platform.python_version(),
        'arch': platform.system() + ' ' + platform.version() + ' ' + platform.architecture()[0],
        'processor': platform.processor(),
        'django': 'Django ' + django.get_version()}})

@login_required
def iphone_location(request):
    from django.conf import settings

    print(settings.ICLOUD_USER)
    print(settings.ICLOUD_PASSWORD)



    api = PyiCloudService(settings.ICLOUD_USER, settings.ICLOUD_PASSWORD)
    for index, item in enumerate(api.devices):
        if item.status()['name'] == 'Iphone_nikitos':
            location = item.location()


            return render_to_response("library/map.html",
                                      {'location':
                                           {'latitude': str(location['latitude']),
                                            'longitude': str(location['longitude']),
                                            'horizontalAccuracy': str(location['horizontalAccuracy'])

                                           }})

# Create your views here.
