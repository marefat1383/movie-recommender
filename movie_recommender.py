import argparse

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

MOVIES = [
    ("Galactic Voyage", "space adventure exploration"),
    ("Ocean Secrets", "ocean mystery exploration"),
    ("Robot Rebellion", "robot science fiction action"),
    ("The Last Detective", "city mystery detective"),
    ("Jungle Quest", "jungle adventure exploration"),
    ("Future Minds", "science fiction robot mystery"),
]


def recommend(query: str, limit: int = 3) -> list[str]:
    if not query.strip():
        raise ValueError("Query cannot be empty")
    descriptions = [description for _, description in MOVIES]
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(descriptions + [query])
    scores = cosine_similarity(matrix[-1], matrix[:-1]).ravel()
    ranked = scores.argsort()[::-1][:limit]
    return [MOVIES[index][0] for index in ranked]


def main() -> None:
    parser = argparse.ArgumentParser(description="Recommend similar movies.")
    parser.add_argument("query", nargs="+", help="Genres or themes")
    args = parser.parse_args()
    print("Recommendations:")
    for title in recommend(" ".join(args.query)):
        print(f"- {title}")


if __name__ == "__main__":
    main()
