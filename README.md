# Nia Intelligence — Personal Portfolio

> Security-First AI Engineering · RAG · NIS2 · Local-First by Design

**Live Site:** [hassan.dev](https://hassan.dev) &nbsp;|&nbsp; **Stack:** Django 6.0 · HTMX · Alpine.js · Tailwind CSS · Qdrant

---

## The Problem

Enterprise teams in Benelux are adopting AI systems — but off-the-shelf RAG solutions force sensitive documents through external API calls, creating GDPR exposure and NIS2 compliance gaps. Most portfolios in this space offer demos. This one proves production-grade, audit-ready AI engineering.

## The Approach

Built with **security as the architecture**, not a layer bolted on top:

| Decision | Why |
|---|---|
| **Django 6.0 + HTMX** | Full-stack, no SPA complexity — server controls the data boundary |
| **Qdrant (embedded)** | Vector DB runs in-process; embeddings never leave the machine |
| **Pydantic AI** | Every LLM response is validated through typed models before reaching users |
| **django-secured-fields** | Fernet AES-128 encryption at the field level — encrypted at rest by default |
| **NeMo Guardrails** | Blocks prompt injection and out-of-scope queries at the guardrail layer |
| **Alpine.js** | Reactive UI with zero build step — no webpack, no node in production |
| **CSP + WhiteNoise** | Strict Content Security Policy shipped with compressed static assets |

The architecture supports both **cloud deployment** (Railway) and **air-gapped on-premise** — same codebase, switched via environment variables.

## The Result

A production-deployable RAG portfolio that demonstrates:

- ✅ Multi-agent RAG pipeline with chunk-level provenance tracking
- ✅ NIS2 / GDPR / ISO 27001 / OWASP LLM Top 10 mitigations documented per project
- ✅ Air-gapped deployment capability (offline-first vector search)
- ✅ Interactive project filtering by domain and security classification
- ✅ CLI-style contact form with HTMX partial updates

---

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+ (for Tailwind CSS build only)

### Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/your-username/personal-portfolio.git
cd personal-portfolio

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env and set a strong DJANGO_SECRET_KEY

# 5. Run database migrations
python manage.py migrate

# 6. (Optional) Seed sample projects
python seed_db.py

# 7. Start the dev server
python manage.py runserver
```

Visit `http://127.0.0.1:8000`

### Tailwind CSS (if modifying styles)

```bash
npm install
npm run dev   # watch mode
```

---

## Project Structure

```
personal-portfolio/
├── config/
│   ├── settings/
│   │   ├── base.py         # Shared settings (env-driven)
│   │   ├── local.py        # Dev overrides
│   │   └── production.py   # Production hardening (HSTS, SSL, etc.)
│   └── urls.py
├── portfolio/              # Core app — projects, home, architecture
│   ├── models.py           # Project + SecurityModel
│   ├── views.py            # Class-based views + HTMX endpoints
│   └── templates/
│       ├── portfolio/      # Page templates
│       └── htmx/          # Partial templates (HTMX swaps)
├── blog/                   # Blog app (markdownx)
├── contact/                # Contact form app
├── static/                 # CSS, JS, images
├── templates/              # Global base.html
├── .env.example            # ← copy this to .env
└── seed_db.py              # Sample data seeder
```

---

## Deployment

Designed for zero-downtime deploy to **Railway**:

1. Set all env vars from `.env.example` in your Railway project
2. Set `DJANGO_SETTINGS_MODULE=config.settings.production`
3. Railway auto-runs `python manage.py migrate` on deploy

For **air-gapped / on-premise**: Qdrant runs embedded, no external services required. Set `DATABASE_URL` to a local Postgres instance.

---

## Security Notes

- `SECRET_KEY` is read exclusively from environment — no hardcoded fallback
- `DEBUG=False` is enforced in production settings
- HSTS, SSL redirect, secure cookies, and CSP headers are enabled in production
- All sensitive model fields use Fernet AES-128 encryption at the database level

---

## License

MIT — see [LICENSE](LICENSE) for details.
