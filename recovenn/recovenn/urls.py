"""
main url configuration file for the askbot site
"""
from django.conf import settings
from django.views.generic import RedirectView
try:
    from django.conf.urls import handler404
    from django.conf.urls import include, url
except ImportError:
    from django.conf.urls.defaults import handler404
    from django.conf.urls.defaults import include, url

import askbot.urls
from askbot import is_multilingual
from askbot.views.error import internal_error as handler500
from django.conf import settings
from django.contrib import admin
from django.views import static as StaticViews
from django.shortcuts import redirect
import followit.urls
import tinymce.urls

admin.autodiscover()

if is_multilingual():
    from django.conf.urls.i18n import i18n_patterns
    urlpatterns = i18n_patterns(
        url(r'%s' % settings.ASKBOT_URL, include(askbot.urls))
    )
else:
    urlpatterns = [
        url(r'%s' % settings.ASKBOT_URL, include(askbot.urls))
    ]

urlpatterns += [
    url(r'^admin/', admin.site.urls),
    #(r'^settings/', include(askbot.deps.livesettings.urls)),
    url(r'^followit/', include(followit.urls)),
    url(r'^tinymce/', include(tinymce.urls)),
    url(r'^robots.txt$', include('robots.urls')),
    url( # TODO: replace with django.conf.urls.static ?
        r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
        StaticViews.serve,
        {'document_root': settings.MEDIA_ROOT.replace('\\','/')},
    ),
    url(r'account/signup/None', RedirectView.as_view(url='/')),
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
                    url(r'^rosetta/', include('rosetta.urls')),
                ]

handler500 = 'askbot.views.error.internal_error'