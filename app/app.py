from flask import Flask, request, render_template, redirect, url_for
from policy_scrape import scrape_policy
from wordprocessor import summarize_notice

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', bullets = "EMPTY")

@app.route('/', methods=["POST"])
def submit_form():
    url = request.form['url']
    chunks = scrape_policy(url)
    if chunks:
        bullets = summarize_notice(chunks)
        return render_template('home.html', bullets = bullets)
    else:
        return redirect('/')

if __name__ == "__main__":
    app.run()