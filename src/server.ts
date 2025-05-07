import Fastify, { FastifyRequest, FastifyReply } from 'fastify'
import cors from '@fastify/cors'
import swagger from '@fastify/swagger'
import swaggerUi from '@fastify/swagger-ui'
import { generateResponse } from './openai'

const app = Fastify({
  logger: true
})

// Configuração do Swagger
app.register(swagger, {
  openapi: {
    info: {
      title: '🎬 Movie of My Life API',
      description: `# Movie of My Life API

API que sugere filmes baseados na história de vida das pessoas, usando inteligência artificial para encontrar o filme perfeito que ressoa com sua história.

## 🚀 Como Usar

1. Faça uma requisição POST para \`/generate\`
2. Envie um JSON com a história de vida no campo \`text\`
3. A história pode ser em português, inglês ou espanhol
4. A resposta será o título de um filme no mesmo idioma da história

## 📝 Endpoint da API

\`\`\`http
POST http://localhost:3321/generate
Content-Type: application/json

{
  "text": "Sua história de vida aqui..."
}
\`\`\`

## 📥 Resposta da API

\`\`\`json
{
  "movie": "Título do Filme"
}
\`\`\`

## 🎨 Prompt para IA Criar Frontend

Crie um frontend para a aplicação "Movie of My Life" com as seguintes características:

### 🎯 Funcionalidades
1. Interface moderna e intuitiva usando React/Next.js
2. Campo de texto grande para o usuário escrever sua história de vida
3. Suporte para português, inglês e espanhol
4. Botão para enviar a história
5. Exibição elegante do filme sugerido

### 🎨 Design
1. Animações suaves durante o carregamento
2. Design responsivo para mobile e desktop
3. Tema escuro/claro
4. Mensagens de erro amigáveis
5. Exemplos de histórias em cada idioma

### 🔌 Integração com API
- **Endpoint**: \`POST http://localhost:3321/generate\`
- **Body**: \`{ "text": "história do usuário" }\`
- **Resposta**: \`{ "movie": "título do filme" }\`

Use Tailwind CSS para estilização e mantenha o código limpo e bem documentado.

## 💻 Exemplos de Uso

### cURL
\`\`\`bash
curl -X POST http://localhost:3321/generate \\
  -H "Content-Type: application/json" \\
  -d '{"text": "Nasci em uma família simples no interior..."}'
\`\`\`

### JavaScript/Fetch
\`\`\`javascript
const response = await fetch('http://localhost:3321/generate', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    text: "Nasci em uma família simples no interior..."
  })
});
const data = await response.json();
\`\`\`

### Python/Requests
\`\`\`python
import requests

response = requests.post(
    'http://localhost:3321/generate',
    json={
        'text': 'Nasci em uma família simples no interior...'
    }
)
data = response.json()
\`\`\`

## ⚠️ Limitações
- O texto da história deve ter no máximo 100 palavras
- A resposta será sempre o título do filme, sem explicações adicionais

## 📞 Suporte
Em caso de dúvidas ou problemas, entre em contato com nossa equipe de suporte.`,
      version: '1.0.0',
      contact: {
        name: 'Suporte',
        email: 'suporte@movieofmylife.com'
      }
    },
    servers: [
      {
        url: 'http://localhost:3321',
        description: 'Servidor de desenvolvimento'
      }
    ],
  }
})

app.register(swaggerUi, {
  routePrefix: '/docs',
  uiConfig: {
    docExpansion: 'full',
    deepLinking: false
  },
  staticCSP: true
})

// Registra o plugin CORS
app.register(cors, {
  origin: true
})

// Rota de teste
app.get('/', {
  schema: {
    description: 'Rota de teste para verificar se a API está funcionando',
    tags: ['health'],
    response: {
      200: {
        description: 'Resposta bem-sucedida',
        type: 'object',
        properties: {
          hello: { type: 'string' }
        }
      }
    }
  }
}, async (request: FastifyRequest, reply: FastifyReply) => {
  return { hello: 'world' }
})

// Rota para gerar resposta do GPT
app.post('/generate', {
  schema: {
    description: '🎬 Endpoint para gerar sugestões de filmes baseadas na história de vida do usuário',
    tags: ['movie'],
    body: {
      type: 'object',
      required: ['text'],
      properties: {
        text: {
          type: 'string',
          description: '📝 História de vida do usuário (pode ser em português, inglês ou espanhol)',
          minLength: 1,
          maxLength: 1000,
          examples: [
            {
              summary: '🇧🇷 Exemplo em Português',
              value: "Nasci em uma família simples no interior. Sempre sonhei em ser professor, mas as dificuldades eram muitas. Estudei à noite enquanto trabalhava de dia. Hoje sou diretor de uma escola pública."
            },
            {
              summary: '🇺🇸 Exemplo em Inglês',
              value: "I was born in a small town. I always dreamed of becoming a teacher, but the difficulties were many. I studied at night while working during the day. Today I am the principal of a public school."
            },
            {
              summary: '🇪🇸 Exemplo em Espanhol',
              value: "Nací en un pequeño pueblo. Siempre soñé con ser profesor, pero las dificultades eran muchas. Estudié por la noche mientras trabajaba durante el día. Hoy soy director de una escuela pública."
            }
          ]
        }
      }
    },
    response: {
      200: {
        description: '✅ Filme sugerido com sucesso',
        type: 'object',
        properties: {
          movie: {
            type: 'string',
            description: '🎬 Título do filme no mesmo idioma da história',
            examples: [
              {
                summary: '🇧🇷 Exemplo em Português',
                value: "À Procura da Felicidade"
              },
              {
                summary: '🇺🇸 Exemplo em Inglês',
                value: "The Pursuit of Happyness"
              },
              {
                summary: '🇪🇸 Exemplo em Espanhol',
                value: "En Busca de la Felicidad"
              }
            ]
          }
        }
      },
      400: {
        description: '❌ Erro de validação',
        type: 'object',
        properties: {
          error: {
            type: 'string',
            description: '⚠️ Mensagem de erro de validação',
            example: 'O campo text é obrigatório'
          }
        }
      },
      500: {
        description: '❌ Erro interno do servidor',
        type: 'object',
        properties: {
          error: {
            type: 'string',
            description: '⚠️ Mensagem de erro',
            example: 'Erro ao gerar resposta'
          }
        }
      }
    }
  }
}, async (request: FastifyRequest<{
  Body: { text: string }
}>, reply: FastifyReply) => {
  try {
    const { text } = request.body
    const response = await generateResponse(text)
    return reply.send(response)
  } catch (error) {
    app.log.error(error)
    return reply.status(500).send({ error: 'Erro ao gerar resposta' })
  }
})

// Inicia o servidor
const start = async () => {
  try {
    const port = process.env.PORT ? parseInt(process.env.PORT, 10) : 3321
    await app.listen({ port, host: '0.0.0.0' })
    app.log.info(`Documentação disponível em: http://localhost:${port}/docs`)
  } catch (err) {
    app.log.error(err)
    process.exit(1)
  }
}

start() 