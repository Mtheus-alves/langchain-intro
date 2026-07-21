from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

gemini = init_chat_model(model="gpt-5-nano", model_provider="openai")
answer_gemini = gemini.invoke("Hello World")
print(answer_gemini.content)