import pandas as pd
import os

def getDataFrame():
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Ruta del archivo actual
    file_path = os.path.join(current_dir, '..', 'data', 'files', 'job_posting_df.csv')
    return pd.read_csv(file_path)
