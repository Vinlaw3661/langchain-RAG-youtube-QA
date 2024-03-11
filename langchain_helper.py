from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from dotenv import load_dotenv


load_dotenv()


def generate_pet_name(animal_type,animal_color):
    llm = OpenAI(temperature = 0.7)

    prompt_template_name = PromptTemplate( 
        input_variables=['animal_type',"animel_color"], 
        template= "I have a pet {animal_type} and want a cool name for it. It's {animal_color} in color. Generate a list of five cool names for my pet dog"
        ) 
    
    name_chain = LLMChain(llm = llm, prompt=prompt_template_name, output_key="pet_name")

    response = name_chain({'animal_type':animal_type, 'animal_color': animal_color})

    return response

def langchain_agent():
    llm = OpenAI(temperature=0.7)

    tools = load_tools(['wikipedia', 'llm-math'], llm=llm)

    agent = initialize_agent(
        tools,llm, agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION , verbose = True
    )

    result = agent.run(
        "What is the average age of a dog? Multiply the age by 3" 
    )

    print(result)

if __name__ == '__main__':

    langchain_agent()
    print(generate_pet_name("cat"))