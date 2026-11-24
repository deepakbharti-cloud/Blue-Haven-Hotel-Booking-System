<div align="center">
<img src="assets/banner.svg" alt="Blue Haven Hotel Booking System" width="100%"/>
<p>
<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
<img src="https://img.shields.io/badge/Bootstrap_5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap 5"/>
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
<img src="https://img.shields.io/badge/Razorpay-Test_Mode-0C2451?style=for-the-badge&logo=razorpay&logoColor=white" alt="Razorpay"/>
</p>
<img src="assets/tagline.svg" alt="Browse rooms. Book your stay. Pay securely." width="720"/>
<p>
<a href="#features"><img src="https://img.shields.io/badge/Features-0ea5e9?style=flat-square" alt="Features"/></a>
<a href="#how-a-booking-works"><img src="https://img.shields.io/badge/How_it_works-6366f1?style=flat-square" alt="How_it_works"/></a>
<a href="#quick-start"><img src="https://img.shields.io/badge/Quick_start-22c55e?style=flat-square" alt="Quick_start"/></a>
<a href="#data-model"><img src="https://img.shields.io/badge/Data_model-f59e0b?style=flat-square" alt="Data_model"/></a>
<a href="#production-checklist"><img src="https://img.shields.io/badge/Production_checklist-ef4444?style=flat-square" alt="Production_checklist"/></a>
<a href="#author"><img src="https://img.shields.io/badge/Author-a855f7?style=flat-square" alt="Author"/></a>
</p>
</div>
<img src="assets/divider.svg" alt="" width="100%"/>
## About
 
**Blue Haven** is a learning project that covers the full hotel-booking journey: room browsing, user accounts, validated booking forms, booking history, an admin panel, and optional **Razorpay** test-mode payments. Without Razorpay keys it falls back to a clearly labelled local demo flow, so you can try everything without charging a rupee.
 
## Features
 
<img src="assets/features.svg" alt="Feature overview" width="100%"/>
## How a booking works
 
<img src="assets/booking-flow.svg" alt="Booking flow: browse, sign in, pick dates, validate, pay, confirmed" width="100%"/>
## Tech stack
 
| Layer | Technology |
| --- | --- |
| Backend | Python 3.10+, Django |
| Frontend | HTML templates, Bootstrap 5 (CDN) |
| Database | SQLite |
| Payments | Razorpay Checkout (test mode) with local demo fallback |
| Admin | Django Admin |
 
## Quick start
 
> **Requirements:** Python 3.10+, pip, and internet access for the Bootstrap CDN and (optionally) Razorpay Checkout.
 
```bash
python -m venv venv
venv\Scripts\activate          # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations hotelapp
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
 
Then open:
 
| Page | URL |
| --- | --- |
| Website | http://127.0.0.1:8000/ |
| Rooms | http://127.0.0.1:8000/rooms/ |
| Admin | http://127.0.0.1:8000/admin/ |
 
> Add room records in Django Admin first, otherwise the public site will show no rooms.
 
<details>
<summary><b>Add a sample room</b></summary>
<br/>
| Field | Value |
| --- | --- |
| Name | Deluxe Room |
| Room type | Deluxe |
| Description | Comfortable room with a king-size bed and Wi-Fi. |
| Price per night | 2500 |
| Capacity | 2 |
| Is available | enabled |
| Image | optional |
 
</details>
<details>
<summary><b>Optional: Razorpay test mode</b></summary>
<br/>
Without keys, the project uses a local demo flow that does not charge money.
 
PowerShell example with test credentials:
 
```powershell
$env:RAZORPAY_KEY_ID="rzp_test_your_key_id"
$env:RAZORPAY_KEY_SECRET="your_test_secret"
python manage.py runserver
```
 
> Never commit secrets to GitHub. Do not use demo-payment mode in production.
 
</details>
<details>
<summary><b>Useful commands</b></summary>
<br/>
```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py test
```
 
</details>
## Data model
 
```mermaid
erDiagram
    USER ||--o{ BOOKING : makes
    ROOM ||--o{ BOOKING : "is booked in"
    ROOM {
        string name
        string room_type
        text description
        decimal price_per_night
        int capacity
        image image
        bool is_available
    }
    BOOKING {
        date check_in
        date check_out
        int guests
        decimal total_price
        string booking_status
        string payment_status
        string payment_ids
    }
```
 
- **Room** - name, type, description, nightly price, capacity, image, availability.
- **Booking** - user, room, dates, guests, total price, booking/payment status, payment IDs.
## Project structure
 
```text
Blue-Haven-Hotel-Booking-System/
|-- templates/            # HTML templates
|-- models.py             # Room, Booking
|-- forms.py              # booking / room / review forms
|-- views.py              # page and booking logic
|-- urls.py               # routes
|-- admin.py              # Django Admin setup
|-- apps.py
|-- hotel_detail.html     # hotel detail page
|-- room_detail.html      # room detail page
|-- room_form.html        # room form
|-- hotel_form.html       # hotel form
|-- review_form.html      # review form
|-- WORKING_DEMO.html     # static demo
|-- requirements.txt
`-- README.md
```
 
## Production checklist
 
This is an educational starter project, not a production-certified booking platform. Before going live:
 
- [ ] Set `DEBUG=False`, a strong `DJANGO_SECRET_KEY`, and valid `ALLOWED_HOSTS`
- [ ] Use HTTPS and secure cookie settings
- [ ] Keep API secrets out of source control
- [ ] Add payment webhooks, idempotency, reconciliation, and refund workflows
- [ ] Add transaction/locking protection against simultaneous overlapping bookings
- [ ] Add logging, backups, monitoring, notifications, and more tests
- [ ] Configure production static/media storage; review privacy and accessibility
## Troubleshooting
 
| Problem | Fix |
| --- | --- |
| `No module named django` | Activate the venv and run `pip install -r requirements.txt` |
| Rooms not showing | Add room records at `/admin/` |
| CSS missing | Check `static/css/style.css` |
| Migration issue | `python manage.py makemigrations hotelapp` then `python manage.py migrate` |
| Razorpay issue | Verify both test credentials and internet access |
 
## Author
 
**Deepak Bharti** - Django / Laravel developer
 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Deepak_Bharti-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/deepak-bharti-ab7622315)
[![GitHub](https://img.shields.io/badge/GitHub-deepakbharti--cloud-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/deepakbharti-cloud)
[![Portfolio](https://img.shields.io/badge/Portfolio-deepakbharti.github.io-38bdf8?style=flat-square&logo=googlechrome&logoColor=white)](https://deepakbharti.github.io)
 
<br/>
<img src="assets/footer.svg" alt="Built with Django by Deepak Bharti" width="100%"/>
