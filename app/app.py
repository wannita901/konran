from flask import Flask, request, render_template
import policy_scrape
# import wordprocessor

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get('url')
        blocks = policy_scrape.scrape_policy(url)
        return blocks
    return render_template('home.html')

if __name__ == "__main__":
    app.run()