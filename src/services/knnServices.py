import pandas as pd

def get_knn_by_id(id, model, df, vectorizer):
    query = df[df["job_id"] == id]["content"]

    query_vector = vectorizer.transform(query)

    distances, indices = model.kneighbors(query_vector)

    result = pd.DataFrame(df['job_id'].iloc[indices[0]])

    result['similarity_knn'] = 1 - distances[0]

    result = result[result['job_id'] != id]

    result["title"] = df[df["job_id"].isin(result["job_id"].to_list())]["title"].values

    return result