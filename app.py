# import streamlit as st
# import requests
# import json
# from langchain.chat_models.base import BaseChatModel
# from langchain.prompts.chat import (
#     ChatPromptTemplate,
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate
# )
# from langchain.chains import SequentialChain, LLMChain
# from langchain.schema import BaseMessage, AIMessage, HumanMessage, SystemMessage, ChatResult, ChatGeneration
# import logging
# from typing import List, Optional

# # Definindo a classe do modelo de chat
# class OllamaChat(BaseChatModel):
#     url: str
#     headers: dict
#     model_name: str

#     def get_prompt(self, messages: List[BaseMessage]) -> str:
#         prompt = f"{messages[0].content} "
#         for i, message in enumerate(messages[1:]):
#             if isinstance(message, HumanMessage):
#                 prompt += f"USUÁRIO: {message.content} "
#             elif isinstance(message, AIMessage):
#                 prompt += f"ASSISTENTE: {message.content}</s>"
#         prompt += f"ASSISTENTE:"
#         return prompt

#     def _generate(self, messages: List[BaseMessage], stop: Optional[List[str]] = None) -> ChatResult:
#         prompt = self.get_prompt(messages)
#         payload = {
#             "model": self.model_name,
#             "prompt": prompt
#         }
#         responses = []
#         try:
#             response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))
            
#             raw_response = response.content.decode('utf-8')

#             # Separe os diferentes objetos JSON
#             json_objects = raw_response.split('\n')

#             # Inicialize uma lista para armazenar as respostas
#             responses = []
            
#             for obj in json_objects:
#                 if obj.strip():  # Certifique-se de ignorar linhas vazias
#                     try:
#                         parsed_obj = json.loads(obj)
#                         responses.append(parsed_obj)
#                     except json.JSONDecodeError as e:
#                         print(f"Erro ao decodificar JSON: {e}")

#             # Combine as respostas para formar a resposta final
#             final_response = ''.join([resp['response'] for resp in responses if 'response' in resp])
#             generated_text = final_response.strip()
            
#         except requests.RequestException as e:
#             generated_text = f"Erro na solicitação: {str(e)}"

#         ai_message = AIMessage(content=generated_text)
#         chat_result = ChatResult(generations=[ChatGeneration(message=ai_message)])
#         return chat_result


#     @property
#     def _llm_type(self) -> str:
#         return self.model_name

#     def _agenerate(self):
#         return None

# # Inicializando o modelo
# url = "http://localhost:11434/api/generate"
# headers = {"Content-Type": "application/json"}
# model_name = "llama3"

# chat = OllamaChat(url=url, headers=headers, model_name=model_name)

# class ItineraryTemplate:
#     def __init__(self):
#         self.system_template = """
#         Você é um agente de viagens que ajuda os usuários a fazer planos de viagem, seu nome é Lucas.
#         """
#         self.human_template = """
#         ####{request}####
#         """
#         self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.system_template)
#         self.human_message_prompt = HumanMessagePromptTemplate.from_template(self.human_template, input_variables=["request"])
#         self.chat_prompt = ChatPromptTemplate.from_messages([self.system_message_prompt, self.human_message_prompt])

# class Agent:
#     def __init__(self, chat_model, verbose=True):
#         self.logger = logging.getLogger(__name__)
#         if verbose:
#             self.logger.setLevel(logging.INFO)
#         self.chat_model = chat_model
#         self.verbose = verbose

#     def get_itinerary(self, request):
#         itinerary_template = ItineraryTemplate()
#         travel_agent = LLMChain(
#             llm=self.chat_model,
#             prompt=itinerary_template.chat_prompt,
#             verbose=self.verbose,
#             output_key='agent_suggestion'
#         )
#         overall_chain = SequentialChain(
#             chains=[travel_agent],
#             input_variables=["request"],
#             output_variables=["agent_suggestion"],
#             verbose=self.verbose
#         )
#         return overall_chain({"request": request}, return_only_outputs=True)

# my_agent = Agent(chat)

# # Streamlit App
# st.title("Agente de Viagem Virtual")
# st.write("Bem-vindo ao seu agente de viagens virtual! Por favor, insira seus planos de viagem abaixo.")

