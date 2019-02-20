from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
  return render_template("index.html")

@app.route('/p5-intro')
def p5Intro():
  return render_template("p5-intro.html")

@app.route('/sketchup-intro')
def sketchUpIntro():
  return render_template("sketchup-intro.html")

if __name__ == '__main__':
  app.run(debug=True)

