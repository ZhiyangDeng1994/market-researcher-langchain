from dotenv import load_dotenv
load_dotenv()

from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model='claude-sonnet-4-6', temperature=0.9)
response = llm.invoke("introduce yourself in ten words.").content
print(response)