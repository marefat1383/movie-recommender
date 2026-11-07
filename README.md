# Movie Recommender

A small educational AI project that recommends movies with similar genres using TF-IDF vectors and cosine similarity.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run

```bash
python movie_recommender.py "space adventure"
```

## Test

```bash
python -m unittest test_movie_recommender.py
```

The catalog is intentionally tiny and embedded in the source so the project stays self-contained.
