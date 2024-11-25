from flask import Blueprint
from controllers.srController import getRecomendations, search_jobs_title, obtain_job_by_id, get_first_jobs

def setupRoutesSr(app):
    bp = Blueprint('recommend', __name__)

    # Rutas para CRUD de items productos
    bp.route('/recommend/<int:id>', methods=['GET'])(getRecomendations)
    bp.route('/job/<int:id>', methods=['GET'])(obtain_job_by_id)
    bp.route('/jobs/<string:input>', methods=['get'])(search_jobs_title)
    bp.route('/jobs', methods=['GET'])(get_first_jobs)
    
    app.register_blueprint(bp)