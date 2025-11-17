# OrientadorCarreiras — Sistema de orientação de carreiras (Python)

Projeto didático em Python (orientado a objetos) que organiza e analisa perfis profissionais do futuro e gera recomendações personalizadas.

## Como usar rápido
1. Extraia o zip e entre na pasta `orientadorcarreiras`.
2. (Opcional) Crie um ambiente virtual: `python -m venv venv` e ative-o.
3. Instale dependências (nenhuma por padrão): `pip install -r requirements.txt`
4. Execute a aplicação CLI: `python main.py`

## Estrutura de arquivos
- `main.py` — ponto de entrada (CLI)
- `models.py` — classes: Competencia, Perfil, Carreira
- `recommender.py` — lógica de recomendação
- `storage.py` — salvar/carregar perfis em JSON
- `utils.py` — perfis de exemplo
- `data/` — perfis salvos (profiles.json)
- `README.md` — este arquivo
- `LICENSE` — MIT
