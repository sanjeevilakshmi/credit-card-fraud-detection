<h1>🛡️ A Suspicious Financial Transaction Detection Model using Boosting Techniques<h1>

A machine learning–based system designed to detect suspicious and fraudulent financial transactions using boosting algorithms.
This project improves transaction security by analyzing financial data patterns and classifying transactions as legitimate or suspicious with high accuracy.

The system helps financial institutions reduce fraud risk, enhance monitoring efficiency, and ensure secure digital transactions.

🚀 Key Features

👤 Remote User Module

✅User registration and secure login

✅Upload transaction data

✅View prediction results (Normal / Fraudulent)

✅Track transaction history

🛡️ Service Provider (Admin) Module

✅Manage users and transaction records

✅Train and test machine learning models

✅View suspicious transaction reports

✅Monitor system performance

🤖 Machine Learning Features

✅Data preprocessing and feature engineering

✅Fraud classification using Boosting techniques

✅Risk-based transaction scoring

✅Performance evaluation using accuracy, precision, recall, and F1-score

🛠️ Tech Stack
Category	Technology
Programming Language	Python
Machine Learning	Boosting Algorithms (AdaBoost, Gradient Boosting)
Frontend	HTML, CSS, Bootstrap
Backend	Django
Database	MySQL / SQLite
Data Processing	Pandas, NumPy
ML Libraries	Scikit-learn
Visualization	Matplotlib
Version Control	Git & GitHub
IDE	VS Code / Jupyter Notebook
⚙️ Installation Guide

Follow these steps to run the project locally 👇

1️⃣ Clone the Repository
git clone https://github.com/sanjeevilakshmi/credit-card-fraud-detection.git
cd credit-card-fraud-detection
2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate        # Windows  
source venv/bin/activate    # Mac/Linux
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Setup Database

Update settings.py with your database credentials:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fraud_detection_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Run migrations:

python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser (Admin)
python manage.py createsuperuser
6️⃣ Run the Server
python manage.py runserver

Open your browser at 👉 http://127.0.0.1:8000/

🧩 Project Structure
credit_card_fraud_detection/
│
├── credit_card_fraud_detection/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── Remote_User/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── Service_Provider/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── app.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── static/
│   └── images/
│
├── Template/
│   └── htmls/
│       ├── RUser/
│       ├── SProvider/
│       └── images/
│
└── manage.py
📊 Learning Outcomes

Gained hands-on experience in Machine Learning model training and evaluation

Implemented Boosting algorithms for fraud detection

Learned data preprocessing and feature engineering techniques

Integrated ML models with Django web application

Improved understanding of financial transaction data analysis

Enhanced skills in Python, Pandas, NumPy, and Scikit-learn

💡 Future Enhancements

Integrate Deep Learning models (Autoencoders, Neural Networks)

Real-time transaction monitoring system

Add dashboard with charts and analytics

Deploy application on cloud platforms (AWS / Azure)

Improve model accuracy using hybrid ensemble techniques

Mobile application support

🧪 Results

Achieved high accuracy in detecting suspicious financial transactions

Reduced false positive rate using Boosting techniques

Efficient classification of normal vs fraudulent transactions

👩‍💻 Author

Sanjeevi Lakshmi Lavanya
🎓 B.Tech (4th Year)
💼 Skills: Python, Machine Learning, Django, HTML, Bootstrap, MySQL

📧 Email: 228r1a1252@gmail.com

🌐 GitHub: https://github.com/sanjeevilakshmi
