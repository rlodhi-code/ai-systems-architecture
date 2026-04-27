# 🧠 System, Human, and AI Messages — Prompting Foundations

This notebook introduces one of the most important concepts in modern LLM application development: **structured prompting using system, human, and AI messages**.  
It demonstrates how message roles influence model behavior, how to design effective prompts, and how to use few‑shot examples to guide the model toward consistent outputs.

This is part of the `09_llm_application_frameworks` module, which focuses on building real LLM applications using structured prompting patterns.

---

## 📌 What This Notebook Covers

### ✔️ System / Human / AI message roles  
### ✔️ Why sarcasm and tone‑based examples matter  
### ✔️ How system messages enforce rules  
### ✔️ How AI messages shape model behavior  
### ✔️ Few‑shot prompting  
### ✔️ Prompt templates & prompt values  
### ✔️ Practical examples for real applications  

---

## 🧱 Message Roles in LLM Applications

Modern LLM frameworks (OpenAI, LangChain, LangGraph, etc.) use **role‑based messages** to structure conversations.

### **1. System Messages**
These define the *rules*, *persona*, and *boundaries* for the model.

Examples:
- “You are a helpful assistant.”
- “Respond concisely and avoid unnecessary details.”
- “Use a professional tone.”

System messages act as the **highest‑priority instruction layer**.  
They shape the model’s behavior before any user input is processed.

### **2. Human Messages**
These represent the **user’s actual request**.

Examples:
- “Explain quantum computing.”
- “Write a sarcastic response to this sentence.”
- “Summarize this article.”

Human messages are the *questions* or *commands* the model must respond to.

### **3. AI Messages**
These represent the **model’s previous responses**.

They help maintain:
- conversation history  
- tone consistency  
- memory of earlier steps  
- multi‑turn reasoning  

AI messages are essential for **stateful conversations** and **agent workflows**.

---

## 🎭 Why Sarcasm Is Included in the Examples

Sarcasm is intentionally included because:

### ✔️ It tests the model’s ability to understand **tone**
Sarcasm requires:
- contextual understanding  
- emotional nuance  
- implicit meaning  

This makes it a strong test of model capability.

### ✔️ It demonstrates **style transfer**
Developers often need models to:
- mimic a tone  
- rewrite text in a specific style  
- generate creative responses  

Sarcasm is a clear, exaggerated example.

### ✔️ It shows how **system messages constrain behavior**
If the system message says:
> “Avoid sarcasm.”

…and the human message asks for sarcasm,  
the model must follow the system instruction.

This teaches developers how **instruction hierarchy** works.

---

## 🧩 Few‑Shot Prompting

Few‑shot prompting means giving the model **examples** of the behavior you want.

Example:

```
System: You are a polite assistant.
Human: Rewrite the sentence politely.
Human: "Close the door."
AI: "Could you please close the door?"
```

Then the next request:

```
Human: "Move your car."
```

The model learns from the example and responds politely.

Few‑shot prompting helps with:
- tone control  
- formatting consistency  
- classification tasks  
- structured outputs  
- style imitation  

This notebook includes several few‑shot examples to demonstrate how the model learns patterns.

---

## 🧩 Prompt Templates & Prompt Values

Prompt templates allow developers to **reuse prompt structures** with dynamic values.

### Example Template

```python
template = """
You are a helpful assistant.

Task: {task}
Input: {input_text}

Respond clearly and concisely.
"""
```

### Example Prompt Values

```python
prompt = template.format(
    task="Summarize the text",
    input_text="Large language models are transforming AI..."
)
```

This approach is essential for:
- LangChain  
- LangGraph  
- production‑grade LLM apps  
- multi‑step pipelines  
- agent workflows  

Prompt templates ensure:
- consistency  
- maintainability  
- clean separation of logic and content  

---

## 📘 Learning Outcomes

By completing this notebook, developers will understand:

### 🧩 Prompting Foundations
- How system, human, and AI messages interact  
- How message roles influence model behavior  
- Why tone‑based examples (like sarcasm) matter  

### 🧩 Prompt Engineering Techniques
- Few‑shot prompting  
- Style and tone control  
- Instruction hierarchy  

### 🧩 Application‑Level Concepts
- Prompt templates  
- Prompt values  
- Reusable prompt structures  
- How these patterns feed into LangChain and LangGraph  

---

## 🚀 Next Steps

After this notebook, you are ready to explore:

- **LangChain chains & prompt templates**  
- **LangGraph state machines**  
- **RAG (Retrieval‑Augmented Generation)**  
- **Agent workflows**  
- **Tool calling & multi‑step reasoning**  

This notebook sets the foundation for building real LLM applications.

---

