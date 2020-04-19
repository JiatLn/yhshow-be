from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify

from utils.algo import YuhunComb

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/calc', methods=['POST'])
def calc_yuhun():
    data = request.json

    yuhun_list = data.get('yuhun_list', [])
    l2_prop_limit = data.get('l2_prop_limit', [])
    l4_prop_limit = data.get('l4_prop_limit', [])
    l6_prop_limit = data.get('l6_prop_limit', [])
    optimize_pane = data.get('optimize_pane', '')
    limit_props = data.get('limit_props', {})
    limit_pane = data.get('limit_pane', {})
    plan = data.get('plan', {})
    shishen_pane = data.get('shishen_pane', {})

    yhc = YuhunComb(yuhun_list, l2_prop_limit, l4_prop_limit, l6_prop_limit,
                    optimize_pane, limit_props, limit_pane, plan, shishen_pane)
    res = yhc.pipeline()
    return jsonify({'res': res})


if __name__ == '__main__':
    app.run(debug=True)
