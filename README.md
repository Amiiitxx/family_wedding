# Family Wedding Centre — Django Website

A **production-ready, fully responsive** wedding fashion retail website for **Family Wedding Centre**, Kerala.

Built with **Python + Django + PostgreSQL** and a premium custom UI.

---

## Tech Stack

| Layer     | Technology                        |
|-----------|-----------------------------------|
| Backend   | Python 3.10+, Django 4.2          |
| Database  | PostgreSQL                        |
| ORM       | Django ORM                        |
| Frontend  | Django Templates, HTML5, CSS3, Vanilla JS |
| Fonts     | Cormorant Garamond + Inter (Google Fonts) |
| Images    | Pillow                            |
| Config    | python-decouple (.env)            |

---

## Project Structure

```
family_wedding/
├── manage.py
├── requirements.txt
├── .env.example
├── README.md
│
├── family_wedding/          # Django project package
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── core/                    # Main app
│   ├── models.py            # Store, Brand, Collection, GalleryImage, Enquiry
│   ├── forms.py             # EnquiryForm
│   ├── views.py             # All page views
│   ├── urls.py
│   ├── admin.py
│   ├── sitemaps.py
│   ├── context_processors.py
│   ├── migrations/
│   └── management/commands/
│       └── seed_data.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── collections.html
│   ├── brands.html
│   ├── stores.html
│   ├── gallery.html
│   ├── contact.html
│   └── components/
│       ├── header.html
│       ├── footer.html
│       └── store_card.html
│
└── static/
    ├── css/
    │   ├── style.css
    │   └── responsive.css
    ├── js/
    │   └── main.js
    └── images/
        ├── logo.png               ← Place your logo here
        ├── logo-white.png         ← White version for footer
        ├── malayalam_campaign.jpg ← Place your campaign artwork here
        ├── hero-1.jpg
        ├── hero-2.jpg
        ├── about-1.jpg
        ├── about-hero.jpg
        ├── collections-hero.jpg
        ├── stores-hero.jpg
        └── og-image.jpg
```

---

## Setup Instructions

### 1. Prerequisites

- Python 3.10+
- PostgreSQL 14+
- pip or the workspace .venv

### 2. Clone / Navigate to project

```bash
cd "c:\Users\LENOVO\OneDrive\Desktop\Applet logic\python_Django\family_wedding"
```

### 3. Create & Activate Virtual Environment

```bash
# Create venv (if not already done by the workspace)
python -m venv .venv

# Activate on Windows
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

```bash
# Copy the example file
copy .env.example .env
```

Edit `.env` with your PostgreSQL credentials:

```
SECRET_KEY=your-very-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=family_wedding_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

### 6. Create PostgreSQL Database

Open **pgAdmin** or **psql** and run:

```sql
CREATE DATABASE family_wedding_db;
```

Or via psql CLI:

```bash
psql -U postgres -c "CREATE DATABASE family_wedding_db;"
```

### 7. Run Migrations

```bash
python manage.py migrate
```

### 8. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 9. Seed Initial Data

```bash
python manage.py seed_data
```

This will create:
- ✅ 7 store locations
- ✅ 10 fashion brands
- ✅ 5 collections

### 10. Add Your Brand Images

Place the following files in `static/images/`:

| File | Description |
|------|-------------|
| `logo.png` | Family Wedding Centre logo |
| `logo-white.png` | White version for footer (or same logo) |
| `malayalam_campaign.jpg` | Malayalam campaign artwork |
| `hero-1.jpg` | Hero slide 1 (Indian wedding couple) |
| `hero-2.jpg` | Hero slide 2 |
| `about-1.jpg` | About page main image |
| `about-hero.jpg` | About page hero background |
| `collections-hero.jpg` | Collections page hero |
| `stores-hero.jpg` | Stores page hero |
| `og-image.jpg` | Open Graph / social media image (1200×630px) |

> **Tip:** Use any high-quality Indian wedding photography for hero/about images. The campaign artwork should NOT be distorted — it will be displayed with `object-fit: contain`.

### 11. Collect Static Files (Production)

```bash
python manage.py collectstatic
```

### 12. Run Development Server

```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

Admin panel: **http://127.0.0.1:8000/admin/**

---

## Pages

| URL | Page |
|-----|------|
| `/` | Home |
| `/about/` | About Us |
| `/collections/` | Collections |
| `/brands/` | Our Brands |
| `/stores/` | Our Stores |
| `/gallery/` | Gallery |
| `/contact/` | Contact / Enquiry |
| `/admin/` | Django Admin |
| `/sitemap.xml` | XML Sitemap |
| `/robots.txt` | Robots.txt |

---

## Admin Panel

Login at `/admin/` with your superuser credentials.

Manage:
- **Stores** — add/edit/deactivate store locations, upload store images
- **Brands** — add brand logos, set display order
- **Collections** — add collection images, edit descriptions
- **Gallery Images** — upload wedding fashion photos, assign categories
- **Enquiries** — view customer enquiries, mark as contacted

---

## Adding Gallery Images

1. Go to `/admin/core/galleryimage/add/`
2. Upload your image
3. Select a category (Bridal, Groom, Couple, Family, Jewellery, Wedding Fashion)
4. Set display order
5. Save

---

## Security Notes

- All secrets are read from `.env` via `python-decouple`
- CSRF protection is active on all forms
- Never commit `.env` to version control
- Set `DEBUG=False` in production
- Set `ALLOWED_HOSTS` to your domain in production

---

## Responsive Design

Tested at:
- 360px (Android small)
- 390px (iPhone 14)
- 430px (iPhone 14 Pro Max)
- 768px (iPad portrait)
- 1024px (iPad landscape)
- 1366px (laptop)
- 1440px (desktop)
- 1920px (wide monitor)

---

## Brand Colors

| Color | Value | Usage |
|-------|-------|-------|
| Purple | `#5B2D8E` | Primary brand color |
| Dark Purple | `#3D1A6E` | Hover states, headers |
| Deepest Purple | `#2D0A4E` | Footer, overlays |
| Accent | `#C0395B` | CTA buttons, highlights |
| Off-white | `#FAF8F5` | Page background |

---

## Contact

Family Wedding Centre  
Corporate Office, Kunnamangalam  
Calicut, Kerala — 673571  
📞 +91 8943 63 63 63
