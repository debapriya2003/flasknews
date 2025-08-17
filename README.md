---

# 📰 News App with Flask API & Streamlit Dashboard

This project provides a simple **News Management System** built with **Flask**, **MongoDB**, and **Streamlit**.
It has two main components:

1. **Flask API** – Fetches and serves stored news articles from MongoDB.
2. **Streamlit Dashboard** – Allows adding new news articles and optionally viewing existing ones.

---

## 🚀 Features

* **Backend (Flask + MongoDB)**

  * REST API endpoint `/news` to fetch all articles in JSON format.
  * Articles are sorted by latest first (`_id` descending).
  * CORS enabled for cross-origin requests.

* **Frontend (Streamlit Dashboard)**

  * User-friendly interface for inserting news articles.
  * Form with fields for:

    * Image URL
    * Headline
    * Description
    * Ad Image URL
    * News Link
  * Validation to ensure all fields are filled.
  * Displays submitted articles with images and links.
  * Option to view existing stored articles.

---

## 🛠️ Tech Stack

* **Python**
* **Flask** (REST API backend)
* **Streamlit** (Dashboard frontend)
* **MongoDB Atlas** (Database)
* **PyMongo** (MongoDB client)
* **Flask-CORS** (CORS handling)

---

## 📂 Project Structure

```
project/
│
├── flask_app.py         # Flask API to serve news articles
├── streamlit_app.py     # Streamlit dashboard for news entry
├── requirements.txt     # Dependencies list
└── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/news-app.git
cd news-app
```

### 2. Install Dependencies

Create a virtual environment (recommended) and install requirements:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
flask
flask-cors
streamlit
pymongo
```

### 3. Configure MongoDB

* Create a **MongoDB Atlas Cluster**.
* Replace the `MONGO_URL` in both files with your connection string.
* Example:

  ```python
  MONGO_URL = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
  ```

### 4. Run Flask API

```bash
python flask_app.py
```

Flask will start at:
`http://localhost:5000/news`

### 5. Run Streamlit Dashboard

```bash
streamlit run streamlit_app.py
```

Dashboard will open in your browser:
`http://localhost:8501`

---

## 📡 API Endpoint

### Get All News

**Request:**

```
GET /news
```

**Response (JSON):**

```json
[
  {
    "image": "https://example.com/image.jpg",
    "headline": "Sample Headline",
    "description": "This is a sample news description.",
    "adImage": "https://example.com/ad.jpg",
    "link": "https://example.com/news"
  }
]
```

---

## 📸 Streamlit Dashboard Preview

* **Add News Article Form**
* **Show Existing Articles (Optional)**

---

## ✅ Future Improvements

* Add authentication for news submission.
* Enable editing and deleting news articles.
* Enhance UI with categories, tags, and filters.
* Deploy API + Dashboard on cloud platforms (e.g., Heroku, Streamlit Cloud).

---

## 👨‍💻 Author

Developed by **Debapriya Mukherjee** ✨

---

Do you want me to also make a **`requirements.txt` file** for this so you can run it directly?
