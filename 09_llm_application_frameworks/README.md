# 🧠 LangChain Application Frameworks — Prompting, LCEL & Runnables

This module introduces the practical building blocks required to create production‑grade LLM applications using **LangChain** and **LangChain Expression Language (LCEL)**.  
It expands on structured prompting (system/human/AI messages) and moves into **composable, debuggable, graph‑based LLM pipelines**.

This folder includes:

- Structured prompting  
- Few‑shot prompting  
- Prompt templates  
- LCEL pipelines  
- Runnables (Sequence, Parallel, Lambda)  
- Passthroughs  
- Batching  
- Streaming  
- Graphing runnable chains  
- The `@chain` decorator  

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

# 1️⃣ System, Human, and AI Messages

**Notebook:** `01_model_system_human_ai_messages.ipynb`

This notebook introduces structured prompting using message roles:

### ✔ System Messages  
Define rules, persona, tone, and constraints.  
They act as the highest‑priority instruction layer.

### ✔ Human Messages  
Represent the user’s actual request.

### ✔ AI Messages  
Store the model’s previous responses, enabling multi‑turn reasoning.

---

## 🎭 Why Sarcasm Is Included  
Sarcasm is intentionally used because it tests:

- tone understanding  
- contextual reasoning  
- implicit meaning  
- instruction hierarchy (system > human)  

It demonstrates how system messages override user requests and how tone can be controlled through examples.

---

## 🧩 Few‑Shot Prompting  
Few‑shot prompting provides 2–3 examples to teach the model:

- tone  
- formatting  
- structure  
- task patterns  

This dramatically improves consistency and accuracy.

---

## 🧩 Prompt Templates & Prompt Values  
Developers learn how to:

- define reusable prompt structures  
- inject dynamic values  
- separate logic from content  
- prepare prompts for LangChain chains  

---

# 2️⃣ LangChain Expression Language (LCEL) & Runnables

**Notebook:** `02_lcel_runnables_and_chains.ipynb`

This notebook covers the full set of LCEL components used to build modular, composable LLM pipelines.

---

## 🔹 Piping a Prompt → Model → Output Parser  
The core LCEL pattern:

```
prompt | model | parser
```

This creates a clean, readable, debuggable chain.

---

## 🔹 Runnable & RunnableSequence  
The foundational LCEL building blocks:

- **Runnable** — a single step  
- **RunnableSequence** — a pipeline of steps  

---

## 🔹 RunnablePassthrough  
Allows you to pass original inputs forward while adding new fields.  
Useful for multi‑input chains and branching logic.

---

## 🔹 Batching  
Run multiple inputs through the same chain efficiently.

---

## 🔹 Streaming  
Stream tokens as they are generated — essential for chat UIs and real‑time apps.

---

## 🔹 Graphing Runnables  
Visualize your chain as a graph to understand execution flow.

---

## 🔹 RunnableParallel  
Run multiple branches at the same time.  
Great for:

- generating multiple summaries  
- running multiple models  
- combining embeddings + metadata  

---

# 3️⃣ Piping a RunnableParallel with Other Runnables  
This section demonstrates how to:

- build a parallel branch  
- merge its outputs  
- feed the merged result into additional steps  

This is essential for multi‑step workflows such as:

- combining embeddings + LLM output  
- running multiple analyses in parallel  
- merging structured + unstructured data  

It shows how LCEL supports **complex, multi‑branch pipelines** without losing readability.

---

# 4️⃣ RunnableLambda — Custom Python Logic in LCEL  
RunnableLambda is the missing piece that makes LCEL practical for real applications.

### ✔ What it does  
**Wraps any Python function and turns it into a runnable step.**

### ✔ Why it’s used  
RunnableLambda allows you to:

- preprocess inputs  
- postprocess model outputs  
- apply conditional logic  
- integrate external tools  
- enrich chain state  
- combine Python logic + LLM steps  

### ✔ Example  
```python
from langchain_core.runnables import RunnableLambda

clean_text = RunnableLambda(lambda x: x.strip())
```

Now `clean_text` can be piped into any LCEL chain.

### ✔ Why it belongs in this notebook  
RunnableLambda completes the LCEL toolkit:

- Runnable  
- RunnableSequence  
- RunnableParallel  
- RunnablePassthrough  
- **RunnableLambda**  
- Batching  
- Streaming  
- Graphing  
- @chain decorator  

It shows how to mix **LLM steps + Python logic** in one pipeline.

---

# 5️⃣ The `@chain` Decorator  
The decorator turns a Python function into an LCEL chain automatically.

It simplifies:

- readability  
- debugging  
- reuse  
- modular design  

Perfect for production‑grade pipelines.

---

# 📘 Learning Outcomes

By completing this module, developers will understand:

### 🧩 Prompting Foundations  
- System/human/AI messages  
- Few‑shot prompting  
- Tone control  
- Prompt templates  

### 🧩 LCEL Foundations  
- Runnables  
- RunnableSequence  
- RunnableParallel  
- RunnableLambda  
- Passthroughs  
- Streaming  
- Batching  
- Graphing  
- The `@chain` decorator  

### 🧩 Application‑Level Skills  
- Building modular LLM pipelines  
- Debugging chain execution  
- Combining Python logic with LLM steps  
- Preparing for LangGraph state machines  

---
