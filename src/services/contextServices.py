def get_context_by_id(id, lsa, df):
    # Encuentra el índice del trabajo en el DataFrame
    job_idx = df[df['job_id'] == id].index[0]

    # Extrae las similitudes para el trabajo dado
    similarity_scores = lsa[job_idx]

    # Ordena los trabajos por similitud (mayor a menor)
    similar_jobs_indices = similarity_scores.argsort()[::-1]

    # Filtra para excluir el trabajo original
    similar_jobs_indices = [idx for idx in similar_jobs_indices if idx != job_idx]

    # Selecciona los índices de los top_n trabajos más similares
    top_job_indices = similar_jobs_indices[:10]

    # Crear DataFrame con las recomendaciones y sus grados de similitud
    recommendations = df.iloc[top_job_indices][['job_id', 'title']].copy()
    
    recommendations['similarity_context'] = similarity_scores[top_job_indices]

    return recommendations