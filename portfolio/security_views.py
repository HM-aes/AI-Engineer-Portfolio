from django.views.generic import TemplateView
from django.conf import settings


class SecurityPolicyView(TemplateView):
    template_name = "portfolio/security.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Mock active headers for the page based on settings
        context["headers"] = {
            "Strict-Transport-Security": f'max-age={getattr(settings, "SECURE_HSTS_SECONDS", "31536000")}; includeSubDomains; preload',
            "X-Frame-Options": getattr(settings, "X_FRAME_OPTIONS", "DENY"),
            "X-Content-Type-Options": "nosniff",
            "Referrer-Policy": "same-origin",
            "Content-Security-Policy": "default-src 'self'",
        }
        return context
