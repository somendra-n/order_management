# 🛒 Order Management System – Django + DRF + Google OAuth 2.0

A secure, scalable **Order Management System** built using Django, Django REST Framework, and Google OAuth 2.0 for seamless third-party authentication.

---

## ✨ Features

- ✅ Google OAuth 2.0 Login (via `django-allauth`)
- 🔐 JWT Authentication using `dj-rest-auth` & `SimpleJWT`
- 📦 Order creation and retrieval APIs
- 📂 Organized and modular Django project
- 🧪 Protected endpoints with token-based access
- 🔐 Secure `.env` usage for sensitive credentials

---

## 📁 Project Structure

order_management/
├── manage.py
├── .env
├── .env.example
├── requirements.txt
├── README.md
├── db.sqlite3
├── order_management/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── orders/
│ ├── init.py
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ ├── urls.py
│ └── migrations/

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/order-management.git
cd order-management
2. Create a virtual environment
# macOS/Linux
python3 -m venv env
source env/bin/activate

# Windows (CMD)
env\Scripts\activate.bat
3. Install dependencies
pip install -r requirements.txt
________________________________________
🔐 Environment Setup
Create a .env file in the project root and configure the following:
# .env
SECRET_KEY=your-django-secret-key
GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-google-client-secret
📁 You can use .env.example as a reference.
________________________________________
🚀 Run the Project
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Access the site at: http://localhost:8000
________________________________________
🔑 Google OAuth Integration
Step 1: Setup Google App
•	Go to Google Cloud Console
•	Create a project → OAuth Consent Screen
•	Add credentials → OAuth Client ID
•	Redirect URI:
•	http://localhost:8000/accounts/google/login/callback/
Step 2: Login Flow
1.	Open:
2.	https://accounts.google.com/o/oauth2/v2/auth?response_type=token&client_id=your-client-id&redirect_uri=http://localhost:8000/accounts/google/login/callback/&scope=email profile
3.	Copy the access_token from the URL.
4.	Authenticate with backend:
curl -X POST http://localhost:8000/auth/google/ \
-H "Content-Type: application/json" \
-d '{"access_token": "your-google-access-token"}'
________________________________________
🔗 API Endpoints
Method	Endpoint	                 Description
POST	/auth/google/	              Login via Google access token
POST	/auth/login/	              Login via credentials
POST	/auth/registration/	        Register new user
GET	  /api/orders/	List          all orders (JWT required)
POST	/api/orders/add/	          Add a new order (JWT required)
________________________________________
🛠 Example: Use Auth Token
Once authenticated, use the JWT token to access protected endpoints:
curl -X GET http://localhost:8000/api/orders/ \
-H "Authorization: Bearer your-jwt-token"
________________________________________
📜 Example .env.example
# .env.example

# Django secret key (required)
SECRET_KEY=your-django-secret-key

# Google OAuth2 credentials
GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-google-client-secret
________________________________________
📦 requirements.txt
If not already present, generate it using:
pip freeze > requirements.txt
Example:
Django==5.1
djangorestframework==3.15.1
dj-rest-auth==5.0.1
django-allauth==0.61.1
python-decouple==3.8
python-dotenv==1.0.1
google-auth==2.29.0
google-auth-oauthlib==1.2.0
________________________________________
✅ Final Submission Checklist
•	All migrations and models included
•	Google OAuth2 login is working
•	REST API for orders implemented
•	.env and .env.example provided
•	README with clear setup instructions
•	JWT auth working for protected routes
•	Admin panel accessible for site config
________________________________________
🧠 How Components Work Together
Component	Role
Django	Main web framework for routing and models
DRF	Builds API views and serializers
django-allauth	Handles Google login and user creation
dj-rest-auth	Manages JWT login/logout/registration
SimpleJWT	Issues and verifies tokens securely
dotenv	Loads .env variables into Django
Orders app	Custom logic for adding & retrieving orders
________________________________________
👨‍🏫 Conclusion
This project demonstrates an end-to-end integration of secure, third-party login using Google OAuth2 with a REST-based backend built in Django. It uses token-based authentication (JWT) to secure access to core order APIs.

