# 🤖 LLM Fundamentals — GPT, Transformers & BERT‑Based Q&A

This module provides a practical, hands‑on introduction to **Large Language Models (LLMs)** using three complementary approaches:

1. **GPT Models (OpenAI API)**  
2. **Hugging Face Transformers (local + Hub)**  
3. **BERT‑based Question Answering (BERT, RoBERTa, DistilBERT)**  

Each notebook focuses on a different layer of the LLM ecosystem, helping developers understand both **how models work** and **how to use them effectively**.

---

## 📁 Project Structure

```
08_llm_fundamentals/
│
├── 01_gpt_models.ipynb
├── 02_huggingface_transformers.ipynb
├── 03_bert_qa_models.ipynb
│
├── config.py
├── .env
└── README.md
```

---

# 1️⃣ GPT Models (OpenAI API)

Notebook: **`01_gpt_models.ipynb`**

This notebook introduces GPT models using the OpenAI Python SDK.

### 🔍 Topics Covered
- API setup and authentication  
- Chat completions  
- System vs. user messages  
- Temperature, max tokens, top‑p  
- Prompt engineering basics  
- Error handling and rate limits  

### 🔐 Environment Variables
Stored in `.env`:

```
OPENAI_API_KEY=your_key_here
```

Loaded automatically through `config.py`.

---

# 2️⃣ Hugging Face Transformers

Notebook: **`02_huggingface_transformers.ipynb`**

This notebook demonstrates how to load and run models using the **Transformers** library.

### 🚀 Topics Covered
- AutoTokenizer & AutoModel  
- Pipelines for text generation  
- CPU vs GPU execution  
- Loading models from the Hugging Face Hub  
- Understanding model sizes and memory requirements  
- Why tokenizers must match the model  
- Avoiding OOM errors  
- When to use `trust_remote_code=True`  

### 🔐 HF Token Setup
Add this to `.env`:

```
HF_TOKEN=your_huggingface_token
```

`config.py` loads it at runtime:

```python
from config import HF_TOKEN
```

This keeps notebooks clean and avoids hard‑coding secrets.

---

# 3️⃣ BERT‑Based Question Answering  
Notebook: **`03_bert_qa_models.ipynb`**

This notebook demonstrates how to build a **Question Answering (QA)** system using:

- `BertForQuestionAnswering`  
- `BertTokenizer`  
- A SQuAD‑fine‑tuned checkpoint  

### 🧠 What the notebook teaches
- How BERT performs span‑based QA  
- How to tokenize context + question pairs  
- How to interpret start/end logits  
- How to extract the predicted answer span  
- How to run inference on custom text  

### 📌 Models Covered (Conceptually)
Although the notebook uses **BERT**, the same workflow applies to:

| Model | Architecture | Notes |
|-------|--------------|-------|
| **BERT** | Encoder‑only | Bidirectional, strong for QA |
| **RoBERTa** | Encoder‑only | Improved training, often higher accuracy |
| **DistilBERT** | Encoder‑only | Lightweight, faster, 40% smaller |

### 🧩 Why developers can easily extend to RoBERTa & DistilBERT
The only changes required are:

```python
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

model_name = "deepset/roberta-base-squad2"
# or
model_name = "distilbert-base-uncased-distilled-squad"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
```

Everything else — tokenization, encoding, logits, span extraction — stays the same.

This makes the notebook a perfect foundation for experimenting with multiple QA models.

---

# 🔒 Security & Environment Management

### `.env` contains:
```
OPENAI_API_KEY=...
HF_TOKEN=...
```

### `config.py` handles:
- Loading environment variables  
- Validating required keys  
- Exposing them as Python constants  

This keeps your notebooks clean, secure, and production‑friendly.

---

# ▶️ How to Run the Notebooks

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Create `.env`
```env
OPENAI_API_KEY=your_openai_key
HF_TOKEN=your_hf_token
```

### 3. Launch Jupyter
```bash
jupyter notebook
```

Open any notebook and run cells top‑to‑bottom.

---

# 📘 Learning Outcomes

By completing this module, developers will understand:

### 🧩 GPT Models
- Hosted inference  
- Prompting  
- Token budgeting  
- Model selection  

### 🧩 Transformers
- Local inference  
- Tokenizers  
- Pipelines  
- Model loading from the Hub  

### 🧩 BERT‑Based QA
- Span‑based question answering  
- How encoder‑only models differ from GPT  
- How to switch between BERT, RoBERTa, and DistilBERT  

### 🧩 Combined Understanding
You now have a complete foundation in:

- Decoder‑only models (GPT)  
- Encoder‑only models (BERT family)  
- Hugging Face ecosystem  
- Practical inference workflows  

---

# ⭐ Next Steps

- Add RoBERTa and DistilBERT examples  
- Add XLNet for permutation‑based language modeling  
- Add a comparison notebook: **GPT vs BERT vs XLNet**  
- Add a RAG demo (Retrieval‑Augmented Generation)  
- Add LangChain & LangGraph in the next module (`09_llm_application_frameworks`)  

---
