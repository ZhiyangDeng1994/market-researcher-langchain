from dotenv import load_dotenv
load_dotenv()

from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-opus-4-8")
prompts = "Introduce the mathematical formulation of mean field games and mean field type control."
response = llm.invoke(prompts).content

print(response)