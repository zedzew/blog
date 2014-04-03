from django.conf.urls import patterns, include, url




urlpatterns = patterns('article.views',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


##    url(r'^1/', 'article.views.basic_one'),
##    url(r'^2/', 'article.views.template_two'),
##    url(r'^3/', 'article.views.template_three_simple'),
    url(r'^articles/all/$', 'articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$', 'article'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'addcomment'),
    url(r'^articles/addlike/(?P<article_id>\d+)/$', 'addlike'),
    url(r'^page/(\d+)/$', 'articles'),
    url(r'^$', 'articles', name='127.0.0.1:8000'),


)