# request = st.text_area("Descreva seus planos de viagem:")

# if st.button("Gerar Itinerário"):
#     if request:
#         result = my_agent.get_itinerary(request)
#         st.write(result["agent_suggestion"])
#     else:
#         st.write("Por favor, insira seus planos de viagem.")




# # import streamlit as st
# # import requests
# # import json
# # import logging
# # from langchain.chat_models.base import BaseChatModel
# # from langchain.prompts.chat import (
# #     ChatPromptTemplate,
# #     SystemMessagePromptTemplate,
# #     HumanMessagePromptTemplate
# # )
# # from langchain.chains import SequentialChain, LLMChain
# # from langchain.schema import BaseMessage, AIMessage, HumanMessage, SystemMessage, ChatResult, ChatGeneration
# # from typing import List, Optional

# # # Definindo a classe do modelo de chat
# # class OllamaChat(BaseChatModel):
# #     url: str
# #     headers: dict
# #     model_name: str

# #     def get_prompt(self, messages: List[BaseMessage]) -> str:
# #         prompt = f"{messages[0].content} "
# #         for i, message in enumerate(messages[1:]):
# #             if isinstance(message, HumanMessage):
# #                 prompt += f"USUÁRIO: {message.content} "
# #             elif isinstance(message, AIMessage):
# #                 prompt += f"ASSISTENTE: {message.content}</s>"
# #         prompt += f"ASSISTENTE:"
# #         return prompt

# #     def _generate(self, messages: List[BaseMessage], stop: Optional[List[str]] = None) -> ChatResult:
# #         prompt = self.get_prompt(messages)
# #         payload = {
# #             "model": self.model_name,
# #             "prompt": prompt
# #         }
# #         responses = []
# #         try:
# #             response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))
            
# #             raw_response = response.content.decode('utf-8')

# #             # Separe os diferentes objetos JSON
# #             json_objects = raw_response.split('\n')

# #             # Inicialize uma lista para armazenar as respostas
# #             responses = []
            
# #             for obj in json_objects:
# #                 if obj.strip():  # Certifique-se de ignorar linhas vazias
# #                     try:
# #                         parsed_obj = json.loads(obj)
# #                         responses.append(parsed_obj)
# #                     except json.JSONDecodeError as e:
# #                         print(f"Erro ao decodificar JSON: {e}")

# #             # Combine as respostas para formar a resposta final
# #             final_response = ''.join([resp['response'] for resp in responses if 'response' in resp])
# #             generated_text = final_response.strip()
            
# #         except requests.RequestException as e:
# #             generated_text = f"Erro na solicitação: {str(e)}"

# #         ai_message = AIMessage(content=generated_text)
# #         chat_result = ChatResult(generations=[ChatGeneration(message=ai_message)])
# #         return chat_result


# #     @property
# #     def _llm_type(self) -> str:
# #         return self.model_name

# #     def _agenerate(self):
# #         return None

# # # Inicializando o modelo
# # url = "http://localhost:11434/api/generate"
# # headers = {"Content-Type": "application/json"}
# # model_name = "llama3"

# # chat = OllamaChat(url=url, headers=headers, model_name=model_name)

# # class ItineraryTemplate:
# #     def __init__(self, agent_name="Seu Agente"):
# #         self.agent_name = agent_name
# #         self.system_template = f"""
# #         Olá! Meu nome é {self.agent_name}, sou o seu agente de viagens e estou aqui para ajudar você a criar um plano de viagem emocionante.
# #         """
# #         self.human_template = """
# #         #### {request} ####
# #         """
# #         self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.system_template)
# #         self.human_message_prompt = HumanMessagePromptTemplate.from_template(self.human_template, input_variables=["request"])
# #         self.chat_prompt = ChatPromptTemplate.from_messages([self.system_message_prompt, self.human_message_prompt])

# # class Agent:
# #     def __init__(self, chat_model, verbose=True):
# #         self.logger = logging.getLogger(__name__)
# #         if verbose:
# #             self.logger.setLevel(logging.INFO)
# #         self.chat_model = chat_model
# #         self.verbose = verbose
# #         self.button_key_counter = 0
# #         self.chat_history = []

