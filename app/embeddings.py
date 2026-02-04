from ai_resume_matcher.app.db import engine
from functools import lru_cache
import numpy as np
from sentence_transformers import SentenceTransformer


@lru_cache(maxsize=1)
def get_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text: str) -> np.ndarray:
    model = get_model()
    return model.encode([text], normalize_embeddings=True)[0]


def serialize_embedding(emb: np.ndarray) -> bytes:
    return emb.astype(np.float32).tobytes()


def deserialize_embedding(emb_bytes: bytes) -> np.ndarray:
    return np.frombuffer(emb_bytes, dtype=np.float32)
def embed(text: str):
    return get_embedding(text).reshape(1, -1)
