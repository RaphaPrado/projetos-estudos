# 📊 Dados

Exercícios e projetos de análise de dados.

## Asimov Academy

Organizado por trilha → curso → aula:
```
asimov-academy/
└── <trilha>/
    └── <curso>/
        ├── 01-nome-da-aula.ipynb
        └── 02-nome-da-aula.py
```

| Trilha / Curso | Conteúdo | Status |
|---|---|---|
| | | |

## Como rodar

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## ⚠️ Datasets

- Arquivos acima de ~50 MB **não sobem** (limite do GitHub é 100 MB). Coloque datasets grandes em `data/raw/` (ignorada no `.gitignore`) e deixe no README o link de onde baixar.
- Antes de commitar notebook, limpe outputs pesados (`Kernel > Restart & Clear Output`).
