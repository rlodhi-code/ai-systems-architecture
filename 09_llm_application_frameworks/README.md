# 🧠 LangChain Application Frameworks — LCEL, Runnables & Prompting

This module introduces the practical building blocks required to create production‑grade LLM applications using **LangChain** and **LangChain Expression Language (LCEL)**.  
It expands on structured prompting (system/human/AI messages) and moves into **composable, debuggable, graph‑based LLM pipelines**.

This folder now includes:

- Structured prompting with system/human/AI messages  
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

Notebook: **`01_model_system_human_ai_messages.ipynb`**

This notebook introduces structured prompting using message roles:

### ✔ System Messages  
Define rules, persona, tone, and constraints.  
They act as the highest‑priority instruction layer.

### ✔ Human Messages  
Represent the user’s actual request.

### ✔ AI Messages  
Store the model’s previous responses, enabling multi‑turn reasoning.

### 🎭 Why Sarcasm Is Included  
Sarcasm is intentionally used because it tests:

- tone understanding  
- contextual reasoning  
- implicit meaning  
- instruction hierarchy (system > human)  

It demonstrates how system messages override user requests and how tone can be controlled through examples.

### 🧩 Few‑Shot Prompting  
The notebook includes examples showing how providing 2–3 demonstrations helps the model:

- mimic tone  
- follow formatting  
- produce consistent outputs  
- learn task patterns  

### 🧩 Prompt Templates & Prompt Values  
Developers learn how to:

- define reusable prompt structures  
- inject dynamic values  
- separate logic from content  
- prepare prompts for LangChain chains  

---

# 2️⃣ LangChain Expression Language (LCEL) & Runnables

Notebook: **`02_lcel_runnables_and_chains.ipynb`**  
(**Recommended name — clean, descriptive, and scalable**)

This notebook covers the LCEL components shown in your screenshot.

### ✔ Piping a prompt → model → output parser  
The core LCEL pattern:

```
prompt | model | parser
```

This creates a clean, readable, debuggable chain.

### ✔ Batching  
Run multiple inputs through the same chain efficiently.

### ✔ Streaming  
Stream tokens as they are generated — essential for chat UIs.

### ✔ Runnable & RunnableSequence  
The building blocks of LCEL:

- `Runnable` = a single step  
- `RunnableSequence` = a pipeline of steps  

### ✔ RunnablePassthrough  
Allows you to pass original inputs forward while adding new fields.  
Useful for multi‑input chains.

### ✔ Graphing Runnables  
Visualize your chain as a graph to understand execution flow.

### ✔ RunnableParallel  
Run multiple branches at the same time.  
Great for:

- generating multiple summaries  
- running multiple models  
- combining embeddings + metadata  

### ✔ Piping RunnableParallel with other Runnables  
Compose parallel branches into larger pipelines.

### ✔ RunnableLambda  
Wrap custom Python functions inside LCEL.

### ✔ The `@chain` Decorator  
Turn Python functions into LCEL chains automatically.

---

# 📘 Learning Outcomes

By completing this module, developers will understand:

### 🧩 Prompting Foundations  
- System/human/AI messages  
- Few‑shot prompting  
- Tone control (including sarcasm)  
- Prompt templates & values  

### 🧩 LCEL Foundations  
- Runnables  
- RunnableSequence  
- RunnableParallel  
- RunnableLambda  
- Passthroughs  
- Streaming  
- Batching  
- Graphing chains  
- The `@chain` decorator  

### 🧩 Application‑Level Skills  
- Building modular LLM pipelines  
- Debugging chain execution  
- Combining Python logic with LLM steps  
- Preparing for LangGraph state machines  

---

