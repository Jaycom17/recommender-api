import numpy as np
import os

def getLsaContent():
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Ruta del archivo actual
    file_path = os.path.join(current_dir, '..', 'data', 'files', 'lsa_similarity_content.npy')
    return np.load(file_path)