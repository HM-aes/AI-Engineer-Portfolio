from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("cv/", views.CVView.as_view(), name="cv"),
    path("projects/", views.ProjectListView.as_view(), name="projects"),
    path(
        "projects/<slug:slug>/",
        views.ProjectDetailView.as_view(),
        name="project-detail",
    ),
    path("htmx/projects/", views.HTMXProjectFilterView.as_view(), name="htmx_projects"),
    path(
        "htmx/project/<slug:slug>/metrics/",
        views.HTMXProjectMetricsView.as_view(),
        name="htmx_project_metrics",
    ),
    path(
        "security/",
        __import__(
            "portfolio.security_views"
        ).security_views.SecurityPolicyView.as_view(),
        name="security",
    ),
]
