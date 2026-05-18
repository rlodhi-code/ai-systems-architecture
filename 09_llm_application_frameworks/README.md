# 🧠 LLM Application Frameworks — LangChain & LlamaIndex

This module provides a practical introduction to building LLM applications using **LangChain** and **LlamaIndex**, including structured prompting, message roles, few‑shot prompting, prompt templates, and the full suite of LCEL‑style components for constructing modular, debuggable LLM pipelines.

---

## 📁 Project Structure

```
09_llm_application_frameworks/
│
├── langchain_basics.ipynb
├── llamaindex_basics.ipynb
├── config.py
├── notes.txt
└── README.md
```

---

## ⚙️ Environment Setup

A dedicated environment is recommended to ensure compatibility with LangChain, LlamaIndex, and related packages.

### **Create a new Conda environment**
```
conda create --name langchain_env python=3.10.10
conda activate langchain_env
```

### **Verify Python version**
```
python -V
```

### **Install core dependencies**
```
pip install openai python-dotenv ipykernel jupyterlab notebook
```

### **Register the environment as a Jupyter kernel**
```
python -m ipykernel install --user --name langchain_env
```

### **Install LangChain, LlamaIndex, and related libraries**
```
pip install langchain==0.2.8
pip install langchain-openai==0.1.7
pip install llama-index
pip install chardet
pip install grandalf
```

> **Note:** `grandalf` is required for graph visualization of runnable pipelines.

---

# 1️⃣ LangChain Basics — Prompting, Templates, and Message Roles  
**Notebook:** `langchain_basics.ipynb`

This notebook introduces the message‑role structure used by modern LLM frameworks.

### **System Messages**
Define rules, tone, persona, and constraints.

### **Human Messages**
Represent the user’s request or input.

### **AI Messages**
Store previous model responses to support multi‑turn reasoning.

### 🎭 Tone Control & Sarcasm  
Used to demonstrate:
- contextual reasoning  
- implicit meaning  
- instruction hierarchy (system > human)  

### 🧩 Few‑Shot Prompting  
Provides examples to guide the model toward:
- consistent formatting  
- specific tone  
- structured outputs  

### 🧱 Prompt Templates  
Enable reusable prompt structures with dynamic values.

---

# 2️⃣ LlamaIndex Basics — LCEL‑Style Runnables & Pipelines  
**Notebook:** `llamaindex_basics.ipynb`

This notebook introduces the components used to build modular, composable LLM pipelines.

### 🔹 Piping a Prompt → Model → Output Parser
```
prompt | model | parser
```

### 🔹 Runnable & RunnableSequence  
- **Runnable** — a single executable step  
- **RunnableSequence** — a pipeline of runnables  

### 🔹 RunnablePassthrough  
For multi‑input chains and branching logic.

### 🔹 Batching  
Efficiently process multiple inputs.

### 🔹 Streaming  
Token‑by‑token output for real‑time applications.

### 🔹 Graphing Runnables  
Visualize execution flow (requires `grandalf`).

### 🔹 RunnableParallel  
Execute multiple branches simultaneously.

### 🔹 RunnableLambda  
Wrap custom Python logic into a runnable step.

### 🔹 `@chain` Decorator  
Convert Python functions into LCEL‑style runnable chains.

---

# 📘 Learning Outcomes

### **Prompting Concepts**
- system, human, and AI messages  
- few‑shot prompting  
- tone control  
- prompt templates  

### **Pipeline Concepts**
- Runnable  
- RunnableSequence  
- RunnableParallel  
- RunnableLambda  
- RunnablePassthrough  
- batching  
- streaming  
- graphing  
- `@chain` decorator  

### **Application Skills**
- constructing modular LLM pipelines  
- combining Python logic with LLM steps  
- debugging chain execution  
- preparing for LangGraph state machines  

---
