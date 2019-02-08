"""A  module to run the application"""
from app import create_app
# from instance.config import app_config
from instance import config



app = create_app(config.ProductionConfig)
app.run(debug=True)
