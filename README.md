# Blue Haven Hotel Booking System

A learning project built with Python, Django, Bootstrap 5, and SQLite. It demonstrates room browsing, user registration/login, booking forms, booking history, Django Admin, and optional Razorpay test-mode integration.

## Features
- Responsive homepage and room catalogue
- Room type filter and room details
- User registration, login, and logout
- Booking form with date and guest-capacity validation
- Basic overlap check for pending/confirmed bookings
- Price calculation based on nightly price Ã— nights
- My Bookings dashboard and unpaid-booking cancellation
- Django Admin for room and booking management
- Optional Razorpay test mode; local demo payment when keys are absent

## Requirements
- Python 3.10+
- pip
- Internet access for Bootstrap CDN and optional Razorpay Checkout

## Install and run (Windows / VS Code)
Extract the ZIP, open its folder in VS Code, then run:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations hotelapp
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- Website: http://127.0.0.1:8000/
- Rooms: http://127.0.0.1:8000/rooms/
- Admin: http://127.0.0.1:8000/admin/

Add room records in Django Admin before expecting rooms to appear on the public site.

## Add a sample room
- Name: Deluxe Room
- Room type: Deluxe
- Description: Comfortable room with a king-size bed and Wi-Fi.
- Price per night: 2500
- Capacity: 2
- Is available: enabled
- Image: optional

## Optional Razorpay test mode
Without keys, the project uses a clearly labelled local demo flow that does not charge money.

PowerShell example for Razorpay test credentials:

```powershell
$env:RAZORPAY_KEY_ID="rzp_test_your_key_id"
$env:RAZORPAY_KEY_SECRET="your_test_secret"
python manage.py runserver
```

Never commit secrets to GitHub. Do not use demo-payment mode in production.

## Useful commands
```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py test
```

## Project structure
```text
hotel_management/
â”œâ”€â”€ manage.py
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ README.md
â”œâ”€â”€ hotel_management/   # settings and root URLs
â”œâ”€â”€ hotelapp/            # models, forms, views, URLs, admin, tests
â”œâ”€â”€ templates/hotelapp/  # HTML templates
â””â”€â”€ static/css/          # stylesheet
```

## Models
- **Room:** name, type, description, nightly price, capacity, image, availability.
- **Booking:** user, room, dates, guests, total price, booking/payment status, payment IDs.

## Limitations / production checklist
This is an educational starter project, not a production-certified booking platform.
- Set `DEBUG=False`, a strong `DJANGO_SECRET_KEY`, and valid `ALLOWED_HOSTS`.
- Use HTTPS and secure cookie settings.
- Keep API secrets out of source control.
- Add payment webhooks, idempotency, reconciliation, and refund workflows.
- Add transaction/locking protection against simultaneous overlapping bookings.
- Add logging, backups, monitoring, notifications, and more tests.
- Configure production static/media storage and review privacy/accessibility.

## Troubleshooting
- `No module named django`: activate venv and install requirements.
- Rooms not showing: add room records at `/admin/`.
- CSS missing: check `static/css/style.css`.
- Migration issue: run `python manage.py makemigrations hotelapp` then `python manage.py migrate`.
- Razorpay issue: verify both test credentials and internet access.

## Author
**Deepak Bharti**  
LinkedIn: https://www.linkedin.com/in/deepak-bharti-ab7622315
