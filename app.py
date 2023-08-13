from flask import Flask, render_template, make_response, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/send_request", methods=["GET"])
def accept_request():
    ds = {
        "msg": "It`s time to increase your counter!",
        "status_code": 200
    }
    return jsonify(ds)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
