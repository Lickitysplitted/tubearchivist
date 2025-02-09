"""all api urls"""

from api.views import (
    ChannelApiListView,
    ChannelApiView,
    DownloadApiListView,
    DownloadApiView,
    LoginApiView,
    PlaylistApiView,
    VideoApiView,
    VideoProgressView,
)
from django.urls import path

urlpatterns = [
    path("login/", LoginApiView.as_view(), name="api-login"),
    path(
        "video/<slug:video_id>/",
        VideoApiView.as_view(),
        name="api-video",
    ),
    path(
        "video/<slug:video_id>/progress/",
        VideoProgressView.as_view(),
        name="api-video-progress",
    ),
    path(
        "channel/",
        ChannelApiListView.as_view(),
        name="api-channel-list",
    ),
    path(
        "channel/<slug:channel_id>/",
        ChannelApiView.as_view(),
        name="api-channel",
    ),
    path(
        "playlist/<slug:playlist_id>/",
        PlaylistApiView.as_view(),
        name="api-playlist",
    ),
    path(
        "download/",
        DownloadApiListView.as_view(),
        name="api-download-list",
    ),
    path(
        "download/<slug:video_id>/",
        DownloadApiView.as_view(),
        name="api-download",
    ),
]
