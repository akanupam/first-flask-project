from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS =[
    {
        'id': 1,
        'service':'ML engineering',
        'location':'Remote'
    },
    {
        'id': 2,
        'service': 'Software Development',
        'location': 'Remote'
    },
    {
        'id': 3,
        'service': 'WEB DEV',
        'location': 'Remote'
    }
]

@app.route("/")
def hello():
    return render_template("home.html", jobs=JOBS)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True) #to run the code

