from django.conf.urls import include, url
from django.contrib import admin
from port import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'clash17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.home),
	url(r'^signup$', views.signup),
	url(r'^login$', views.log_in),
	url(r'^logout$', views.log_out),
	url(r'^leaderboard$', views.leaderboard),
	url(r'^submit$', views.submit),
	url(r'^questions$', views.questions),
	url(r'^qlist$', views.qlist),
	url(r'^(?P<question_id>[0-9]+)$', views.edit),
	url(r'^save/(?P<question_id>[0-9]+)$', views.save),
	url(r'^add$', views.add)
]
