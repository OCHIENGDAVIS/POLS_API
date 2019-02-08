"""A  module to run the application"""
from app import create_app
from flask import jsonify
from instance import config
app = create_app(config.DevelopmentConfig)

@app.route("/"):
def home():
    response = dict{
        message = "Welcome Politico, go to /api/v1/parties to see all the parties"
    }
    return jsonify(response)
    

if __name__ == '__main__':
    app.run(debug=True)
