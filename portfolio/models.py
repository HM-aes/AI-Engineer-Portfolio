from django.db import models


class TechTag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    DOMAIN_CHOICES = [
        ("construction", "Construction"),
        ("hospitality", "Hospitality"),
        ("legal", "Legal"),
        ("tech", "Technology"),
        ("youth", "Youth Protection"),
        ("other", "Other"),
    ]
    SECURITY_LEVELS = [
        ("CRITICAL", "CRITICAL"),
        ("HIGH", "HIGH"),
        ("MEDIUM", "MEDIUM"),
        ("LOW", "LOW"),
    ]

    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    tagline = models.CharField(max_length=200)
    description = models.TextField()
    security_level = models.CharField(choices=SECURITY_LEVELS, max_length=20)
    stack = models.ManyToManyField(TechTag)
    domain = models.CharField(choices=DOMAIN_CHOICES, max_length=50)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return self.name


class SecurityModel(models.Model):
    project = models.OneToOneField(
        Project, on_delete=models.CASCADE, related_name="security_model"
    )
    threat_model = models.TextField()
    data_flow = models.TextField()
    access_control = models.TextField()
    compliance_refs = models.JSONField(default=list)  # e.g., ['NIS2', 'GDPR']
    owasp_mitigations = models.JSONField(default=list)

    def __str__(self):
        return f"{self.project.name} - Security Model"
