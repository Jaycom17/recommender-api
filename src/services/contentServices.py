import pandas as pd

def get_content_by_id(id, lsa, df):
    # Get index of the job that matches the title
    idx = df[df['job_id'] == id].index[0]

    # Get pairwise similarity scores of all jobs with that job
    sim_scores = list(enumerate(lsa[idx]))

    # Sort the jobs based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the top-n most similar jobs (excluding itself)
    sim_scores = sim_scores[1:11]

    # Get the jobs indices
    jobs_indices = [i[0] for i in sim_scores]

    # Return the top-n most similar jobs
    result = pd.DataFrame(df['job_id'].iloc[jobs_indices])
    result['title'] = df['title']
    result['similarity_content'] = [i[1] for i in sim_scores]
    
    return result