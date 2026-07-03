# Decodelabs-internship-project3
🎯 AI Career Path Recommendation System

📌 Project Overview

The AI Career Path Recommendation System is a simple machine learning project that recommends the most suitable career paths based on a user's skills. It uses TF-IDF Vectorization and Cosine Similarity from Scikit-learn to compare the user's skill set with predefined job role skill profiles and suggests the top three matching careers.

This project demonstrates the practical application of Natural Language Processing (NLP) techniques in career recommendation systems.

---

🚀 Features

- Accepts 3 or more user skills as input.
- Validates user input before processing.
- Converts skills into numerical vectors using TF-IDF Vectorizer.
- Calculates similarity using Cosine Similarity.
- Recommends the Top 3 most suitable career paths.
- Displays a match percentage for each recommended role.
- Beginner-friendly and easy to understand.

---

🛠️ Technologies Used

- Python
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

---

📚 Job Roles Included

The system currently recommends careers from the following domains:

- Data Scientist
- DevOps Engineer
- Backend Developer
- Frontend Developer
- Cloud Architect
- Machine Learning Engineer
- Cybersecurity Analyst
- Mobile App Developer

---

📥 Input

The user enters at least three skills, separated by commas.

Example:

Python, SQL, Machine Learning

---

📤 Sample Output

🎯 Top 3 Recommended Career Paths

1. Data Scientist → Match Score: 91.24%
2. Machine Learning Engineer → Match Score: 84.76%
3. Backend Developer → Match Score: 52.18%

✅ Recommendation Complete!

---

⚙️ How It Works

1. The user enters their skills.
2. The program validates that at least three skills are provided.
3. User skills are converted into a single text profile.
4. TF-IDF Vectorizer transforms both job descriptions and user skills into numerical vectors.
5. Cosine Similarity compares the user's profile with every job role.
6. The system ranks all job roles by similarity score.
7. The top three most relevant career paths are displayed.

---

📦 Installation

Install the required library:

pip install scikit-learn

---

▶️ How to Run

python project_2.py

Enter your skills when prompted, separated by commas.

---

📁 Project Structure

project/
│── project_2.py
│── README.md

---

🎯 Learning Outcomes

Through this project, you will learn:

- Text preprocessing
- TF-IDF Vectorization
- Cosine Similarity
- Basic Natural Language Processing (NLP)
- User input validation
- Career recommendation logic using Machine Learning

---

🔮 Future Improvements

- Add more job roles and skill datasets.
- Build a graphical user interface (GUI).
- Develop a web application using Flask or Django.
- Recommend online courses based on missing skills.
- Store job profiles in a database.
- Integrate real-world job listings using APIs.

---

👩‍💻 Author

Qaswa Arshad

AI & Data Science Student | Aspiring Machine Learning Engineer

---

📄 License

This project is developed for educational and learning purposes.
