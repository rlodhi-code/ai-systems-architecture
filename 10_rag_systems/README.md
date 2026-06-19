# RAG Systems: Learning Path

A progressive, end-to-end Jupyter Notebook covering the full Retrieval-Augmented Generation (RAG) pipeline using **LangChain 1.2.x** and **OpenAI**. The notebook is organized in three parts — Indexing, Retrieval, and Generation — mirroring how a production RAG system is actually built.

---

## Overview

RAG is a pattern that enhances LLM responses by grounding them in external knowledge. Instead of relying solely on a model's training data, a RAG system retrieves relevant documents at query time and passes them to the model as context. This notebook builds that pipeline from the ground up, step by step.

```
Documents → Load → Split → Embed → Store → Retrieve → Generate
```

---

## Notebook: `rag_learning_path.ipynb`

### Part 1 — Indexing

Indexing is the process of preparing documents so they can be efficiently searched later.

| Section | Description |
|---|---|
| Document Loading with PyPDF Loader | Load PDF files using `PyPDFLoader` from `langchain-community` |
| Document Loading with DOCX2TXT Loader | Load Word documents using the `Docx2txtLoader` |
| Document Splitting with Character Text Splitter | Split documents into chunks by character count with configurable overlap |
| Document Splitting with Markdown Header Text Splitter | Structure-aware splitting that preserves Markdown hierarchy |
| Text Embedding with OpenAI | Convert text chunks into dense vector representations using OpenAI embeddings |
| Creating a Chroma Vectorstore | Persist embedded documents in a local Chroma vector database |
| Inspecting and Managing Documents in a Vectorstore | Query, inspect, and manage the contents of a Chroma collection |

### Part 2 — Retrieval

Retrieval is the process of finding the most relevant document chunks for a given query.

| Section | Description |
|---|---|
| Similarity Search | Retrieve documents by cosine similarity to a query embedding |
| Maximal Marginal Relevance (MMR) Search | Balance relevance and diversity to reduce redundancy in retrieved results |
| Vectorstore-Backed Retriever | Wrap a vectorstore as a LangChain `Retriever` object for use in chains |

### Part 3 — Generation

Generation is the final step: combining retrieved context with a prompt to produce a grounded LLM response.

| Section | Description |
|---|---|
| Stuffing Documents | Combine retrieved chunks into a single prompt context using the stuffing strategy |
| Generating a Response | Pass the stuffed context to an LLM and generate a final answer |

---

## Environment Setup

Follow these steps from an **Anaconda Prompt** to create a fully isolated environment with all dependencies required to run this notebook.

### Step 1 — Create a Conda Environment

```bash
Note: I have used my existing environment llm_course_env_311 and Jupyter Notebook)
conda create -n rag_env python=3.11 -y
```

### Step 2 — Activate the Environment

```bash
conda activate rag_env
```

### Step 3 — Install Jupyter

```bash
conda install -c conda-forge notebook jupyterlab -y
```

### Step 4 — Install All Python Dependencies

Run this single command to install every package the notebook requires:

```bash
pip install langchain==1.2.* ^
            langchain-community ^
            langchain-openai ^
            langchain-chroma ^
            langchain-text-splitters ^
            langchain-core ^
            chromadb ^
            openai ^
            tiktoken ^
            pypdf ^
            docx2txt ^
            numpy ^
            python-dotenv
```

> **Note (Linux/macOS):** Replace the `^` line continuation characters with `\`

### Step 5 — Register the Environment as a Jupyter Kernel

```bash
pip install ipykernel
python -m ipykernel install --user --name rag_env --display-name "Python (rag_env)"
```

### Step 6 — Configure Your OpenAI API Key

Create a `.env` file in the same folder as the notebook:

```
OPENAI_API_KEY=sk-...
```

The notebook loads this automatically via:

```python
from dotenv import load_dotenv
load_dotenv()
```

### Step 7 — Launch Jupyter and Select the Kernel

```bash
jupyter notebook
```

Once the notebook opens, go to **Kernel → Change Kernel → Python (rag_env)** to ensure it runs in the correct environment.

---

## Sample Files

The document loading sections expect sample files in the same directory as the notebook:

- `Introduction_to_Data_and_Data_Science.pdf` — used in the PyPDF loading section
- A `.docx` file of your choice — used in the DOCX2TXT loading section

You can substitute any PDF or Word document; adjust the file paths in the relevant cells accordingly.

---

## How to Use

1. Clone the repository and navigate to the `10_rag_systems/` folder.
2. Complete the Environment Setup steps above.
3. Open `rag_learning_path.ipynb` in Jupyter.
4. Confirm the kernel is set to **Python (rag_env)**.
5. Run cells top to bottom — the notebook is designed to be executed sequentially.

---

## LangChain Version Notes

This notebook targets **LangChain 1.2.x**. Several imports changed from earlier versions:

| Component | Import Path |
|---|---|
| `PyPDFLoader` | `langchain_community.document_loaders` |
| `Chroma` | `langchain_chroma` (separate package) |
| `OpenAIEmbeddings` | `langchain_openai` |
| `ChatOpenAI` | `langchain_openai` |
| `CharacterTextSplitter` | `langchain_text_splitters.character` |
| `MarkdownHeaderTextSplitter` | `langchain_text_splitters.markdown` |

If you encounter import errors, verify the correct environment is active (`conda activate rag_env`) and that all packages installed without errors in Step 4.

---

## Related

This notebook is part of the [`ai-systems-architecture`](https://github.com/rlodhi-code/ai-systems-architecture) learning portfolio, which covers the full Agentic AI stack — from LLM fundamentals through RAG pipelines to multi-agent orchestration with LangGraph.
