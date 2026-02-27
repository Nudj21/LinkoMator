from flask import Flask, render_template, request, redirect
import string
import random
import sqlite3

app = Flask(__name__)

# --- 1. UPDATED DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    # Notice we added a new column: 'clicks INTEGER DEFAULT 0'
    c.execute('''CREATE TABLE IF NOT EXISTS urls
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  original_url TEXT NOT NULL,
                  short_code TEXT NOT NULL UNIQUE,
                  clicks INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()

init_db()

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(5))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['long_url']
        short_code = generate_short_code()
        
        conn = sqlite3.connect('urls.db')
        c = conn.cursor()
        c.execute("INSERT INTO urls (original_url, short_code) VALUES (?, ?)", (original_url, short_code))
        conn.commit()
        conn.close()
        
        # After saving, refresh the page to show the updated table
        return redirect('/')
    
    # --- 2. FETCH ANALYTICS DATA ---
    # Every time the home page loads, we grab all URLs from the database
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT * FROM urls")
    urls = c.fetchall() # This grabs everything as a list
    conn.close()

    # We send that list (urls) over to our HTML file!
    return render_template('index.html', urls=urls)

@app.route('/<short_code>')
def redirect_url(short_code):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT original_url FROM urls WHERE short_code=?", (short_code,))
    url_data = c.fetchone()

    if url_data:
        # --- 3. THE ANALYTICS MATH ---
        # If the URL exists, add +1 to the click counter!
        c.execute("UPDATE urls SET clicks = clicks + 1 WHERE short_code=?", (short_code,))
        conn.commit()
        conn.close()
        
        # Then, redirect them to their destination
        return redirect(url_data[0])
    else:
        conn.close()
        return "<h1>URL not found</h1>", 404

if __name__ == '__main__':
    app.run(debug=True)