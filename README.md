# 🧠 Fake Profile Detection Web App

A simple Machine Learning web application that detects whether a social media profile is **Fake** or **Real** using user input features.

---

## 🚀 Live Demo

🔗 https://fake-profile-detection-st64.onrender.com

---

## 📌 Features

* Predicts **Fake vs Real profiles**
* Simple and clean web interface
* Built using Machine Learning
* Deployed online for public use

---

## 🛠️ Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* HTML / CSS
* Gunicorn (for deployment)

---

## 📂 Project Structure

```
Fakeid/
│── app.py
│── model.pkl
│── train_model.py
│── requirements.txt
│
├── templates/
│     └── index.html
│
└── static/
      └── style.css
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/fake-profile-detection.git
cd fake-profile-detection
```

---

### 2️⃣ Install dependencies

```
python -m pip install -r requirements.txt
```

---

### 3️⃣ Run the app

```
python app.py
```

---

### 4️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 🧪 Input Features

The model uses the following inputs:

* Followers count
* Following count
* Number of posts
* Bio (0 or 1)
* Profile picture (0 or 1)
* Verified account (0 or 1)

---

## 🤖 Machine Learning Model

* Algorithm: Random Forest Classifier
* Trained on sample dataset
* Outputs:

  * **0 → Real Profile**
  * **1 → Fake Profile**

---

## ⚠️ Note

This is a **basic demo project**.
The dataset is small and used for learning purposes.

---

## 👨‍💻 Author

Shyam

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share it

---

## 📜 License

This project is open-source and free to use.
