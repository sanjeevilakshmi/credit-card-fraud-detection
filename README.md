

<h1>🧠 A Suspicious Financial Transaction Detection Model using Boosting Techniques</h1>

<p>
A machine learning–based system designed to detect suspicious and fraudulent financial transactions using boosting algorithms.
This project improves transaction security by analyzing financial data patterns and classifying transactions as legitimate or suspicious with high accuracy.
</p>

<p>
The system helps financial institutions reduce fraud risk, enhance monitoring efficiency, and ensure secure digital transactions.
</p>

<hr>

<h2>🚀 Key Features</h2>

<h3>👤 Remote User Module</h3>
<ul>
    <li>User registration and secure login</li>
    <li>Upload transaction data</li>
    <li>View prediction results (Normal / Fraudulent)</li>
    <li>Track transaction history</li>
</ul>

<h3>🛡️ Service Provider (Admin) Module</h3>
<ul>
    <li>Manage users and transaction records</li>
    <li>Train and test machine learning models</li>
    <li>View suspicious transaction reports</li>
    <li>Monitor system performance</li>
</ul>

<h3>🤖 Machine Learning Features</h3>
<ul>
    <li>Data preprocessing and feature engineering</li>
    <li>Fraud classification using Boosting techniques</li>
    <li>Risk-based transaction scoring</li>
    <li>Performance evaluation using accuracy, precision, recall, and F1-score</li>
</ul>

<hr>

<h2>🛠️ Tech Stack</h2>

<table border="1" cellpadding="8">
    <tr>
        <th>Category</th>
        <th>Technology</th>
    </tr>
    <tr>
        <td>Programming Language</td>
        <td>Python</td>
    </tr>
    <tr>
        <td>Machine Learning</td>
        <td>AdaBoost, Gradient Boosting</td>
    </tr>
    <tr>
        <td>Frontend</td>
        <td>HTML, CSS, Bootstrap</td>
    </tr>
    <tr>
        <td>Backend</td>
        <td>Django</td>
    </tr>
    <tr>
        <td>Database</td>
        <td>MySQL / SQLite</td>
    </tr>
    <tr>
        <td>Data Processing</td>
        <td>Pandas, NumPy</td>
    </tr>
    <tr>
        <td>ML Libraries</td>
        <td>Scikit-learn</td>
    </tr>
    <tr>
        <td>Visualization</td>
        <td>Matplotlib</td>
    </tr>
    <tr>
        <td>Version Control</td>
        <td>Git & GitHub</td>
    </tr>
    <tr>
        <td>IDE</td>
        <td>VS Code / Jupyter Notebook</td>
    </tr>
</table>

<hr>

<h2>⚙️ Installation Guide</h2>

<h3>1️⃣ Clone the Repository</h3>
<pre>
git clone https://github.com/&lt;your-username&gt;/credit-card-fraud-detection.git
cd credit-card-fraud-detection
</pre>

<h3>2️⃣ Create a Virtual Environment</h3>
<pre>
python -m venv venv
venv\Scripts\activate        # Windows  
source venv/bin/activate     # Mac/Linux
</pre>

<h3>3️⃣ Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>4️⃣ Setup Database</h3>
<pre>
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
</pre>

<h3>Run Migrations</h3>
<pre>
python manage.py makemigrations
python manage.py migrate
</pre>

<h3>5️⃣ Create Superuser</h3>
<pre>
python manage.py createsuperuser
</pre>

<h3>6️⃣ Run Server</h3>
<pre>
python manage.py runserver
</pre>

<p><b>Open in browser:</b> http://127.0.0.1:8000/</p>

<hr>

<h2>🧩 Project Structure</h2>

<pre>
    
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
</pre>

<hr>

<h2>📊 Learning Outcomes</h2>
<ul>
    <li>Hands-on experience in ML model training and evaluation</li>
    <li>Implemented Boosting algorithms for fraud detection</li>
    <li>Learned data preprocessing and feature engineering</li>
    <li>Integrated ML models with Django web application</li>
    <li>Improved understanding of financial data analysis</li>
</ul>

<hr>

<h2>💡 Future Enhancements</h2>
<ul>
    <li>Real-time transaction monitoring</li>
    <li>Analytics dashboard with charts</li>
    <li>Cloud deployment (AWS / Azure)</li>
    <li>Mobile application support</li>
</ul>

<hr>

<h2>🧪 Results</h2>
<ul>
    <li>High accuracy in detecting suspicious transactions</li>
    <li>Reduced false positive rate</li>
    <li>Efficient classification of normal vs fraudulent</li>
</ul>

<hr>

<h2>👩‍💻 Author</h2>
<p>
<b>Name:</b> Sanjeevi Lakshmi Lavanya<br>
<b>Qualification:</b> B.Tech (4th Year)<br>
<b>Skills:</b> Python, Machine Learning, Django, HTML, Bootstrap, MySQL<br>
<b>Email:</b> 228r1a1252@gmail.com<br>
<b>GitHub:</b> https://github.com/sanjeevilakshmi
</p>

</body>
</html>
