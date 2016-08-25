#! -*- coding:utf-8 -*-


from django.conf.urls import patterns, include, url
from django.contrib import admin
from rango import views
from django.conf import settings

# UNDERNEATH your urlpatterns definition, add the following two lines:


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^about/', include('rango.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )


'''
from django.conf import settings  # New Import
from django.conf.urls.static import static  # New Import

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, documet_root=settings.STATIC_ROOT)
DEBUG变量在settings.py中,设置它可以让我们控制是否输出错误信息.当把DEBUG设置成True时对于
应用的部署并不安全.当你把DEBUG设置成False,你得需要把settings.py中的ALLOWED_HOSTS变量设置
成127.0.0.1以便可以在本地主机上运行.你需要修改项目里的urls.py文件:
'''
