# Fidha & Rashid – Wedding Invitation Website

A Django-based digital wedding invitation that replicates the original PDF design with interactive animations.

## 📁 Project Structure

```
wedding_invite/
├── manage.py
├── requirements.txt
├── README.md
├── wedding_invite/          ← Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── invitation/              ← Django app
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── invitation/
│           ├── envelope.html      ← Page 1: Envelope with wax seal
│           ├── main_invite.html   ← Pages 2-3-4: Scrollable invitation + RSVP
│           ├── rsvp_yes.html      ← Golden confetti celebration
│           └── rsvp_no.html      ← Farewell page with auto-close
└── static/
    └── images/
        └── FIDHA___RASHID__1_.pdf  ← Original PDF (for reference)
```

## 🚀 Setup & Run

### 1. Install Python (3.10+)
Make sure Python is installed: `python --version`

### 2. Create virtual environment
```bash
cd wedding_invite
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run development server
```bash
python manage.py runserver
```

### 5. Open in browser
Visit: **http://127.0.0.1:8000/**

---

## 🎯 User Flow

1. **Envelope Page** (`/`) — Beautiful cream envelope with golden wax seal
   - Click anywhere on envelope → flap opens with animation
   - "Open Invitation" button appears → click to enter

2. **Main Invitation** (`/invite/`) — Scrollable page with 4 sections:
   - **Section 1** — Bismillah, bride & groom names, Arabic calligraphy
   - **Section 2** — Date (01 May 2026), time (3:30 PM), venue details
     - 📍 Click the **location pin icon** → opens Google Maps for directions
   - **Section 3** — "Hope you are coming" RSVP with YES / NO buttons
   - **Section 4** — Closing gratitude page

3. **RSVP YES** (`/rsvp/yes/`) — New page opens with:
   - ✨ Golden glittering confetti animation
   - Gratitude message in Arabic + English
   - Event reminder details

4. **RSVP NO** (`/rsvp/no/`) — New page opens with:
   - Falling rose petals
   - Graceful farewell message
   - Auto-closes in 10 seconds (or click "Close Invitation")

---

## 🎨 Design Details

- **Colors**: Deep crimson (#2d0508) + Gold (#c9a227) — matches original PDF exactly
- **Typography**: Cinzel (headings) + Cormorant Garamond (body) — elegant serif fonts
- **Animations**: Scroll-triggered fade-ups, envelope opening, confetti particles
- **Back navigation**: Every page has a ← Back button
- **Google Maps**: Location icon on venue page links to White Lilies Convention Center, Kodumudi

---

## 📝 Notes

- The Google Fonts CDN links in templates require internet access when the page loads
- For offline use, download fonts locally and update the `@import` URLs
- The Google Maps link opens: `https://maps.google.com/?q=White+Lilies+Convention+Center+Kodumudi`
- For production, set `DEBUG = False` in `settings.py` and configure `ALLOWED_HOSTS`
