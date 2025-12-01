
Quotify

Quotify is a simple and elegant web application designed for storing, displaying, and managing meaningful quotes. It provides users with the ability to sign up, log in, submit new quotes, and explore a gallery of all submitted quotes. Built with HTML on the frontend and Python (Flask) on the backend, this project is lightweight, clean, and beginner-friendly.

#Features

- User Authentication
  - Signup & Login system
  - Secure user data handling

- Quote Management
  - Add new quotes
  - View all quotes in a gallery layout
  - View each quote on a dedicated page

- Backend + Frontend Integration
  - Flask handles routing and data processing
  - HTML templates render the UI
  - Simple, minimalistic, easy to extend

---

#Tech Stack

Frontend:  
- HTML5  
- Basic CSS (custom or inline with templates)

Backend:  
- Python  
- Flask Framework  

Database:  
- SQLite (via custom model definitions in `models.py`)

---

#Project Structure

```

Quotify/
│
├── app.py                # Main Flask application
├── models.py             # Quote and user models
├── database_setup.py     # Script to initialize/reset database
├── init_db.py            # Additional DB initialization script
│
├── login.html            # Login page
├── signup.html           # Signup page
├── gallery.html          # All quotes displayed here
├── quote.html            # Individual quote display
├── app.html              # Additional layout/template page
│
└── static/               # (If added) CSS, images, etc.

````

---

#How to Run the Project Locally

1️⃣ Clone the Repository
```bash
git clone https://github.com/YesadeSamiksha/Quotify.git
cd Quotify
````

2️⃣ Create a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

3️⃣ Install Dependencies

If you have a `requirements.txt`, run:

```bash
pip install -r requirements.txt
```

4️⃣ Initialize the Database

Run whichever file applies:

```bash
python database_setup.py
```

or

```bash
python init_db.py
```

5️⃣ Start the Application

```bash
python app.py
```

Now open your browser and visit:

➡️ `http://127.0.0.1:5000/`
Your Quotify app should now be running!

---

#Why Quotify?

* Minimalistic and beginner-friendly
* Demonstrates real backend-frontend integration
* Shows basic CRUD functionality and authentication
* Great for students building their first Flask project
* Easy to customize, upgrade, or expand

---

#Future Enhancements (Roadmap)

* Add quote editing & deletion
* Improve UI with better styling
* Add search/filter to the quote gallery
* Introduce user roles (e.g., admin)
* API endpoints for quotes (REST API)
* Dark/light theme UI
* Export quotes as images for social media

---

#Contributing

Feel free to fork this project, open issues, or submit pull requests.
Suggestions and improvements are always welcome!

---

#Author

Samiksha Yesade
Developer • Engineering Student • Tech Enthusiast

Built with passion and creativity 

```
```
