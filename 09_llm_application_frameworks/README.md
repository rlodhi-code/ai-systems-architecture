# 🧠 LangChain Application Frameworks — Prompting, LCEL & Runnables

This module provides a practical introduction to building LLM applications using **LangChain** and the **LangChain Expression Language (LCEL)**.  
It covers structured prompting, message roles, few‑shot prompting, prompt templates, and the full suite of LCEL components for constructing modular, debuggable LLM pipelines.

---

## 📁 Project Structure

```
09_llm_application_frameworks/
│
├── 01_model_system_human_ai_messages.ipynb
├── 02_lcel_runnables_and_chains.ipynb
│
└── README.md
```

---

# ⚙️ Environment Setup

A dedicated environment is recommended for this module to ensure compatibility with LangChain and related packages.

### **Create a new Conda environment**

```bash
conda create --name langchain_env python=3.10.10
activate langchain_env
```

### **Verify Python version**

```bash
python -V
```

### **Install core dependencies**

```bash
pip install openai python-dotenv ipykernel jupyterlab notebook
```

### **Register the environment as a Jupyter kernel**

```bash
python -m ipykernel install --user --name langchain_env
```

### **Install LangChain and related libraries**

```bash
pip install langchain==0.2.8
pip install langchain-openai==0.1.7
pip install chardet
pip install grandalf
```

**Note:**  
`grandalf` is required for LCEL graph visualization (graphing runnable pipelines).

---

# 1️⃣ Structured Prompting — System, Human, and AI Messages

**Notebook:** `01_model_system_human_ai_messages.ipynb`

This notebook introduces the message‑role structure used by modern LLM frameworks.

### **System Messages**
Define rules, tone, persona, and constraints.  
They act as the highest‑priority instruction layer.

### **Human Messages**
Represent the user’s request or input.

### **AI Messages**
Store previous model responses, enabling multi‑turn reasoning and conversation continuity.

---

## 🎭 Sarcasm and Tone Control

Sarcasm is included as an example because it demonstrates:

- tone understanding  
- contextual reasoning  
- implicit meaning  
- instruction hierarchy (system > human)  

It highlights how system messages can override or shape stylistic behavior.

---

## 🧩 Few‑Shot Prompting

Few‑shot prompting provides example inputs and outputs to guide the model toward:

- consistent formatting  
- specific tone  
- structured responses  
- task‑specific behavior  

This technique improves reliability without requiring fine‑tuning.

---

## 🧩 Prompt Templates & Prompt Values

Prompt templates allow reusable prompt structures with dynamic values.  
They support:

- clean separation of logic and content  
- consistent formatting  
- integration with LangChain chains  
- scalable application development  

---

# 2️⃣ LangChain Expression Language (LCEL) & Runnables

**Notebook:** `02_lcel_runnables_and_chains.ipynb`

This notebook introduces the LCEL components used to build modular, composable LLM pipelines.

---

## 🔹 Piping a Prompt → Model → Output Parser

The core LCEL pattern:

```
prompt | model | parser
```

This creates readable, debuggable chains with minimal boilerplate.

---

## 🔹 Runnable & RunnableSequence

- **Runnable** — a single executable step  
- **RunnableSequence** — a pipeline of runnables executed in order  

These form the foundation of LCEL workflows.

---

## 🔹 RunnablePassthrough

Allows original inputs to be forwarded while adding new fields.  
Useful for multi‑input chains and branching logic.

---

## 🔹 Batching

Enables efficient processing of multiple inputs through the same chain.

---

## 🔹 Streaming

Supports token‑by‑token output streaming for real‑time applications such as chat interfaces.

---

## 🔹 Graphing Runnables

LCEL pipelines can be visualized as graphs to understand execution flow.  
Graphing requires the `grandalf` package.

---

## 🔹 RunnableParallel

Executes multiple branches simultaneously.  
Useful for:

- generating multiple summaries  
- running multiple models  
- combining embeddings with metadata  
- parallel analysis workflows  

---

# 3️⃣ Piping a RunnableParallel with Other Runnables

Parallel branches can be composed with additional runnables to form multi‑stage workflows.

This enables:

- merging structured and unstructured outputs  
- combining multiple analyses  
- feeding parallel results into downstream steps  

This pattern supports complex, multi‑branch pipelines while maintaining readability.

---

# 4️⃣ RunnableLambda — Custom Python Logic in LCEL

RunnableLambda wraps any Python function and turns it into a runnable step.

### **Capabilities**

- preprocess inputs  
- postprocess outputs  
- apply conditional logic  
- integrate external tools  
- enrich chain state  
- combine Python logic with LLM steps  

### **Example**

```python
from langchain_core.runnables import RunnableLambda

clean_text = RunnableLambda(lambda x: x.strip())
```

RunnableLambda enables seamless integration of Python logic into LCEL pipelines.

---

# 5️⃣ The `@chain` Decorator — Python Functions as LCEL Chains

The `@chain` decorator converts a Python function into a Runnable with LCEL execution behavior.

### **What it provides**

- automatic wrapping into a runnable  
- support for `.invoke()`, `.batch()`, `.stream()`  
- compatibility with LCEL piping (`|`)  
- metadata for debugging and graphing  

### **Example**

```python
from langchain_core.runnables import chain

@chain
def clean_text(x):
    return x.strip()
```

The decorated function becomes a chain step that can be composed with prompts, models, and other runnables.

---

# 📘 Learning Outcomes

This module provides a foundation for building production‑grade LLM applications.

### **Prompting Concepts**

- system, human, and AI messages  
- few‑shot prompting  
- tone control  
- prompt templates  

### **LCEL Concepts**

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