# #     def get_itinerary(self, request):
# #         itinerary_template = ItineraryTemplate()
# #         travel_agent = LLMChain(
# #             llm=self.chat_model,
# #             prompt=itinerary_template.chat_prompt,
# #             verbose=self.verbose,
# #             output_key='agent_suggestion'
# #         )
# #         overall_chain = SequentialChain(
# #             chains=[travel_agent],
# #             input_variables=["request"],
# #             output_variables=["agent_suggestion"],
# #             verbose=self.verbose
# #         )
# #         return overall_chain({"request": request}, return_only_outputs=True)

# # # Inicializando o agente de viagem
# # my_agent = Agent(chat)

# # # Streamlit App
# # st.title("Agente de Viagem Virtual")
# # st.write("Bem-vindo ao seu agente de viagens virtual! Digite suas mensagens abaixo:")

# # # Layout do chat com barra de rolagem
# # chat_area = st.empty()
# # user_input = st.text_area("Você:", key=f"user_input_{my_agent.button_key_counter}")

# # if st.button(f"Enviar_{my_agent.button_key_counter}", key=f"button_{my_agent.button_key_counter}") and user_input:
# #     my_agent.chat_history.append({"sender": "user", "message": user_input})
# #     my_agent.chat_history.append({"sender": "agent", "message": my_agent.get_itinerary(user_input)["agent_suggestion"]})
# #     my_agent.button_key_counter += 1

# # # Exibindo o histórico de chat com barra de rolagem
# # for message in my_agent.chat_history:
# #     if message["sender"] == "user":
# #         st.text_input("Você:", value=message["message"], key=f"user_input_{my_agent.button_key_counter}", max_chars=200)
# #     else:
# #         st.text_area("Agente:", value=message["message"], key=f"agent_output_{my_agent.button_key_counter}", height=100, max_chars=500)

# import streamlit as st
# import requests
# import json
# from langchain.chat_models.base import BaseChatModel
# from langchain.prompts.chat import (
#     ChatPromptTemplate,
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate
# )
# from langchain.chains import SequentialChain, LLMChain
# from langchain.schema import BaseMessage, AIMessage, HumanMessage, SystemMessage, ChatResult, ChatGeneration
# import logging
# from typing import List, Optional

# # Definindo a classe do modelo de chat
# class OllamaChat(BaseChatModel):
#     url: str
#     headers: dict
#     model_name: str

#     def get_prompt(self, messages: List[BaseMessage]) -> str:
#         prompt = f"{messages[0].content} "
#         for i, message in enumerate(messages[1:]):
#             if isinstance(message, HumanMessage):
#                 prompt += f"USUÁRIO: {message.content} "
#             elif isinstance(message, AIMessage):
#                 prompt += f"ASSISTENTE: {message.content}</s>"
#         prompt += f"ASSISTENTE:"
#         return prompt

#     def _generate(self, messages: List[BaseMessage], stop: Optional[List[str]] = None) -> ChatResult:
#         prompt = self.get_prompt(messages)
#         payload = {
#             "model": self.model_name,
#             "prompt": prompt
#         }
#         responses = []
#         try:
#             response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))
            
#             raw_response = response.content.decode('utf-8')

#             # Separe os diferentes objetos JSON
#             json_objects = raw_response.split('\n')

#             # Inicialize uma lista para armazenar as respostas
#             responses = []
            
#             for obj in json_objects:
#                 if obj.strip():  # Certifique-se de ignorar linhas vazias
#                     try:
#                         parsed_obj = json.loads(obj)
#                         responses.append(parsed_obj)
#                     except json.JSONDecodeError as e:
#                         print(f"Erro ao decodificar JSON: {e}")

#             # Combine as respostas para formar a resposta final
#             final_response = ''.join([resp['response'] for resp in responses if 'response' in resp])
#             generated_text = final_response.strip()
            
#         except requests.RequestException as e:
#             generated_text = f"Erro na solicitação: {str(e)}"

#         ai_message = AIMessage(content=generated_text)
#         chat_result = ChatResult(generations=[ChatGeneration(message=ai_message)])
#         return chat_result

