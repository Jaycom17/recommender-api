import pandas as pd

def get_job_by_id(id, app):
    df = app.data_frame
    
    result = df[df["job_id"] == id]
    
    result = result[["job_id", "title", "job_description", "job_posting_url"]]
    
    return result.to_dict(orient="records")

def search_jobs(query, app):
    df = app.data_frame
    
    result = df[df["job_description"].str.contains(query, case=False) | df["title"].str.contains(query, case=False)]
    
    result = result[["job_id", "title", "job_description", "job_posting_url"]].head(20)
    
    return result.to_dict(orient="records")

def get_jobs(app):
    
    df = app.data_frame
    
    df = df[["job_id", "title", "job_description", "job_posting_url"]].head(20)
    
    return df.to_dict(orient="records")
    