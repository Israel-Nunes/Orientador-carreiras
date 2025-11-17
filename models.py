from typing import Dict, List

class Competencia:
    def __init__(self, nome: str, tipo: str, score: float):
        self.nome = nome
        self.tipo = tipo  # 'tecnica' ou 'comportamental'
        self.score = float(score)

    def to_dict(self):
        return {"nome": self.nome, "tipo": self.tipo, "score": self.score}


class Perfil:
    def __init__(self, nome: str, competencias: List[Competencia] = None):
        self.nome = nome
        self.competencias = competencias or []

    def add_competencia(self, comp: Competencia):
        self.competencias.append(comp)

    def get_scores(self) -> Dict[str, float]:
        tipos = {"tecnica": [], "comportamental": []}
        for c in self.competencias:
            tipos[c.tipo].append(c.score)
        return {
            "media_tecnica": sum(tipos["tecnica"]) / len(tipos["tecnica"]) if tipos["tecnica"] else 0,
            "media_comportamental": sum(tipos["comportamental"]) / len(tipos["comportamental"]) if tipos["comportamental"] else 0,
            "por_competencia": {c.nome: c.score for c in self.competencias}
        }

    def to_dict(self):
        return {"nome": self.nome, "competencias": [c.to_dict() for c in self.competencias]}


class Carreira:
    def __init__(self, nome: str, requisitos: Dict[str, float], descricao: str = ""):
        self.nome = nome
        self.requisitos = requisitos
        self.descricao = descricao

    def to_dict(self):
        return {"nome": self.nome, "requisitos": self.requisitos, "descricao": self.descricao}
