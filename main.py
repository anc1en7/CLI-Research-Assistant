from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langgraph.prebuilt import create_react_agent
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatAnthropic(model="claude-haiku-4-5-20251001")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

system_prompt = """
You are a research assistant. Your task is to research a given topic and provide a summary, sources, and tools used in your research.
Wrap the output in this format and provide no other text\n{format_instructions}
""".format(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]

# create_agent returns a compiled LangGraph agent directly
agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt=system_prompt,
)

query = input("How can I assist you with your research today? ")

raw_response = agent.invoke({"messages": [{"role": "user", "content": query}]})

# Extract and parse the text response
output_text = raw_response["messages"][-1].content
parsed = parser.parse(output_text)

try:
    # Attempt to parse the response
    parsed = parser.parse(output_text)
    print(parsed)
except Exception as e:
    print(f"Failed to parse response: {e}")
    print(f"Raw response: {output_text}")