# 📝 Smurfia – Question & Word API

Django REST API serving curated vocabulary and practice questions
for the Smurfia language learning app. Deployed on Render with PostgreSQL.

## ⚙️ Tech Stack
- Django + Django REST Framework
- PostgreSQL (environment-managed)
- Knox Token + SimpleJWT Authentication
- django-filter
- Render deployment

## 📡 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/words/` | Paginated word list by topic/level |
| GET | `/questions/` | Practice questions by category |

## 🔗 Related
- Mobile App: [Smurfia – HataDefteri](https://github.com/Busrwa/HataDefteri)

## 🚀 Getting Started
```bash
git clone https://github.com/Busrwa/QuestionWordApi.git
cd QuestionWordApi
pip install -r requirements.txt
# Add .env: DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, SECRET_KEY
python manage.py migrate
python manage.py runserver
```
