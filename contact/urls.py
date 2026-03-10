from django.urls import path
from . import views

urlpatterns = [
    path("", views.ContactView.as_view(), name="contact"),
    path(
        "htmx/submit/",
        views.HTMXContactSubmitView.as_view(),
        name="htmx_contact_submit",
    ),
]
