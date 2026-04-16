from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_ats_score(resume_text: str, job_description: str):
    
    texts = [resume_text, job_description]

    # Convert text to vectors
    vectorizer = CountVectorizer().fit_transform(texts)
    vectors = vectorizer.toarray()

    # Compute cosine similarity
    similarity = cosine_similarity([vectors[0]], [vectors[1]])[0][0]

    score = round(similarity * 100, 2)

    # Keyword extraction
    job_keywords = set(job_description.lower().split())
    resume_words = set(resume_text.lower().split())

    matched = job_keywords.intersection(resume_words)
    missing = job_keywords - resume_words

    return {
        "ats_score": score,
        "matched_keywords": list(matched)[:20],
        "missing_keywords": list(missing)[:20]
    }