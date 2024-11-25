from flask import Flask
from flask_cors import CORS

from config.config import config

from routes.srRoutes import setupRoutesSr
from data.initContent import getLsaContent
from data.initContext import getLsaContext
from data.initDataframe import getDataFrame
from data.initKnn import getKnnModel, getVectorizer

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:4200"}})

def init_app(config):
    # Configuration
    app.config.from_object(config)
    
    # Initialize data
    app.lsa_content = getLsaContent()
    app.lsa_context = getLsaContext()
    app.data_frame = getDataFrame()
    app.knn_model = getKnnModel()
    app.vectorizer = getVectorizer()

    setupRoutesSr(app)

    CORS(app)

    return app

configuration = config['development']
app = init_app(configuration)

if __name__ == '__main__':
    app.run()