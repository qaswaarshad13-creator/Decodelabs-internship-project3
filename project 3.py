from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

job_roles = {
    "Data Scientist": "python sql machine learning data analysis statistics pandas",
    "DevOps Engineer": "aws docker kubernetes ci cd automation cloud linux",
    "Backend Developer": "java python sql apis databases spring rest",
    "Frontend Developer": "html css javascript react ui design responsive",
    "Cloud Architect": "aws azure cloud computing automation networking security",
    "Machine Learning Engineer": "python machine learning tensorflow deep learning neural networks",
    "Cybersecurity Analyst": "network security firewalls encryption penetration testing linux",
    "Mobile App Developer": "java kotlin swift flutter mobile ui android ios"
}
print("Apni 3 (ya zyada) skills likho, comma (,) se separate karke.")
print("Misaal: Python, Cloud, Automation\n")
user_input = input("Aapki Skills: ")
user_skills_list = [skill.strip() for skill in user_input.split(",") if skill.strip() != ""]
if len(user_skills_list) < 3:
    print("\n⚠️ Kam az kam 3 skills likhna zaroori hai. Dobara try karo.")
    exit()
user_profile_text = " ".join(user_skills_list).lower()
job_titles = list(job_roles.keys())
job_descriptions = list(job_roles.values())
all_documents = job_descriptions + [user_profile_text]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_documents)
user_vector = tfidf_matrix[-1]
job_vectors = tfidf_matrix[:-1]
similarity_scores = cosine_similarity(user_vector, job_vectors)[0]
results = list(zip(job_titles, similarity_scores))
results.sort(key=lambda x: x[1], reverse=True)
top_matches = results[:3]
print("\n🎯 Aapki skills ke mutabiq Top 3 Recommended Career Paths:\n")
for rank, (role, score) in enumerate(top_matches, start=1):
    match_percentage = round(score * 100, 2)
    print(f"{rank}. {role}  →  Match Score: {match_percentage}%")
print("\n✅ Recommendation complete!")