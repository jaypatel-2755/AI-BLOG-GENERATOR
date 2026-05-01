# 🚀 AI Blog Generator

A full-stack Django web application that generates high-quality blog posts using Google Gemini AI.

---

## 📌 Features

* ✨ Generate blog posts using AI
* 🔐 User authentication (Login / Logout)
* 📝 Save and manage blogs
* 📖 View detailed blog content
* 🗑️ Delete blogs
* 🎨 Clean and responsive UI

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite
* **AI Integration:** Google Gemini API

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-BLOG-GENERATOR.git
cd AI-BLOG-GENERATOR
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add environment variables

Create a `.env` file and add:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

### 5. Run migrations

```bash
python manage.py migrate
```

---

### 6. Start server

```bash
python manage.py runserver
```

---

### 7. Open in browser

```
http://127.0.0.1:8000/
```

---

## 📂 Project Structure

```
AI-BLOG-GENERATOR/
│
├── blog/
├── templates/
├── static/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## 🔑 API Used

* Google Gemini API (Generative AI)

---

## 💡 Future Improvements

* ✍️ Rich text editor
* 🌐 Deployment (Render / Railway)
* 📊 Blog analytics
* 🖼️ Image generation support

---

## 👨‍💻 Author

**Jay Patel**

---

⭐ If you like this project, don’t forget to give it a star!
