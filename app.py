from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from flasgger import Swagger
import yaml
from free_prompts import generate_free_prompt, generate_free_system_message
from premium_prompts import generate_premium_prompt, generate_premium_system_message
from open_ai import generate_free_response, generate_premium_response

app = Flask(__name__)
CORS(app)

swagger_config = {
    "swagger": "2.0",
    "info": {
        "title": "Movie of My Life API",
        "description": "API de Recomendação de Filmes Personalizada",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": ["http"],
    "host": "localhost:5000",
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
    "headers": []
}
swagger = Swagger(app, config=swagger_config)

@app.route('/')
def index():
    return redirect('/apidocs/')

@app.route('/getFreeMovie')
def getfreeMovie():
    #swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===
    """
    Recomendação Gratuita de Filme
    ---
    parameters:
      - name: story
        in: query
        type: string
        required: true
        description: História de vida do usuário
      - name: language
        in: query
        type: string
        enum: [pt, en, es]
        required: true
        description: Idioma da resposta (pt=Português, en=Inglês, es=Espanhol)
    responses:
      200:
        description: Recomendação gerada com sucesso
        schema:
          type: object
          properties:
            movie:
              type: string
              description: Nome do filme recomendado
    """
    #swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===

    story = request.args.get('story')
    language = request.args.get('language')
    prompt = generate_free_prompt(story, language)
    system_message = generate_free_system_message(language)
    movie = generate_free_response(system_message, prompt)
    return jsonify({'movie': movie})

@app.route('/getPaidMovie')
def getpaidMovie():
    #swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===
    """
    Recomendação Premium de Filme
    ---
    parameters:
      - name: story
        in: query
        type: string
        required: true
        description: História de vida do usuário
      - name: emotion
        in: query
        type: string
        required: true
        description: Emoção predominante na história
      - name: journey
        in: query
        type: string
        required: true
        description: Jornada pessoal do usuário
      - name: favGenre
        in: query
        type: string
        required: true
        description: Gênero de filme favorito
      - name: age
        in: query
        type: string
        required: true
        description: Idade do usuário
      - name: cenaryOfLife
        in: query
        type: string
        required: true
        description: Cenário de vida atual
      - name: endOfLife
        in: query
        type: string
        required: true
        description: Perspectiva sobre o fim da vida
      - name: keyWords
        in: query
        type: string
        required: true
        description: Palavras-chave importantes
      - name: language
        in: query
        type: string
        enum: [pt, en, es]
        required: true
        description: Idioma da resposta (pt=Português, en=Inglês, es=Espanhol)
      - name: gender_identity
        in: query
        type: string
        required: true
        description: Identidade de gênero do usuário
    responses:
      200:
        description: Recomendação premium gerada com sucesso
        schema:
          type: object
          properties:
            movie_name:
              type: string
              description: Nome do filme recomendado
            movie_year:
              type: string
              description: Ano do filme
            connection_explanation:
              type: string
              description: Explicação detalhada da conexão entre o filme e a história
            resonant_elements:
              type: array
              items:
                type: string
              description: Lista de elementos que ressoam com a história
    """
    #swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===#swagger===
    story = request.args.get('story')
    emotion = request.args.get('emotion')
    journey = request.args.get('journey')
    favGenre = request.args.get('favGenre')
    age = request.args.get('age')
    cenaryOfLife = request.args.get('cenaryOfLife')
    endOfLife = request.args.get('endOfLife')
    keyWords = request.args.get('keyWords')
    language = request.args.get('language')
    gender_identity = request.args.get('gender_identity')

    prompt = generate_premium_prompt(
        story=story,
        emotion=emotion,
        journey=journey,
        favGenre=favGenre,
        age=age,
        cenaryOfLife=cenaryOfLife,
        endOfLife=endOfLife,
        keyWords=keyWords,
        language=language,
        gender_identity=gender_identity
    )
    system_message = generate_premium_system_message(language)
    response = generate_premium_response(system_message, prompt)
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)