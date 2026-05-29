# Blog API Loyihasi

## Loyiha haqida

Ushbu loyiha Django Rest Framework (DRF) yordamida yaratilgan Blog API hisoblanadi.

Loyiha imkoniyatlari:

* Authentication tizimi
* Custom User modeli
* Post CRUD
* Comment CRUD
* Like tizimi
* Category tizimi
* Profile boshqaruvi
* Filtering, Searching, Ordering
* Token Authentication
* Permission tizimi

---

# Ishlatilgan texnologiyalar

* Python
* Django
* Django Rest Framework
* SQLite
* Token Authentication

---

# O‘rnatish

## 1. Loyihani clone qilish

```bash
git clone <repository_url>
```

---

## 2. Virtual environment yaratish

```bash
python -m venv .venv
```

---

## 3. Virtual environmentni ishga tushirish

### Windows

```bash
.venv\Scripts\activate
```

### Linux / MacOS

```bash
source .venv/bin/activate
```

---

## 4. Kerakli kutubxonalarni o‘rnatish

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Project root ichida `.env` fayl yarating:

```env
SECRET_KEY=your_secret_key
DEBUG=True
```

---

# Loyihani ishga tushirish

## Migration qilish

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Superuser yaratish

```bash
python manage.py createsuperuser
```

---

## Serverni ishga tushirish

```bash
python manage.py runserver
```

---

# API Endpointlar

## Accounts

### Ro‘yxatdan o‘tish

```http
POST /api/accounts/sign-up/
```

### Login

```http
POST /api/accounts/login/
```

### Logout

```http
DELETE /api/accounts/logout/
```

### Profile

```http
GET /api/accounts/profile/
```

### Profile yangilash

```http
PATCH /api/accounts/profile-update/<id>/
```

---

# Postlar

### Postlarni olish

```http
GET /api/posts/post-list/
```

### Post yaratish

```http
POST /api/posts/post-list/
```

### Post detail

```http
GET /api/posts/detail/<id>/
```

### Post yangilash

```http
PATCH /api/posts/detail/<id>/
```

### Post o‘chirish

```http
DELETE /api/posts/detail/<id>/
```

---

# Commentlar

### Commentlarni olish

```http
GET /api/comments/comments/
```

### Comment yaratish

```http
POST /api/comments/comments/
```

### Comment detail

```http
GET /api/comments/comments/<id>/
```

### Comment yangilash

```http
PATCH /api/comments/comments/<id>/
```

### Comment o‘chirish

```http
DELETE /api/comments/comments/<id>/
```

---

# Like lar

### Like larni olish

```http
GET /api/likes/likes/
```

### Like bosish

```http
POST /api/likes/likes/
```

### Like detail

```http
GET /api/likes/detail-like/<id>/
```

### Like o‘chirish

```http
DELETE /api/likes/detail-like/<id>/
```

---

# Categoriyalar

### Category list

```http
GET /api/categories/list/
```

### Category yaratish

```http
POST /api/categories/create/
```

### Category detail

```http
GET /api/categories/detail/<id>/
```

---

# Filtering

Category bo‘yicha filter qilish:

```http
GET /api/posts/post-list/?category=1
```

---

# Search

Title bo‘yicha qidirish:

```http
GET /api/posts/post-list/?search=python
```

---

# Ordering

Yangi postlar:

```http
GET /api/posts/post-list/?ordering=-created_at
```

Eski postlar:

```http
GET /api/posts/post-list/?ordering=created_at
```

---

# Authentication

Protected endpointlar Token Authentication talab qiladi.

Misol:

```http
Authorization: Token your_token
```

---

# Permissionlar

* Faqat authenticated user create/update/delete qila oladi.
* Faqat object egasi o‘z objectini edit yoki delete qila oladi.

---

# Serializer Validation

* Title juda qisqa bo‘lishi mumkin emas.
* Description bo‘sh bo‘lishi mumkin emas.
* Comment juda qisqa bo‘lishi mumkin emas.

---

# Muallif

Afzalbek Ismatov
