from models import Competencia, Perfil
from recommender import Recommender, sample_careers
from storage import save_profiles, load_profiles
from utils import sample_profile

def input_float(prompt, minv=0, maxv=10):
    while True:
        try:
            v = float(input(prompt))
            if v < minv or v > maxv:
                print(f"Digite um valor entre {minv} e {maxv}.")
                continue
            return v
        except ValueError:
            print("Valor inválido. Tente novamente.")

def cadastrar_perfil():
    nome = input("Nome do candidato: ")
    perfil = Perfil(nome)
    print("Agora vamos cadastrar competências. Digite '-' para parar.")
    while True:
        comp = input("Nome da competência (ex: Programação, Comunicação) ou '-' para sair: ")
        if comp.strip() == "-":
            break
        tipo = input("Tipo ('tecnica' ou 'comportamental'): ").strip().lower()
        if tipo not in ("tecnica", "comportamental"):
            print("Tipo inválido. Use 'tecnica' ou 'comportamental'.")
            continue
        score = input_float("Nota (0-10): ")
        perfil.add_competencia(Competencia(comp, tipo, score))
    return perfil

def main():
    os_path = "data/profiles.json"
    profiles = load_profiles(os_path)
    careers = sample_careers()
    recommender = Recommender(careers)

    while True:
        print("\n=== OrientadorCarreiras ===")
        print("1) Cadastrar perfil")
        print("2) Mostrar perfis")
        print("3) Analisar perfil")
        print("4) Exemplo: carregar perfil de amostra")
        print("5) Salvar perfis")
        print("6) Sair")
        opt = input("Escolha: ")
        if opt == "1":
            p = cadastrar_perfil()
            profiles.append(p)
            print(f"Perfil {p.nome} cadastrado.")
        elif opt == "2":
            if not profiles:
                print("Nenhum perfil cadastrado.")
            for i, p in enumerate(profiles):
                print(f"[{i}] {p.nome}")
        elif opt == "3":
            idx = int(input("Índice do perfil: "))
            perfil = profiles[idx]
            print("Scores:", perfil.get_scores())
            recs = recommender.recommend(perfil, top_n=3)
            print("Recomendações:")
            for carreira, score, faltas in recs:
                print(f"- {carreira.nome} (compatibilidade: {score*100:.1f}%)")
                if faltas:
                    print("  -> Áreas a melhorar:", ", ".join(faltas))
        elif opt == "4":
            profiles.append(sample_profile())
            print("Perfil de amostra adicionado.")
        elif opt == "5":
            save_profiles(os_path, profiles)
            print(f"Perfis salvos em {os_path}")
        elif opt == "6":
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    main()
