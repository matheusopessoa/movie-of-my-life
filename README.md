# Movie of My Life - API de Recomendação de Filmes

## 📝 Sobre o Projeto

O Movie of My Life é uma API inovadora que utiliza inteligência artificial para recomendar filmes baseados na história de vida das pessoas. A plataforma combina psicanálise e cinema para criar recomendações altamente personalizadas, analisando profundamente a história do usuário, suas emoções, jornada pessoal e contexto.

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- Flasgger (Swagger UI)
- GPT-4
- Flask-CORS

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd movie-of-my-life
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
# ou
.\env\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Executando o Projeto

1. Inicie o servidor:
```bash
python app.py
```

2. Acesse a documentação da API:
```
http://localhost:5000/apidocs/
```

## 📚 Endpoints Disponíveis

### 1. Recomendação Gratuita
- **Endpoint**: `/getFreeMovie`
- **Método**: GET
- **Parâmetros**:
  - `story` (string): História de vida do usuário
  - `language` (string): Idioma da resposta (pt, en, es)

### 2. Recomendação Premium
- **Endpoint**: `/getPaidMovie`
- **Método**: GET
- **Parâmetros**:
  - `story` (string): História de vida do usuário
  - `emotion` (string): Emoção predominante na história
  - `journey` (string): Jornada pessoal do usuário
  - `favGenre` (string): Gênero de filme favorito
  - `age` (string): Idade do usuário
  - `cenaryOfLife` (string): Cenário de vida atual
  - `endOfLife` (string): Perspectiva sobre o fim da vida
  - `keyWords` (string): Palavras-chave importantes
  - `language` (string): Idioma da resposta (pt, en, es)
  - `gender_identity` (string): Identidade de gênero do usuário

## 📋 Versões Disponíveis

### Versão Gratuita
- Recomendação básica baseada na história do usuário
- Análise simples do contexto

### Versão Premium
- Análise profunda incluindo emoções
- Jornada pessoal
- Preferências
- Contexto detalhado
- Explicação da conexão entre o filme e a história
- Elementos ressonantes

## 🔐 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
OPENAI_API_KEY=sua_chave_api_aqui
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Contribuição

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit das suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📧 Contato

Movie of My Life Team - contato@movieofmylife.com 

## 🚀 Deploy no Railway

1. Crie uma conta no [Railway](https://railway.app/)
2. Instale o [Railway CLI](https://docs.railway.app/develop/cli)
3. Faça login no Railway:
```bash
railway login
```
4. Inicialize o projeto:
```bash
railway init
```
5. Configure as variáveis de ambiente no dashboard do Railway:
   - `OPENAI_API_KEY`: Sua chave da API OpenAI
6. Faça o deploy:
```bash
railway up
```

O Railway irá automaticamente:
- Detectar o `Procfile`
- Instalar as dependências do `requirements.txt`
- Iniciar a aplicação usando o Gunicorn 