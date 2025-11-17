from models import Competencia, Perfil

def sample_profile() -> Perfil:
    p = Perfil("Ana Silva")
    dados = [
        ("Lógica", "tecnica", 8),
        ("Programação", "tecnica", 7),
        ("Matemática", "tecnica", 6),
        ("Criatividade", "comportamental", 8),
        ("Comunicação", "comportamental", 6),
        ("Colaboração", "comportamental", 7),
    ]
    for nome, tipo, score in dados:
        p.add_competencia(Competencia(nome, tipo, score))
    return p
