import joblib
import os

current_dir = os.path.dirname(os.path.abspath(__file__))  

def getKnnModel():# Ruta del archivo actual
    file_path = os.path.join(current_dir, '..', 'data', 'files', 'knn_model.pkl')
    return joblib.load(file_path)

def getVectorizer():
    file_path = os.path.join(current_dir, '..', 'data', 'files', 'tfidf_vectorizer.pkl')
    return joblib.load(file_path)