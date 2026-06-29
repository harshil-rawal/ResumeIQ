from utils.preprocessing import preprocess_text

text = """
Harshil Rawal

Python Developer

Skills:
Python, Flask, SQL, Docker, Git, NumPy, Pandas

Experience:
Worked for 2 years developing Machine Learning projects using TensorFlow 2.18.

Education:
B.Tech Mechanical Engineering
"""

tokens = preprocess_text(text)

print(tokens)