import json
from models import Perfil, Competencia
from typing import List

def save_profiles(path: str, profiles: List[Perfil]):
    with open(path, "w", encoding="utf-8") as f:
        json.dump([p.to_dict() for p in profiles], f, ensure_ascii=False, indent=2)

def load_profiles(path: str) -> List[Perfil]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        profiles = []
        for p in data:
            comps = [Competencia(c["nome"], c["tipo"], c["score"]) for c in p.get("competencias", [])]
            profiles.append(Perfil(p["nome"], comps))
        return profiles
    except FileNotFoundError:
        return []
