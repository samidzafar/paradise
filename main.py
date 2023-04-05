from flask import Flask, render_template
app = Flask(__name__) 
  
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/details")
def details():
    return render_template('vec_but.html')



@app.route("/five")
def five():
    return render_template('5_7.html')


@app.route("/four")
def four():
    return render_template('4_6.html')



@app.route("/horizontal")
def horizontal():
    return render_template('horizontal.html')


@app.route("/vertical")
def vertical():
    return render_template('vertical.html')


@app.route("/hom")
def ho():
    return render_template('index.html')













if __name__ == '__main__':
    print("I am in")
    app.run(host='0.0.0.0', port=80, debug=True)