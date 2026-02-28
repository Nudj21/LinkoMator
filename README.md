# ✂️ LinkoMator - URL Shortener & Analytics

A full-stack, lightweight URL shortener built with Python and Flask. This application takes long, cumbersome URLs and converts them into compact, easily shareable short links. It also features a built-in analytics dashboard to track how many times each link has been clicked.

## ✨ Features
* **Link Shortening:** Instantly generates a random 5-character short code for any valid URL.
* **Seamless Redirection:** Users clicking the short link are instantly routed to the original destination.
* **Analytics Dashboard:** A clean, modern UI that tracks and displays the total number of clicks for every generated link.
* **Persistent Storage:** Uses a lightweight SQLite database to securely store URLs and click data.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Database:** SQLite3 (Built-in)
* **Frontend:** HTML5, CSS3 (Custom responsive styling)

## 🚀 How to Run Locally

If you want to download this code and run it on your own machine, follow these steps in your terminal:

```bash
# 1. Clone the repository and enter the folder
git clone https://github.com/Nudj21/LinkoMator.git
cd LinkoMator

# 2. Create and activate a virtual environment (Windows)
python -m venv venv
.\venv\Scripts\activate

# 3. Install the required dependencies
pip install Flask

# 4. Run the application
python app.py
```

Step 5: Open your web browser and navigate to http://127.0.0.1:5000 to use the app! (Note: A local urls.db file will automatically be generated the first time you run it)