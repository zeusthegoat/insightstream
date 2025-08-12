from flask import jsonify

def error_response(msg, code=400):
    return jsonify({"error": msg}), code