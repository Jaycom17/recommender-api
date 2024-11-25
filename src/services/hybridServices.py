from services.contextServices import get_context_by_id
from services.contentServices import get_content_by_id
from services.knnServices import get_knn_by_id

import pandas as pd

def get_hybrid_by_id(id, app):
    
    weights = {"content": 0.4, "context": 0.1, "knn": 0.5}
    
    df = app.data_frame
    
    rec_content = get_content_by_id(id, app.lsa_content, df)[["job_id", "similarity_content"]]
    rec_context = get_context_by_id(id, app.lsa_context, df)[["job_id", "similarity_context"]]
    rec_knn = get_knn_by_id(id, app.knn_model, df, app.vectorizer)[["job_id", "similarity_knn"]]

    result = pd.merge(rec_content, rec_context, on="job_id", how="outer").fillna(0)
    result = pd.merge(result, rec_knn, on="job_id", how="outer").fillna(0)

    result["similarity_hybrid"] = weights["content"] * result["similarity_content"] + weights["context"] * result["similarity_context"] + weights["knn"] * result["similarity_knn"]

    result["title"] = df[df["job_id"].isin(result["job_id"].to_list())]["title"].values
    
    result["url"] = df[df["job_id"].isin(result["job_id"].to_list())]["job_posting_url"].values

    result = result.sort_values(by="similarity_hybrid", ascending=False)

    return result.to_dict(orient="records")