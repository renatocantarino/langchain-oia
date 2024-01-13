from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage

from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_organization = os.getenv("OPENAI_ORGANIZATION")

def generate_company(palavra):
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7, #quanto mais perto de 1, mais criativo ele é
        openai_api_key=openai_api_key,
        openai_organization=openai_organization,)
    
    chat_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Você é um assistente IA que sempre responde em português do Brasil",
            ),
             ("human", "Gere 5 frases engraçadas com a palavra {palavra}"),
        ]
    )

    company_names_chain = LLMChain(llm=llm, prompt=chat_template, output_key="company_name")
    response = company_names_chain({ "palavra" : palavra})

    
    return response
    



if __name__ == "__main__":
    print(generate_company("imobiliária"))