#     @property
#     def _llm_type(self) -> str:
#         return self.model_name

#     def _agenerate(self):
#         return None

# # Inicializando o modelo
# url = "http://localhost:11434/api/generate"
# headers = {"Content-Type": "application/json"}
# model_name = "llama3"

# chat = OllamaChat(url=url, headers=headers, model_name=model_name)

# # Definindo a classe do agente de viagens
# class ItineraryTemplate:
#     def __init__(self):
#         self.system_template = """
#         Você é um agente de viagens que ajuda os usuários a fazer planos de viagem, seu nome é Lucas.
#         """
#         self.human_template = """
#         ####{request}####
#         """
#         self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.system_template)
#         self.human_message_prompt = HumanMessagePromptTemplate.from_template(self.human_template, input_variables=["request"])
#         self.chat_prompt = ChatPromptTemplate.from_messages([self.system_message_prompt, self.human_message_prompt])

# class Agent:
#     def __init__(self, chat_model, verbose=True):
#         self.logger = logging.getLogger(__name__)
#         if verbose:
#             self.logger.setLevel(logging.INFO)
#         self.chat_model = chat_model
#         self.verbose = verbose

#     def get_itinerary(self, request):
#         itinerary_template = ItineraryTemplate()
#         travel_agent = LLMChain(
#             llm=self.chat_model,
#             prompt=itinerary_template.chat_prompt,
#             verbose=self.verbose,
#             output_key='agent_suggestion'
#         )
#         overall_chain = SequentialChain(
#             chains=[travel_agent],
#             input_variables=["request"],
#             output_variables=["agent_suggestion"],
#             verbose=self.verbose
#         )
#         return overall_chain({"request": request}, return_only_outputs=True)

# # Inicializando o agente de viagens com o modelo LLaMA3
# my_agent = Agent(chat)

# # Interface do Streamlit
# st.title('🌍 Agente de Viagens Virtual')
# st.write("Bem-vindo ao Agente de Viagens Virtual! Como posso ajudar você hoje?")

# # Função para interação do usuário
# def chat_interface():
#     user_input = st.text_input('Você:', key='user_input')
#     if st.button('Enviar'):
#         if user_input:
#             st.write("Você:", user_input)
#             response = my_agent.get_itinerary(user_input)
#             st.write("Assistente:", response['agent_suggestion'])

# # Executando a interface do chat
# chat_interface()


# import streamlit as st
# import requests
# import json
# from langchain.chat_models.base import BaseChatModel
# from langchain.prompts.chat import (
#     ChatPromptTemplate,
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate
# )
# from langchain.chains import SequentialChain, LLMChain
# from langchain.schema import BaseMessage, AIMessage, HumanMessage, SystemMessage, ChatResult, ChatGeneration
# import logging
# from typing import List, Optional

# # Definindo a classe do modelo de chat
# class OllamaChat(BaseChatModel):
#     url: str
#     headers: dict
#     model_name: str

#     def get_prompt(self, messages: List[BaseMessage]) -> str:
#         prompt = f"{messages[0].content} "
#         for i, message in enumerate(messages[1:]):
#             if isinstance(message, HumanMessage):
#                 prompt += f"USUÁRIO: {message.content} "
#             elif isinstance(message, AIMessage):
#                 prompt += f"ASSISTENTE: {message.content}</s>"
#         prompt += f"ASSISTENTE:"
#         return prompt

#     def _generate(self, messages: List[BaseMessage], stop: Optional[List[str]] = None) -> ChatResult:
#         prompt = self.get_prompt(messages)
#         payload = {
#             "model": self.model_name,
#             "prompt": prompt
#         }
#         responses = []
#         try:
#             response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))
            
#             raw_response = response.content.decode('utf-8')

#             # Separe os diferentes objetos JSON
#             json_objects = raw_response.split('\n')

#             # Inicialize uma lista para armazenar as respostas
#             responses = []
            
#             for obj in json_objects:
#                 if obj.strip():  # Certifique-se de ignorar linhas vazias
#                     try:
#                         parsed_obj = json.loads(obj)
#                         responses.append(parsed_obj)
#                     except json.JSONDecodeError as e:
#                         print(f"Erro ao decodificar JSON: {e}")

