from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .models import ContactMessage


class ContactView(TemplateView):
    template_name = "contact/contact.html"


class HTMXContactSubmitView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            return render(request, "htmx/contact_success.html")
        else:
            return render(request, "htmx/contact_error.html", status=400)
