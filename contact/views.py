from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from urllib.parse import quote
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
            
            subject = f"Portfolio Inquiry from {name}"
            body = f"Hi Hassan,\n\n{message}\n\n---\nFrom: {name}\nEmail: {email}"
            mailto_link = f"mailto:iaesdev@pm.me?subject={quote(subject)}&body={quote(body)}"
            
            return render(request, "htmx/contact_success.html", {"mailto_link": mailto_link})
        else:
            return render(request, "htmx/contact_error.html", status=400)
