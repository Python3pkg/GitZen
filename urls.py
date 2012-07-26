from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('enhancement_tracking.views',
    url(r'^$', 'user_login_form_handler', name='login'),
    url(r'^logout/$', 'user_logout', name='logout'),
    url(r'^create/$', 'user_creation_form_handler', name='user_creation'),
    url(r'^confirm_user_creation/$', 'confirm_user_creation', 
        name='confirm_user_creation'),
    url(r'^confirm_git_oauth/$', 'confirm_git_oauth', name='confirm_git_oauth'),
    url(r'^home/$', 'home', name='home'),
    url(r'^change/$', 'change_form_handler', name='change_account_data'),
    url(r'^confirm_changes/$', 'confirm_changes', name='confirm_changes')
)
