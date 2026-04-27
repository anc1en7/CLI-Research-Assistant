from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool, tool
from datetime import datetime

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

@tool
def save_tool(data: str) -> str:
    """Saves structured research output to a text file."""
    return save_to_txt(data)

_search = DuckDuckGoSearchRun()

@tool
def search_tool(query: str) -> str:
    """Searches the web for information."""
    return _search.run(query)


api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
_wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

@tool
def wiki_tool(query: str) -> str:
    """Searches Wikipedia for information on a given topic."""
    return _wiki.run(query)