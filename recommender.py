from models import Perfil, Carreira
from typing import List, Tuple

class Recommender:
    def __init__(self, careers: List[Carreira]):
        self.careers = careers

    def score_profile_for_career(self, perfil: Perfil, carreira: Carreira) -> float:
        perfil_dict = {k: v for k, v in perfil.get_scores()["por_competencia"].items()}
        total_weight = 0.0
        accumulated = 0.0
        for comp, weight in carreira.requisitos.items():
            total_weight += weight
            perfil_score = perfil_dict.get(comp, 0)
            accumulated += (perfil_score / 10.0) * weight
        return (accumulated / total_weight) if total_weight > 0 else 0.0

    def recommend(self, perfil: Perfil, top_n: int = 3) -> List[Tuple[Carreira, float, List[str]]]:
        scored: List[Tuple[Carreira, float]] = []
        for c in self.careers:
            s = self.score_profile_for_career(perfil, c)
            scored.append((c, s))
        scored.sort(key=lambda x: x[1], reverse=True)
        results = []
        for carreira, s in scored[:top_n]:
            faltas = []
            perfil_dict = {k: v for k, v in perfil.get_scores()["por_competencia"].items()}
            for comp, weight in carreira.requisitos.items():
                score = perfil_dict.get(comp, 0)
                if score < 6.0:
                    faltas.append(f"{comp} ({score}/10)")
            results.append((carreira, round(s, 3), faltas))
        return results


def sample_careers() -> List[Carreira]:
    careers = [
        Carreira("Engenheiro de Machine Learning", {"Lógica": 0.2, "Matemática": 0.2, "Programação": 0.3, "Criatividade": 0.1, "Comunicação": 0.2}, descricao="Modelagem e implementação de modelos ML"),
        Carreira("Product Manager", {"Comunicação": 0.25, "Colaboração": 0.2, "Criatividade": 0.2, "Visão de Produto": 0.25, "Adaptabilidade": 0.1}, descricao="Lidera desenvolvimento de produtos"),
        Carreira("UX Designer", {"Criatividade": 0.3, "Empatia": 0.3, "Pesquisa": 0.2, "Comunicação": 0.2}, descricao="Pesquisa e design de experiências"),
        Carreira("DevOps / SRE", {"Programação": 0.2, "Infraestrutura": 0.3, "Automação": 0.3, "Resiliência": 0.2}, descricao="Operação e confiabilidade de sistemas"),
    ]
    return careers
