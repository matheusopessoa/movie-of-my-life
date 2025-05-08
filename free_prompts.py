free_system_message_pt = "Voce é um especialista em psicanalise e cinema, que ao ouvir a historia da vida de uma pessoa, consegue indicar um filme que vai gerar identificação e emoção por se ver nele. Seja preciso ao indicar o filme, diga apenas o nome do filme e nada mais."
free_system_message_en = "You are a specialist in psychoanalysis and cinema, who, upon hearing the life story of a person, can indicate a movie that will generate identification and emotion by seeing it. Be precise when indicating the movie, say only the name of the movie and nothing else."
free_system_message_es = "Eres un experto en psicoanálisis y cine, que al escuchar la historia de la vida de una persona, puede indicar una película que generará identificación y emoción al verla. Se preciso al indicar la película, diga solo el nombre de la película y nada más."

free_prompt_base_pt = "A partir da história a seguir, indique um filme que vai gerar identificação e emoção por se ver nele: {story} Idioma: {language}"
free_prompt_base_en = "Based on the following story, indicate a movie that will generate identification and emotion by seeing it: {story} Language: {language}"
free_prompt_base_es = "A partir de la siguiente historia, indica una película que generará identificación y emoción al verla: {story} Idioma: {language}"

def generate_free_prompt(story, language):
    if language == "pt":
        return free_prompt_base_pt.format(story=story, language=language)
    elif language == "en":
        return free_prompt_base_en.format(story=story, language=language)
    elif language == "es":
        return free_prompt_base_es.format(story=story, language=language)

def generate_free_system_message(language):
    if language == "pt":
        return free_system_message_pt
    elif language == "en":
        return free_system_message_en
    elif language == "es":
        return free_system_message_es



