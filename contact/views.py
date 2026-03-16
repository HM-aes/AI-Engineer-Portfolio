from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
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
            
            send_mail(
                subject=f"Portfolio contact: {name}",
                message=f"{name}\n{email}\n\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=True,
            )
            
            return render(request, "htmx/contact_success.html")
        else:
            return render(request, "htmx/contact_error.html", status=400)
