import OpenAI from "openai";
import dotenv from "dotenv";

dotenv.config();

const openai = new OpenAI({
  apiKey: process.env.OPEN_AI_KEY,
});

export const generateResponse = async (text: string) => {
  try {
    const response = await openai.responses.create({
      model: "gpt-4.1-nano",
      input: [
        {
          "role": "system",
          "content": [
            {
              "type": "input_text",
              "text": "Você é um assistente que sugere filmes baseados na história de vida das pessoas. IMPORTANTE: Você DEVE retornar APENAS o título do filme no mesmo idioma em que a história foi contada.\n\nExemplos:\n\nEntrada (português): \"Sempre trabalhei muito...\"\nResposta: \"À Procura da Felicidade\"\n\nEntrada (inglês): \"I always worked hard...\"\nResposta: \"The Pursuit of Happyness\"\n\nEntrada (espanhol): \"Siempre trabajé duro...\"\nResposta: \"En Busca de la Felicidad\"\n\nRegras:\n1. Retorne APENAS o título do filme\n2. Use o mesmo idioma da história\n3. Não adicione explicações ou comentários"
            }
          ]
        },
        {
          "role": "user",
          "content": [
            {
              "type": "input_text",
              "text": text
            }
          ]
        }
      ],
      text: {
        "format": {
          "type": "text"
        }
      },
      reasoning: {},
      tools: [],
      temperature: 1,
      max_output_tokens: 16,
      top_p: 1,
      store: true
    });

    return { movie: response.output_text };
  } catch (error) {
    console.error('Erro ao gerar resposta:', error);
    throw error;
  }
};
