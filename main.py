from flask import Flask, render_template, request
from extractors.wwr import extract_wwr_jobs
# from extractors.indeed import extract_indeed_jobs


app = Flask("JobScrapper")

# Decorator
@app.route("/")
def home():
    return render_template("home.html", name="soyeon")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    # indeed = extract_indeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    # jobs = indeed + wwr
    return render_template("search.html", keyword=keyword, wwr=wwr)
app.run("127.0.0.1")