from note import views
from django.urls import path

urlpatterns=[
    path("post",views.PostView.as_view(),name="note-post"),
    path("post/list",views.PostListView.as_view(),name="note-list"),
    path("post/update/<str:emp_id>",views.PostEditView.as_view(),name="note-edit"),
    path("post/remove/<str:emp_id>",views.removeview,name="note-remove")
]
