from flask import Flask, render_template, request, redirect, send_file
from extractors.wwr import extract_wwr_jobs
from extractors.remoteok import extract_remoteok_jobs
# from extractors.indeed import extract_indeed_jobs
from file import save_to_file

app = Flask("JobScrapper")
# for pythonanywhere setup
# app = Flask('GrabAJob', template_folder='/home/ssoyeee/Grab-a-job/templates/')


# Decorator
@app.route("/")
def home():
    return render_template("home.html", name="soyeon")

db = {}

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None or keyword == "":
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:    
        # indeed = extract_indeed_jobs(keyword)
        remoteok = extract_remoteok_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = wwr + remoteok
        # jobs = indeed + wwr
        db[keyword] = jobs
        return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None or keyword == "":
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])    
    return send_file(f"{keyword}.csv", as_attachment=True)

# for pythonanywhere setup
# if __name__ == '__main__':
#     app.debug = True
#     app.run(host="0.0.0.0", port=5050)
    
app.run("127.0.0.1", port=8000, debug=True)
