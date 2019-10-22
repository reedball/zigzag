from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^jobs$', views.register),
    url(r'^loginprocess$', views.loginprocess),
    url(r'^logout$', views.logout),
    url(r'^jobs/new$', views.new_job),
    url(r'^addjob$', views.addjob),
    url(r'^edit/(?P<job_id>\d+)$', views.edit),
    url(r'^remove/(?P<job_id>\d+)$', views.delete),
    url(r'^update/(?P<job_id>\d+)$',views.update),
    url(r'^jobs/(?P<job_id>\d+)$',views.view),
    url(r'^add/(?P<job_id>\d+)$',views.add),
    url(r'^giveup/(?P<job_id>\d+)$',views.giveup)
]


