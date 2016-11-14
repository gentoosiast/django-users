from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from qa import views

urlpatterns = patterns('',
    url(r'^$', views.question_list, {'sort': 'newest'}),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^question/(?P<qid>[0-9]+)/$', views.question_details, name='question-details'),
    url(r'^ask/', views.askform, name='ask-question'),
    url(r'^answer/', views.post_answer, name='post-answer'),
    url(r'^popular/$', views.question_list, {'sort': 'popular'}),
    url(r'^new/$', views.test),
)
