from django.conf.urls import patterns, url
from .views import (profile_detail, profile_followings, profile_followers,
                    profile_follow, user_arguments, user_contributed_arguments)


urlpatterns = patterns(
    '',
    url(r'^(?P<username>[A-Za-z0-9-_]+)/$',
        profile_detail,
        name='api-profile-detail'),
    url(r'^(?P<username>[A-Za-z0-9-_]+)/follow/$',
        profile_follow,
        name='api-profile-follow'),
    url(r'^(?P<username>[A-Za-z0-9-_]+)/followers/$',
        profile_followers,
        name='api-profile-followers'),
    url(r'^(?P<username>[A-Za-z0-9-_]+)/followings/$',
        profile_followings,
        name='api-profile-followings'),
    url(r'^(?P<username>[A-Za-z0-9-_]+)/arguments/owner/$',
        user_arguments,
        name='api-user-arguments'),
    url(r'^(?P<username>[A-Za-z0-9-_]+)/arguments/contributed/$',
        user_contributed_arguments,
        name='api-user-arguments-contributed'),
)