#             # Combine as respostas para formar a resposta final
#             final_response = ''.join([resp['response'] for resp in responses if 'response' in resp])
#             generated_text = final_response.strip()
            
#         except requests.RequestException as e:
#             generated_text = f"Erro na solicitação: {str(e)}"

#         ai_message = AIMessage(content=generated_text)
#         chat_result = ChatResult(generations=[ChatGeneration(message=ai_message)])
#         return chat_result

#     @property
#     def _llm_type(self) -> str:
#         return self.model_name

#     def _agenerate(self):
#         return None

# # Inicializando o modelo
# url = "http://localhost:11434/api/generate"
# headers = {"Content-Type": "application/json"}
# model_name = "llama3"

# chat = OllamaChat(url=url, headers=headers, model_name=model_name)

# # Definindo a classe do agente de viagens
# class ItineraryTemplate:
#     def __init__(self):
#         self.system_template = """
#         Você é um agente de viagens que ajuda os usuários a fazer planos de viagem, seu nome é Lucas.
#         """
#         self.human_template = """
#         ####{request}####
#         """
#         self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.system_template)
#         self.human_message_prompt = HumanMessagePromptTemplate.from_template(self.human_template, input_variables=["request"])
#         self.chat_prompt = ChatPromptTemplate.from_messages([self.system_message_prompt, self.human_message_prompt])

# class Agent:
#     def __init__(self, chat_model, verbose=True):
#         self.logger = logging.getLogger(__name__)
#         if verbose:
#             self.logger.setLevel(logging.INFO)
#         self.chat_model = chat_model
#         self.verbose = verbose

#     def get_itinerary(self, messages: List[BaseMessage]):
#         itinerary_template = ItineraryTemplate()
#         travel_agent = LLMChain(
#             llm=self.chat_model,
#             prompt=itinerary_template.chat_prompt,
#             verbose=self.verbose,
#             output_key='agent_suggestion'
#         )
#         overall_chain = SequentialChain(
#             chains=[travel_agent],
#             input_variables=["request"],
#             output_variables=["agent_suggestion"],
#             verbose=self.verbose
#         )
#         return overall_chain({"request": messages[-1].content}, return_only_outputs=True)

# # Inicializando o agente de viagens com o modelo LLaMA3
# my_agent = Agent(chat)

# # Interface do Streamlit
# st.title('🌍 Agente de Viagens Virtual')
# st.write("Bem-vindo ao Agente de Viagens Virtual! Como posso ajudar você hoje?")

# # Função para interação do usuário
# def chat_interface():
#     if "messages" not in st.session_state:
#         st.session_state.messages = [
#             SystemMessage(content="Você é um agente de viagens que ajuda os usuários a fazer planos de viagem, seu nome é Lucas.")
#         ]
    
#     user_input = st.text_input('Você:', key='user_input')
#     if st.button('Enviar'):
#         if user_input:
#             st.session_state.messages.append(HumanMessage(content=user_input))
#             response = my_agent.get_itinerary(st.session_state.messages)
#             st.session_state.messages.append(AIMessage(content=response['agent_suggestion']))
    
#     # Exibir o histórico da conversa
#     for message in st.session_state.messages:
#         if isinstance(message, HumanMessage):
#             st.write(f"Você: {message.content}")
#         elif isinstance(message, AIMessage):
#             st.write(f"Assistente: {message.content}")

# # Executando a interface do chat
# chat_interface()

import streamlit as st
import requests
import json
from langchain.chat_models.base import BaseChatModel
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains import SequentialChain, LLMChain
from langchain.schema import BaseMessage, AIMessage, HumanMessage, SystemMessage, ChatResult, ChatGeneration
import logging
from typing import List, Optional

