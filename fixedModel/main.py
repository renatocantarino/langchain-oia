from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage


from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_organization = os.getenv("OPENAI_ORGANIZATION")



def generate_company():
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7, #quanto mais perto de 1, mais criativo ele é
        openai_api_key=openai_api_key,
        openai_organization=openai_organization,)
    
    company_names = llm(
        [
            SystemMessage(
                content="Você é um assistente IA que sempre responde em Português do Brasil"
            ),
            HumanMessage(
                     content="Gere 5 ideias de nomes para empresas no segmento Pets"
            )
        ])
    
    return company_names
    



if __name__ == "__main__":
    print(generate_company())