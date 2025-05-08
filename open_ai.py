from openai import OpenAI
import os
import json

api_key = os.getenv("OPEN_AI_KEY")
client = OpenAI(api_key=api_key)

def generate_free_response(system_message, prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=150
    )
    return response.choices[0].message.content

def generate_premium_response(system_message, prompt):
    json_format_instruction = """
    Retorne sua resposta em formato JSON com a seguinte estrutura:
    {
        "movie_name": "Nome do filme",
        "movie_year": "Ano do filme",
        "connection_explanation": "Explicação detalhada de como o filme se conecta com a história",
        "resonant_elements": ["Elemento 1", "Elemento 2", "Elemento 3"]
    }
    """
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
            {"role": "system", "content": json_format_instruction}
        ],
        temperature=1,
        max_tokens=500
    )
    
    try:
        content = response.choices[0].message.content
        json_start = content.find('{')
        json_end = content.rfind('}') + 1
        if json_start >= 0 and json_end > json_start:
            json_str = content[json_start:json_end]
            return json.loads(json_str)
        else:
            return {
                "movie_name": content,
                "movie_year": None,
                "connection_explanation": "",
                "resonant_elements": []
            }
    except json.JSONDecodeError:
        return {
            "movie_name": content,
            "movie_year": None,
            "connection_explanation": "",
            "resonant_elements": []
        }