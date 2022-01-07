from flask import Flask, render_template, make_response
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["secret"]

@app.route("/", methods = ['GET'])
def home():
  return render_template("home.html", title="Home - Mr. Nguyen's Website", description="The home page of Mr Nguyen's Website!")

@app.route("/about", methods = ['GET'])
def about():
  return render_template("about.html", title="About - Mr. Nguyen's Website", description="Learn more about Mr. Nguyen!")

@app.route("/pictures", methods = ['GET'])
def pictures():
  return render_template("pictures.html", title="Pictures - Mr. Nguyen's Website", description="Check out some fine pictures of Mr. Nguyen's universe!")

@app.route("/algebra-2", methods = ['GET'])
def algebra_2():
  return render_template("algebra-2.html", title="Algebra 2 - Mr. Nguyen's Website", description="A page for my Algebra 2 students!")

@app.route("/ap-statistics", methods = ['GET'])
def ap_statistics():
  return render_template("ap-statistics.html", title="AP Statistics - Mr. Nguyen's Website", description="A page for my AP Statistics students!")

@app.route("/ap-computer-science-a", methods = ['GET'])
def ap_computer_science_a():
  return render_template("ap-computer-science-a.html", title="AP Computer Science A - Mr. Nguyen's Website", description="A page for my AP Computer Science A students!")

@app.errorhandler(404)
def error_404(e):
  return render_template("404.html", title="404: Page Not Found - Mr. Nguyen's Website", description="Page not found!"), 404

@app.route('/main.css', methods = ['GET'])
def main_css():
  response = make_response(render_template("main.css"), 200)
  response.headers['Content-Type'] = 'text/css'
  return response

@app.route('/main.js', methods = ['GET'])
def main_js():
  response = make_response(render_template("main.js"), 200)
  response.headers['Content-Type'] = 'text/javascript'
  return response

@app.route('/logo')
def logo_site():
  return app.send_static_file('logo.png')

@app.route('/logo-rounded')
def logo_rounded_site():
  return app.send_static_file('logo-rounded.png')

@app.route('/favicon.ico')
def favicon_site():
  return app.send_static_file('favicon.ico')

app.run(host="0.0.0.0")