# LangGraph Fundamentals

A unified, progressive learning notebook covering the core concepts of **LangGraph** — the framework for building stateful, multi-step AI agent workflows on top of LangChain.

This project consolidates 14 individual course notebooks into a single, self-contained learning path with expanded commentary, bug fixes, and deprecation updates for the specified environment.

---

## Contents

| Section | Topic | Key Concepts |
|---------|-------|-------------|
| 1 | Graph Components | States, Nodes, Edges, START, END |
| 2 | Building Your First Graph | StateGraph, compile(), invoke() |
| 3 | Conditional Edges | Routing functions, branching, loops |
| 4 | The Annotated Construct | Reducers, `Annotated`, `add_messages` |
| 5 | Reducer Functions in Action | State accumulation, message history |
| 6 | The MessagesState Class | Built-in state shortcut |
| 7 | The RemoveMessage Class | Selective message deletion |
| 8 | Trimming Messages | Context window management |
| 9 | Summarizing Messages | Rolling LLM-generated summaries |
| 10 | Short-Term Memory | `InMemorySaver`, thread IDs |
| 11 | The StateSnapshot Class | Checkpoint history, time travel |
| 12 | Long-Term Memory | `SqliteSaver`, cross-session persistence |

---

## Environment Setup

### Step 1 — Create and Activate a Conda Environment

Open **Anaconda Prompt** and run:

```bash
conda create -n langgraph_env python=3.11 -y
conda activate langgraph_env
```

### Step 2 — Install Dependencies

```bash
pip install langchain langgraph langchain-openai langchain-core langsmith openai==1.81.0 python-dotenv==1.1.0 mypy-extensions==1.1.0 grandalf==0.8 ipykernel==6.29.5 notebook==7.4.2
```

For long-term memory (Section 12), also install the SQLite checkpointer:

```bash
pip install langgraph-checkpoint-sqlite
```

### Step 3 — Register the Kernel with Jupyter

```bash
python -m ipykernel install --user --name=langgraph_env --display-name "langgraph_env"
```

### Step 4 — Create Your `.env` File

In the same directory as the notebook, create a file named `.env`:

```
OPENAI_API_KEY=sk-your-key-here
```

> **Never commit your `.env` file to GitHub.** The `.gitignore` in this repo excludes it.

### Step 5 — Launch Jupyter Notebook

```bash
jupyter notebook
```

Open `langgraph_learning_path.ipynb` and select the **langgraph_env** kernel from the kernel menu.

---

## Dependency Notes

| Package | Version | Purpose |
|---------|---------|---------|
| `langchain` | latest | Core LangChain framework |
| `langgraph` | latest | Graph-based agent orchestration |
| `langchain-openai` | latest | OpenAI model integration |
| `langchain-core` | latest | Base classes and interfaces |
| `langsmith` | latest | Tracing and observability |
| `openai` | 1.81.0 | OpenAI Python SDK |
| `python-dotenv` | 1.1.0 | `.env` file loading |
| `mypy-extensions` | 1.1.0 | TypedDict and type hint support |
| `grandalf` | 0.8 | ASCII graph rendering (`draw_ascii()`) |
| `ipykernel` | 6.29.5 | Jupyter kernel support |
| `notebook` | 7.4.2 | Jupyter Notebook interface |
| `langgraph-checkpoint-sqlite` | latest | SQLite persistence (Section 12, optional) |

---

## Key Fixes and Updates vs. Original Course Files

The following issues from the original notebooks were resolved:

- **`%load_ext dotenv` / `%dotenv` magic** replaced with `python-dotenv`'s `load_dotenv()` for broader environment compatibility
- **`%load_ext mypy_ipython` / `%mypy` magic** removed; type checking is handled by the type annotations themselves
- **`state["messages"].content` bug** (notebook 03-05) fixed to `state["messages"][0].content` — `messages` is a list, not a single message object
- **`max_tokens` parameter** updated to `max_completion_tokens` throughout, matching the current OpenAI SDK API
- **SQLite import** wrapped in `try/except` with graceful `InMemorySaver` fallback, since `langgraph-checkpoint-sqlite` is a separate install
- **Hardcoded Windows path** (`C:/Users/Hristina/Desktop/...`) replaced with a portable relative path `"langgraph.db"` with instructions for customization
- **Deprecation warnings** suppressed globally at notebook startup for clean output

---

## Project Structure

```
langgraph-fundamentals/
├── langgraph_learning_path.ipynb   # Unified learning notebook (14 source notebooks combined)
├── README.md                       # This file
├── .env                            # Your API key (not committed to git)
├── .gitignore                      # Excludes .env, __pycache__, .ipynb_checkpoints, *.db
└── langgraph.db                    # SQLite checkpoint database (created at runtime, Section 12)
```

---

## `.gitignore` Recommendation

Create a `.gitignore` with the following content to avoid committing secrets or generated files:

```
.env
*.db
__pycache__/
.ipynb_checkpoints/
*.pyc
```

---

## Stack

- **Language:** Python 3.11
- **Framework:** LangGraph + LangChain
- **LLM:** OpenAI GPT-4o
- **Memory:** InMemorySaver (short-term) / SqliteSaver (long-term)
- **Environment:** Anaconda + Jupyter Notebook

---

## Related Projects

This notebook is part of a broader AI Systems Architecture learning series:

- [`rag-learning-path`](../rag_learning_path) — Retrieval-Augmented Generation with LangChain and ChromaDB
- `langgraph-fundamentals` — **(this project)** Stateful agent graphs with LangGraph
