# CLI Research Assistant

A command-line AI research assistant powered by Claude and LangGraph. Ask it any research question and it will autonomously search the web, query Wikipedia, compile a structured summary, and save the output to a file.

## How It Works

The agent uses a ReAct loop (Reason + Act) via LangGraph's `create_react_agent`. Given a query, it decides which tools to use, calls them, observes the results, and repeats until it has enough information to produce a structured response.

The final output is parsed into a Pydantic model with four fields: topic, summary, sources, and tools used — and saved to `research_output.txt`.

## Tools

| Tool | Description |
|------|-------------|
| `search_tool` | Searches the web using DuckDuckGo |
| `wiki_tool` | Queries Wikipedia for topic summaries |
| `save_tool` | Saves the research output to a `.txt` file |

## Project Structure

```
CLI-Research-Assistant/
├── main.py           # Entry point — sets up the agent and handles I/O
├── tools.py          # Tool definitions (search, wiki, save)
├── requirments.txt   # Python dependencies
├── research_output.txt  # Generated research outputs (auto-created)
└── .env              # API keys (not committed)
```

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/anc1en7/CLI-Research-Assistant.git
cd CLI-Research-Assistant
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirments.txt
pip install ddgs langgraph
```

**4. Set up your API key**

Create a `.env` file in the root directory:
```
ANTHROPIC_API_KEY=your_api_key_here
```
Get your API key from [console.anthropic.com](https://console.anthropic.com).

## Usage

```bash
python main.py
```

You'll be prompted to enter a research query:
```
How can I assist you with your research today? > What is quantum computing?
```

The agent will search and compile a response, then print a structured result:
```
topic='Quantum Computing'
summary='Quantum computing uses quantum mechanical phenomena...'
sources=['https://en.wikipedia.org/wiki/Quantum_computing', ...]
tools_used=['wiki_tool', 'search_tool', 'save_tool']
```

Results are also appended to `research_output.txt` with a timestamp.

## Dependencies

- `langchain` — agent framework
- `langchain-anthropic` — Claude model integration
- `langchain-community` — DuckDuckGo and Wikipedia tools
- `langgraph` — ReAct agent execution
- `pydantic` — structured output parsing
- `python-dotenv` — environment variable management
- `duckduckgo-search` / `ddgs` — web search backend

## Notes

- The `venv/` folder and `.env` file should be added to `.gitignore` and not committed.
- `research_output.txt` is appended to on each run — delete it to start fresh.
