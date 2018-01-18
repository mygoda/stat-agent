# -*- coding: utf-8 -*-
# __author__ = xutao
import time
from flask import Flask
from flask import request
from flask import jsonify
import traceback
from tools import GetNetworkInterfaces

app = Flask(__name__)


@app.route('/net/', methods=["GET"])
def net_stat_api():
    """net stat api"""
    try:
        data = {}
        net_data = GetNetworkInterfaces()
        for net in net_data:
            data[net.get("interface")] = {
                "sendbytes": net["tx"]["bytes"],
                "recvbytes": net["rx"]["bytes"]
            }
        return jsonify({"status": "ok", "data": data})
    except Exception as e:
        return jsonify(
            {
                "status": "error",
                "message": traceback.format_exc()
            }
        )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7001)