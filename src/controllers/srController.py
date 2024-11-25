from flask import request, jsonify, current_app as app

from services.hybridServices import get_hybrid_by_id
from services.dataframeServices import get_job_by_id, search_jobs, get_jobs

def getRecomendations(id):
    
    return get_hybrid_by_id(id, app), 200

def obtain_job_by_id(id):
        
    return get_job_by_id(id, app), 200

def search_jobs_title(input):
        
    return search_jobs(input, app), 200

def get_first_jobs():
    
    return get_jobs(app), 200