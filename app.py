from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import random
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key to secure session cookies


def init_db():
    conn = sqlite3.connect('contact.db')  # Create a database file
    cursor = conn.cursor()
    
    # Create a table for storing contact form submissions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    
        # Create a table for storing users (for login/signup)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')


    conn.commit()
    conn.close()

# Call the function to create the database
init_db()


# Quotes categorized
quotes = {
    "motivational": [
        "Believe in yourself and all that you are.",
        "Work hard in silence, let success make the noise.",
        "Success is the sum of small efforts repeated daily.",
        "Push yourself because no one else will do it for you.",
        "Dream big, work hard, stay focused, and surround yourself with good people.",
        "Do what you have to do until you can do what you want to do.",
        "The harder you work for something, the greater you'll feel when you achieve it.",
        "Great things never come from comfort zones.",
        "Stay patient and trust your journey.",
        "Difficult roads often lead to beautiful destinations.",
        "Do something today that your future self will thank you for.",
        "Your only limit is your mind.",
        "Opportunities don't happen, you create them.",
        "You don’t have to be great to start, but you have to start to be great.",
        "Failure is not the opposite of success, it is part of success."
    ],
    "love": [
        "Love is not about how much you say 'I love you' but how much you prove it's true.",
        "Love is the bridge between two hearts.",
        "The best thing to hold onto in life is each other.",
        "Love is when the other person's happiness is more important than your own.",
        "True love stories never have endings.",
        "Love is a choice you make every day.",
        "You don't love someone for their looks or their clothes, but because they sing a song only you can hear.",
        "The greatest thing you'll ever learn is just to love and be loved in return.",
        "Love is composed of a single soul inhabiting two bodies.",
        "To love and be loved is to feel the sun from both sides.",
        "Love is not finding someone to live with, it is finding someone you can't live without.",
        "Love does not dominate; it cultivates.",
        "We are most alive when we're in love.",
        "Love is the beauty of the soul.",
        "You are my today and all of my tomorrows."
    ],
    "life": [
        "Life is a journey, not a destination.",
        "Do what makes you happy, be with those who make you smile.",
        "Enjoy the little things, for one day you may look back and realize they were the big things.",
        "Live for today, hope for tomorrow.",
        "Happiness depends upon ourselves.",
        "Every moment is a fresh beginning.",
        "Life isn't about finding yourself, it's about creating yourself.",
        "Life is too important to be taken seriously.",
        "Do what you love and you'll never work a day in your life.",
        "Make each day your masterpiece.",
        "You only live once, but if you do it right, once is enough.",
        "Life is what happens when you're busy making other plans.",
        "The best way to predict your future is to create it.",
        "Life is really simple, but we insist on making it complicated.",
        "The purpose of life is not to be happy, but to be useful."
    ],
    "friendship": [
        "A friend is someone who knows all about you and still loves you.",
        "True friendship is never serene.",
        "Friendship is not about who you’ve known the longest, it’s about who came and never left your side.",
        "A real friend is one who walks in when the rest of the world walks out.",
        "A true friend is the greatest of all blessings.",
        "Friendship doubles your joys and divides your sorrows.",
        "Friends are the family we choose for ourselves.",
        "A friend is someone who gives you total freedom to be yourself.",
        "Many people will walk in and out of your life, but only true friends leave footprints in your heart.",
        "Good friends are like stars. You don’t always see them, but you know they’re always there.",
        "One loyal friend is worth ten thousand relatives.",
        "A friend to all is a friend to none.",
        "Friendship isn’t about whom you’ve known the longest, it’s about who came and never left your side.",
        "A true friend accepts who you are but also helps you become who you should be.",
        "A good friend is like a four-leaf clover: hard to find and lucky to have."
    ],
    "happiness": [
        "Happiness is not something ready-made, it comes from your own actions.",
        "Smile, not because life is easy, but because you choose to be happy.",
        "Happiness depends on what you decide to focus on.",
        "You do not find a happy life, you make it.",
        "Happiness is not a goal, it is a by-product of a life well-lived.",
        "The happiest people don’t have the best of everything, they make the best of everything.",
        "Happiness is letting go of what you think your life is supposed to be and celebrating it for everything that it is.",
        "The secret of happiness is freedom, and the secret of freedom is courage.",
        "Happiness is a choice, not a result. Nothing will make you happy until you choose to be happy.",
        "Happiness is like a butterfly; the more you chase it, the more it will elude you.",
        "A happy heart makes a cheerful face.",
        "Happiness is enjoying the simple things in life.",
        "Be so happy that when others look at you, they become happy too.",
        "Happiness is not in things, it is in us.",
        "Happiness is not a destination, it is a way of life."
    ],

    
    "Movie":[
        
        "Mogambo khush hua! – Mogambo",
    "Kitne aadmi the? – Gabbar Singh",
    "Don ko pakadna mushkil hi nahi, naamumkin hai. – Don",
    "Zindagi mein do cheez kabhi mat bhoolna, ek teri maa ka ashirwad, doosra apne desh ka namak. – Babu Moshai",
    "Dilwale Dulhania Le Jayenge. – Raj",
    "Tension lene ka nahi, dene ka. – Jai",
    "Tumse na ho payega. – Chulbul Pandey",
    "Jab tak tumhare paas apne haath hain, tab tak kuch bhi mumkin hai. – Raj",
    "Rishte mein toh hum tumhare baap lagte hain, naam hai Shahenshah. – Shahenshah",
    "Aaj khush toh bahut honge tum. – Gabbar Singh"
    ]
}

@app.route("/history")
def history():
    return render_template("app.html")

@app.route("/quote")
def quote():
    return render_template("quote.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/")
def home():
    category = request.args.get("category", "motivational")
    random_quotes = random.choice(quotes[category])
    return render_template("login.html", quotes=random_quotes)

@app.route("/quotes", methods=["GET"])
def get_quotes():
    category = request.args.get("category", "motivational")
    random_quotes = random.choice(quotes[category])
    return jsonify({"quotes": random_quotes})

# Route to render the signup page
@app.route('/signup')
def signup_page():
    return render_template('signup.html')

# Route to handle the signup logic
@app.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if not email or not password:
        return "Missing email or password", 400
    # Hash the password before saving it to the database
    hashed_password = generate_password_hash(password)
    
    # Insert the new user into the database
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_password))
        conn.commit()
        
        return render_template('login.html')  # Redirect to login page after successful signup
    except sqlite3.IntegrityError:
        return "Error: User already exists"
    finally:
        conn.close()
# Route to render the login page
@app.route('/login')
def login_page():
    return render_template('login.html')

# Route to handle the login logic
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form['password']
    
    # Check if the user exists and verify the password
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    
    if user and check_password_hash(user[2], password):  # Check if the hashed password matches
        session['user'] = email 
        return render_template('app.html')  # Redirect to home page if login is successful
    else:
        return "Invalid credentials"

@app.route('/logout')
def logout():
    session.clear()  # Clears the session data
    return render_template('login.html')  # Redirect to homepage after logout

# Function to insert contact form data into the database
def insert_contact(name, email, message):
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()

@app.route('/app')
def app_page():
    return render_template('app.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()

    # Fetch all messages
    cursor.execute("SELECT name, message FROM contacts")
    feedbacks = cursor.fetchall()

    conn.close()
    
    return render_template('app.html', feedbacks=feedbacks)


if __name__ == "__main__":
    app.run(debug=True)




