from flask import Flask, render_template, jsonify
from db import DataBaseConnection
from loguru import logger
from datetime import datetime

app = Flask(__name__)
db_handler = DataBaseConnection()
logger.add(f"logs/{datetime.now().date()}.log", rotation="500 MB")

@app.route("/")
def index():
    ds = {
        'count': db_handler.make_select_query(
                    "SELECT count FROM COUNTER"
                )[0][0]
    }
    logger.info('Render index template')
    return render_template('index.html', ds=ds)

@app.route("/send_request", methods=["GET"])
def accept_request():
    db_handler.make_update_query(
        "UPDATE counter SET count = count + 1"
    )
    ds = {
        "msg": "It`s time to increase your counter!",
        "status_code": 200
    }
    logger.info("Increase counter")
    return jsonify(ds)


if __name__ == '__main__':
    logger.info("Start app")
    app.run(debug=True, host='0.0.0.0', port=5000)
