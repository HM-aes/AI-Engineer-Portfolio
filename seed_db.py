import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

from portfolio.models import Project, SecurityModel, TechTag
from django.utils.text import slugify

# Define Tags
tags = [
    "Django 6.0",
    "Pydantic AI",
    "Qdrant",
    "Ollama",
    "PostgreSQL",
    "Railway",
    "PyMuPDF",
    "Docling",
    "HTMX",
    "TailwindCSS",
    "Sentence Transformers",
]

tag_objs = {}
for t in tags:
    tag_objs[t], _ = TechTag.objects.get_or_create(name=t)

# Define Projects
projects_data = [
    {
        "name": "SMB-Shield · Nia",
        "tagline": "NIS2 & Cybersecurity Compliance Platform — 5-Agent Pydantic AI System",
        "description": "5-agent architecture: SecurityGatekeeper, Librarian, Auditor, IntelligenceAnalyst, ReportManager. Multi-framework RAG knowledge base: NIS2, GDPR, ISO 27001, SOC2 in a single Qdrant index. Dual deployment: cloud SaaS + offline Mac Mini appliance for air-gapped clients.",
        "security_level": "CRITICAL",
        "domain": "tech",
        "stack": [
            "Django 6.0",
            "Pydantic AI",
            "Qdrant",
            "Ollama",
            "PostgreSQL",
            "Railway",
        ],
        "order": 1,
        "is_featured": True,
        "security_model": {
            "threat_model": "RAG poisoning via malicious document injection. Prompt injection via user queries. Data exfiltration via LLM responses.",
            "data_flow": "Dual deployment structure. Validated ingestion pipeline to Qdrant. Output filtering + PII scrubbing pipeline.",
            "access_control": "Role-based access control — agent-level permission scoping. Full audit trail.",
            "compliance_refs": ["NIS2", "GDPR", "ISO 27001", "SOC2"],
            "owasp_mitigations": [
                "LLM01: Prompt Injection",
                "LLM03: Training Data Poisoning",
                "LLM06: Sensitive Information Disclosure",
            ],
        },
    },
    {
        "name": "ComplianceRadar",
        "tagline": "Multi-Framework Compliance Document Intelligence",
        "description": "GDPR, NIS2, ISO 27001, SOC2 in a single RAG KB. Embedded Qdrant mode for zero network dependency. Pydantic AI agents for structured validation. Mac Monterey native setup for full data sovereignty.",
        "security_level": "CRITICAL",
        "domain": "tech",
        "stack": [
            "Django 6.0",
            "Qdrant",
            "Ollama",
            "Pydantic AI",
            "PyMuPDF",
            "Docling",
        ],
        "order": 2,
        "is_featured": True,
        "security_model": {
            "threat_model": "Data exfiltration over public networks.",
            "data_flow": "Local embedded Qdrant mode on Mac Monterey. No external API calls for generation/embedding during runtime.",
            "access_control": "Local user access.",
            "compliance_refs": ["GDPR", "NIS2", "ISO 27001", "SOC2"],
            "owasp_mitigations": ["LLM06: Sensitive Information Disclosure"],
        },
    },
    {
        "name": "BouwBewijs Pro",
        "tagline": "WKb Compliance Platform for Dutch Construction SMBs",
        "description": "WKb compliance document management. Offline-first architecture for construction sites. RAG over Dutch building regulations and WKb dossier requirements.",
        "security_level": "HIGH",
        "domain": "construction",
        "stack": [
            "Django 6.0",
            "Ollama",
            "Qdrant",
            "PostgreSQL",
            "HTMX",
            "TailwindCSS",
        ],
        "order": 3,
        "is_featured": True,
        "security_model": {
            "threat_model": "Data interception of sensitive Dutch construction documents.",
            "data_flow": "No Dutch construction data leaves the client's infrastructure. Offline-first capabilities.",
            "access_control": "On-premises system authentication.",
            "compliance_refs": ["WKb", "GDPR", "Dutch Building Regulations"],
            "owasp_mitigations": ["LLM06: Sensitive Information Disclosure"],
        },
    },
    {
        "name": "MijnDossier",
        "tagline": "Youth Protection Document Retrieval",
        "description": "Retrieval-only system: surfaces exact source documents, never synthesizes new text. Zero generative AI to avoid hallucination risks in child protection.",
        "security_level": "CRITICAL",
        "domain": "youth",
        "stack": [
            "Django 6.0",
            "Docling",
            "Sentence Transformers",
            "PostgreSQL",
            "HTMX",
        ],
        "order": 4,
        "is_featured": True,
        "security_model": {
            "threat_model": "LLM Hallucinations leading to false information in youth protection cases.",
            "data_flow": "Sentence Transformers local embedding. Zero external API calls. Retrieval-only generation block.",
            "access_control": "Every document retrieval timestamped and attributed to a case worker in PostgreSQL.",
            "compliance_refs": ["GDPR", "AVG", "Dutch Jeugdwet"],
            "owasp_mitigations": ["LLM09: Overreliance"],
        },
    },
    {
        "name": "HostelHub",
        "tagline": "AI Document Management RAG System for Hostels",
        "description": "AI-powered document processing for house rules, safety procedures, and check-in flows. Multi-property support with property-specific RAG indexing.",
        "security_level": "MEDIUM",
        "domain": "hospitality",
        "stack": ["Django 6.0", "Pydantic AI", "Qdrant", "HTMX", "TailwindCSS"],
        "order": 5,
        "is_featured": True,
        "security_model": {
            "threat_model": "PII exposure within vector embeddings.",
            "data_flow": "Documents scrubbed of PII before ingestion to the Qdrant index. Property-specific tenant segregation.",
            "access_control": "Hostel staff authenticated views.",
            "compliance_refs": ["GDPR", "Local fire safety regulations"],
            "owasp_mitigations": ["LLM06: Sensitive Information Disclosure"],
        },
    },
    {
        "name": "LegalFlow",
        "tagline": "RAG Platform for Dutch Law Firms — Attorney-Client Privilege by Design",
        "description": "Legal document ingestion via Docling for court filings. Attorney-client privilege modeled as matter-level vector isolation in Qdrant. NOvA-compliant audit trails.",
        "security_level": "HIGH",
        "domain": "legal",
        "stack": [
            "Django 6.0",
            "Pydantic AI",
            "Qdrant",
            "Docling",
            "PostgreSQL",
            "HTMX",
        ],
        "order": 6,
        "is_featured": True,
        "security_model": {
            "threat_model": "Cross-matter document retrieval breaching attorney-client privilege.",
            "data_flow": "Matter-level vector isolation in Qdrant. Strict data tenancy.",
            "access_control": "Role-based access: attorney, paralegal, and admin tiers with scoped retrieval limits. Audit trails for NOvA requirements.",
            "compliance_refs": ["GDPR", "AVG", "NOvA record-keeping"],
            "owasp_mitigations": ["LLM02: Insecure Output Handling"],
        },
    },
]

for idx, p_data in enumerate(projects_data):
    slug = slugify(p_data["name"])
    p, created = Project.objects.update_or_create(
        slug=slug,
        defaults={
            "name": p_data["name"],
            "tagline": p_data["tagline"],
            "description": p_data["description"],
            "security_level": p_data["security_level"],
            "domain": p_data["domain"],
            "order": p_data["order"],
            "is_featured": p_data["is_featured"],
        },
    )
    p.stack.set([tag_objs[t] for t in p_data["stack"]])

    # Create or update security model
    sec_data = p_data["security_model"]
    SecurityModel.objects.update_or_create(
        project=p,
        defaults={
            "threat_model": sec_data["threat_model"],
            "data_flow": sec_data["data_flow"],
            "access_control": sec_data["access_control"],
            "compliance_refs": sec_data["compliance_refs"],
            "owasp_mitigations": sec_data["owasp_mitigations"],
        },
    )

print("Database seeded successfully with 6 core projects.")
