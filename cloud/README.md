# ☁️ Cloud

Estudos de AWS e Azure. ⚪ **Planejado** — começa depois das trilhas atuais.

```
cloud/
├── aws/
│   ├── anotacoes/          # resumos de serviços (EC2, S3, IAM, Lambda...)
│   └── labs/               # exercícios práticos, scripts, IaC
└── azure/
    ├── anotacoes/
    └── labs/
```

| Plataforma | Tema | Status |
|---|---|---|
| AWS | | ⚪ |
| Azure | | ⚪ |

## 🔐 Regra de ouro

**Nunca** commitar chaves de acesso, `credentials`, `.env`, arquivos `.tfstate` ou `.pem`. Já estão no `.gitignore`, mas confira o `git status` antes de todo commit. Chave vazada em repositório público é usada por bots em minutos e vira cobrança na conta.
