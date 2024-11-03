# dependencies
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# models
from src.model.models import Img

load_dotenv()

async def trigger_ai_response(image_urls):
    question = (
        "Dada la siguiente lista de URLs de imágenes obtenidas de una página de noticias, "
        "identifica y devuelve cuál de estas imágenes es más probable que represente la imagen principal de la noticia. "
        "Considera los siguientes factores: la relevancia del contenido visual, la fecha de publicación, "
        "y el contexto del artículo en el que se presenta la imagen. "
        "Aquí está el arreglo de imágenes: {}"
    ).format(image_urls)
    
    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    parser = JsonOutputParser(pydantic_object=Img)

    prompt = PromptTemplate(
        template="Answer the user query.\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={
            "format_instructions": parser.get_format_instructions()
        },
    )
    
    chain = prompt | model | parser
    
    response = chain.invoke({"query": question})  
    
    return response  