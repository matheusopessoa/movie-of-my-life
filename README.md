# Movie of My Life - Backend

API backend construída com Fastify e TypeScript.

## Requisitos

- Node.js 18 ou superior
- npm ou yarn

## Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
npm install
```

## Executando o projeto

Para desenvolvimento:
```bash
npm run dev
```

Para produção:
```bash
npm run build
npm start
```

O servidor estará rodando em `http://localhost:3333` 

## Configuração da API do ChatGPT

Para utilizar a API do ChatGPT, você precisa configurar a variável de ambiente `OPENAI_API_KEY`. Você pode fazer isso adicionando a seguinte linha ao seu arquivo `.env`:

```
OPENAI_API_KEY=sua_chave_aqui
```

Certifique-se de substituir `sua_chave_aqui` pela sua chave de API real. 