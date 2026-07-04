import json
from pathlib import Path

GRAPH_PATH = (
    Path(__file__).parent.parent
    / "data"
    / "technology_graph.json"
)


PRIORITY_MAP = {
    5: "Critical",
    4: "High",
    3: "Medium",
    2: "Low",
    1: "Low"
}


DIFFICULTY_MAP = {

    # Languages
    "Python": "Beginner",
    "Java": "Intermediate",
    "C++": "Intermediate",
    "Go": "Intermediate",
    "JavaScript": "Beginner",
    "TypeScript": "Intermediate",

    # Frameworks
    "Flask": "Beginner",
    "FastAPI": "Intermediate",
    "Django": "Intermediate",
    "Node.js": "Intermediate",
    "React": "Intermediate",
    "Angular": "Intermediate",
    "Vue": "Intermediate",
    "Next.js": "Advanced",

    # Cloud / DevOps
    "Docker": "Intermediate",
    "AWS": "Intermediate",
    "Kubernetes": "Advanced",
    "Redis": "Intermediate",
    "NGINX": "Intermediate",

    # Databases
    "SQL": "Beginner",
    "PostgreSQL": "Intermediate",

    # ML
    "NumPy": "Beginner",
    "Pandas": "Beginner",
    "Scikit-learn": "Intermediate",
    "TensorFlow": "Advanced",
    "PyTorch": "Advanced",
    "MLflow": "Advanced",
    "ONNX": "Advanced",
    "Hugging Face": "Advanced",

    # Data Science
    "Tableau": "Intermediate",
    "Power BI": "Intermediate",
    "Spark": "Advanced",
    "Airflow": "Advanced"
}


TIME_MAP = {
    "Beginner": "1-2 weeks",
    "Intermediate": "2-4 weeks",
    "Advanced": "4-8 weeks"
}


with open(GRAPH_PATH, encoding="utf-8") as file:
    graph = json.load(file)


for domain in graph.values():

    for section in domain.values():

        for skill, details in section.items():

            weight = details["weight"]

            priority = PRIORITY_MAP[weight]

            difficulty = DIFFICULTY_MAP.get(
                skill,
                "Intermediate"
            )

            details["priority"] = priority
            details["difficulty"] = difficulty
            details["estimated_learning_time"] = TIME_MAP[difficulty]


with open(GRAPH_PATH, "w", encoding="utf-8") as file:
    json.dump(graph, file, indent=2)

print("Technology graph enriched successfully.")