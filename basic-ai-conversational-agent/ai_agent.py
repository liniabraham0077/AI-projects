# ai_agent.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data import qa_pairs

def get_best_answer(user_question):
    questions = [item["question"] for item in qa_pairs]
    
    # Add the user's question to the list for vectorization
    all_questions = questions + [user_question]
    
    print(f"all_questions ${all_questions}")

    # Convert text to TF-IDF features
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_questions)

    # Compute similarity between user's question and all dataset quepstions
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    print(f"similarity_scores ${similarity_scores}")

    # Get the index of the most similar question
    best_match_index = similarity_scores.argmax()
    
    print(f"best_match_index ${best_match_index}")
    
    return qa_pairs[best_match_index]["answer"]