premium_system_message_pt = """Você é um especialista em psicanálise e cinema, com profundo conhecimento em narrativas cinematográficas e análise psicológica. 
Sua tarefa é analisar detalhadamente a história de vida de uma pessoa, considerando suas emoções, jornada pessoal, preferências, contexto e identidade de gênero, 
para recomendar um filme que ressoe profundamente com sua experiência. Seja extremamente preciso e detalhado em sua análise, 
fornecendo não apenas o nome do filme, mas também uma breve explicação de por que este filme específico se conecta com a história da pessoa."""

premium_system_message_en = """You are a specialist in psychoanalysis and cinema, with deep knowledge in cinematographic narratives and psychological analysis.
Your task is to thoroughly analyze a person's life story, considering their emotions, personal journey, preferences, context, and gender identity,
to recommend a movie that deeply resonates with their experience. Be extremely precise and detailed in your analysis,
providing not only the movie name but also a brief explanation of why this specific movie connects with the person's story."""

premium_system_message_es = """Eres un experto en psicoanálisis y cine, con profundo conocimiento en narrativas cinematográficas y análisis psicológico.
Tu tarea es analizar detalladamente la historia de vida de una persona, considerando sus emociones, viaje personal, preferencias, contexto e identidad de género,
para recomendar una película que resuene profundamente con su experiencia. Sé extremadamente preciso y detallado en tu análisis,
proporcionando no solo el nombre de la película, sino también una breve explicación de por qué esta película específica se conecta con la historia de la persona."""

premium_prompt_base_pt = """Analise profundamente a seguinte história de vida e recomende um filme que ressoe com a experiência da pessoa:

História: {story}
Emoção predominante: {emotion}
Jornada pessoal: {journey}
Gênero favorito: {favGenre}
Idade: {age}
Cenário de vida: {cenaryOfLife}
Perspectiva sobre o fim da vida: {endOfLife}
Palavras-chave importantes: {keyWords}
Identidade de gênero: {gender_identity}

Por favor, forneça:
1. O nome do filme recomendado
2. Uma breve explicação de por que este filme se conecta com a história
3. Como os elementos específicos do filme ressoam com os aspectos mencionados acima

Idioma da resposta: {language}"""

premium_prompt_base_en = """Deeply analyze the following life story and recommend a movie that resonates with the person's experience:

Story: {story}
Predominant emotion: {emotion}
Personal journey: {journey}
Favorite genre: {favGenre}
Age: {age}
Life setting: {cenaryOfLife}
Perspective on end of life: {endOfLife}
Important keywords: {keyWords}
Gender identity: {gender_identity}

Please provide:
1. The name of the recommended movie
2. A brief explanation of why this movie connects with the story
3. How specific elements of the movie resonate with the aspects mentioned above

Response language: {language}"""

premium_prompt_base_es = """Analiza profundamente la siguiente historia de vida y recomienda una película que resuene con la experiencia de la persona:

Historia: {story}
Emoción predominante: {emotion}
Viaje personal: {journey}
Género favorito: {favGenre}
Edad: {age}
Escenario de vida: {cenaryOfLife}
Perspectiva sobre el fin de la vida: {endOfLife}
Palabras clave importantes: {keyWords}
Identidad de género: {gender_identity}

Por favor, proporciona:
1. El nombre de la película recomendada
2. Una breve explicación de por qué esta película se conecta con la historia
3. Cómo los elementos específicos de la película resuenan con los aspectos mencionados anteriormente

Idioma de la respuesta: {language}"""

def generate_premium_prompt(story, emotion, journey, favGenre, age, cenaryOfLife, endOfLife, keyWords, language, gender_identity):
    if language == "pt":
        return premium_prompt_base_pt.format(
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
    elif language == "en":
        return premium_prompt_base_en.format(
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
    elif language == "es":
        return premium_prompt_base_es.format(
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

def generate_premium_system_message(language):
    if language == "pt":
        return premium_system_message_pt
    elif language == "en":
        return premium_system_message_en
    elif language == "es":
        return premium_system_message_es 