# Definindo a classe do modelo de chat
class OllamaChat(BaseChatModel):
    url: str
    headers: dict
    model_name: str

    def get_prompt(self, messages: List[BaseMessage]) -> str:
        prompt = f"{messages[0].content} "
        for i, message in enumerate(messages[1:]):
            if isinstance(message, HumanMessage):
                prompt += f"USUÁRIO: {message.content} "
            elif isinstance(message, AIMessage):
                prompt += f"ASSISTENTE: {message.content}</s>"
        prompt += f"ASSISTENTE:"
        return prompt

    def _generate(self, messages: List[BaseMessage], stop: Optional[List[str]] = None) -> ChatResult:
        prompt = self.get_prompt(messages)
        payload = {
            "model": self.model_name,
            "prompt": prompt
        }
        responses = []
        try:
            response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))
            
            raw_response = response.content.decode('utf-8')

            # Separe os diferentes objetos JSON
            json_objects = raw_response.split('\n')

            # Inicialize uma lista para armazenar as respostas
            responses = []
            
            for obj in json_objects:
                if obj.strip():  # Certifique-se de ignorar linhas vazias
                    try:
                        parsed_obj = json.loads(obj)
                        responses.append(parsed_obj)
                    except json.JSONDecodeError as e:
                        print(f"Erro ao decodificar JSON: {e}")

            # Combine as respostas para formar a resposta final
            final_response = ''.join([resp['response'] for resp in responses if 'response' in resp])
            generated_text = final_response.strip()
            
        except requests.RequestException as e:
            generated_text = f"Erro na solicitação: {str(e)}"

        ai_message = AIMessage(content=generated_text)
        chat_result = ChatResult(generations=[ChatGeneration(message=ai_message)])
        return chat_result

    @property
    def _llm_type(self) -> str:
        return self.model_name

    def _agenerate(self):
        return None

# Inicializando o modelo
url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}
model_name = "llama3"

chat = OllamaChat(url=url, headers=headers, model_name=model_name)

class ItineraryTemplate:
    def __init__(self):
        self.system_template = """
        Você é um agente de viagens que ajuda os usuários a fazer planos de viagem, seu nome é Lucas.
        """
        self.human_template = """
        ####{request}####
        """
        self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.system_template)
        self.human_message_prompt = HumanMessagePromptTemplate.from_template(self.human_template, input_variables=["request"])
        self.chat_prompt = ChatPromptTemplate.from_messages([self.system_message_prompt, self.human_message_prompt])

class Agent:
    def __init__(self, chat_model, verbose=True):
        self.logger = logging.getLogger(__name__)
        if verbose:
            self.logger.setLevel(logging.INFO)
        self.chat_model = chat_model
        self.verbose = verbose

    def get_itinerary(self, request):
        itinerary_template = ItineraryTemplate()
        travel_agent = LLMChain(
            llm=self.chat_model,
            prompt=itinerary_template.chat_prompt,
            verbose=self.verbose,
            output_key='agent_suggestion'
        )
        overall_chain = SequentialChain(
            chains=[travel_agent],
            input_variables=["request"],
            output_variables=["agent_suggestion"],
            verbose=self.verbose
        )
        return overall_chain({"request": request}, return_only_outputs=True)

my_agent = Agent(chat)

# Streamlit App
st.set_page_config(page_title="Agente de Viagem Virtual")
st.title("Agente de Viagem Virtual")

# Sidebar for parameters
st.sidebar.header("Parâmetros")
temperature = st.sidebar.slider("Temperatura", min_value=0.01, max_value=1.00, value=0.10, step=0.01)
top_p = st.sidebar.slider("Top P", min_value=0.01, max_value=1.00, value=0.90, step=0.01)
max_length = st.sidebar.slider("Comprimento máximo", min_value=32, max_value=128, value=120, step=1)

st.sidebar.write("🔄 [Learn how to build this app](https://your-link.com)")

# Clear chat history button
if st.sidebar.button("Clear Chat History"):
    st.session_state['chat_history'] = [{"role": "assistant", "content": "Como posso ajudar com seus planos de viagem hoje?"}]

# Main chat interface
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [{"role": "assistant", "content": "Como posso ajudar com seus planos de viagem hoje?"}]

# Display chat history
for chat in st.session_state['chat_history']:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# Input for user message
if prompt := st.chat_input("Digite sua mensagem:", disabled=not st.sidebar.button):
    st.session_state['chat_history'].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from agent
    result = my_agent.get_itinerary(prompt)
    response = result["agent_suggestion"]

    # Add agent response to chat history
    st.session_state['chat_history'].append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
