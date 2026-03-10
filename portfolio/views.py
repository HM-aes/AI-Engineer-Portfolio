from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import Project


class HomeView(ListView):
    template_name = "portfolio/home.html"
    model = Project
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(is_featured=True)[:6]


class AboutView(TemplateView):
    template_name = "portfolio/about.html"


class CVView(TemplateView):
    template_name = "portfolio/cv.html"


class ProjectListView(ListView):
    template_name = "portfolio/projects.html"
    model = Project
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    template_name = "portfolio/project_detail.html"
    model = Project
    context_object_name = "project"


class HTMXProjectFilterView(View):
    def get(self, request, *args, **kwargs):
        tag = request.GET.get("tag", "all").lower()
        if tag == "all":
            projects = Project.objects.all()
        elif tag == "tech":  # RAG_ARCH — technology/RAG pipeline projects
            projects = Project.objects.filter(domain="tech")
        elif tag == "compliance":  # COMPLIANCE — regulatory-driven projects (NIS2, GDPR)
            projects = Project.objects.filter(security_level__in=["CRITICAL", "HIGH"])
        elif tag == "other":  # SECURITY_ONLY — hardened, critical-security projects
            projects = Project.objects.filter(security_level="CRITICAL")
        else:
            projects = Project.objects.filter(domain=tag)

        return render(request, "htmx/project_grid_partial.html", {"projects": projects})


class HTMXProjectMetricsView(View):
    def get(self, request, slug, *args, **kwargs):
        project = get_object_or_404(Project, slug=slug)
        return render(
            request, "htmx/project_metrics_partial.html", {"project": project}
        )
