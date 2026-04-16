# 🤖 LLM Fundamentals — GPT, Transformers, BERT QA & XLNet Classification

This module provides a structured, hands‑on introduction to **Large Language Models (LLMs)** and modern NLP techniques.  
It covers four major pillars:

1. **GPT Models (OpenAI API)**  
2. **Hugging Face Transformers (local + Hub)**  
3. **BERT‑family Question Answering (BERT, RoBERTa, DistilBERT)**  
4. **Classical ML vs XLNet for Text Classification**  

Each notebook builds on the previous one, giving developers a clear path from API‑based inference → local model execution → task‑specific architectures → classical vs transformer‑based NLP.

---

## 📁 Project Structure

```
08_llm_fundamentals/
│
├── 01_gpt_models.ipynb
├── 02_huggingface_transformers.ipynb
├── 03_bert_qa_models.ipynb
├── 04_text_classification_classical_vs_xlnet.ipynb
│
├── config.py
├── .env
└── README.md
```

Your filenames are **clear, consistent, and do NOT need to be changed**.

---

# 1️⃣ GPT Models (OpenAI API)

**Notebook:** `01_gpt_models.ipynb`

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

Loaded via `config.py`.

---

# 2️⃣ Hugging Face Transformers

**Notebook:** `02_huggingface_transformers.ipynb`

This notebook demonstrates how to load and run models using the **Transformers** library.

### 🚀 Topics Covered
- AutoTokenizer & AutoModel  
- Pipelines for text generation  
- CPU vs GPU execution  
- Loading models from the Hugging Face Hub  
- Understanding model sizes and memory requirements  
- Why tokenizers must match the model  
- Avoiding out‑of‑memory errors  
- When to use `trust_remote_code=True`  

### 🔐 HF Token Setup
Add this to `.env`:

```
HF_TOKEN=your_huggingface_token
```

Loaded automatically via:

```python
from config import HF_TOKEN
```

---

# 3️⃣ BERT‑Family Question Answering (BERT, RoBERTa, DistilBERT)

**Notebook:** `03_bert_qa_models.ipynb`

This notebook demonstrates how to build a **Question Answering (QA)** system using:

- `BertForQuestionAnswering`  
- `BertTokenizer`  
- A SQuAD‑fine‑tuned checkpoint  

### 🧠 What the notebook teaches
- How encoder‑only models perform span‑based QA  
- How to tokenize context + question pairs  
- How to interpret start/end logits  
- How to extract the predicted answer span  
- How to run inference on custom text  

### 📌 BERT, RoBERTa & DistilBERT — All Supported

The notebook currently uses **BERT**, but developers can easily switch to:

| Model | Architecture | Notes |
|-------|--------------|-------|
| **BERT** | Encoder‑only | Bidirectional, strong for QA |
| **RoBERTa** | Encoder‑only | Improved training, often higher accuracy |
| **DistilBERT** | Encoder‑only | Lightweight, faster, 40% smaller |

### 🔄 Switching models
Replace:

```python
model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
```

With:

```python
model_name = "deepset/roberta-base-squad2"
# or
model_name = "distilbert-base-uncased-distilled-squad"
```

Everything else stays the same.

---

# 4️⃣ Classical ML vs XLNet for Text Classification

**Notebook:** `04_text_classification_classical_vs_xlnet.ipynb`

This notebook compares **traditional NLP classifiers** with **XLNet**, a permutation‑based transformer model.

### 🧩 Classical ML Models Covered
- Logistic Regression  
- Naive Bayes  
- Support Vector Machines  
- TF‑IDF vectorization  
- Bag‑of‑Words vs n‑grams  

### 🧩 XLNet Topics Covered
- XLNet architecture (permutation language modeling)  
- Tokenization with `XLNetTokenizer`  
- Sequence classification with `XLNetForSequenceClassification`  
- Fine‑tuning vs zero‑shot usage  
- Performance comparison with classical ML  

### 🎯 What developers learn
- When classical ML still performs well  
- When transformers outperform traditional methods  
- How XLNet differs from BERT and GPT  
- How to evaluate classification models  

This notebook is a perfect bridge between **traditional NLP** and **modern transformer‑based NLP**.

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

Run any notebook top‑to‑bottom.

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

### 🧩 BERT‑Family QA
- Span‑based question answering  
- Encoder‑only architectures  
- How to switch between BERT, RoBERTa, and DistilBERT  

### 🧩 Classical ML vs XLNet
- Traditional NLP pipelines  
- Transformer‑based classification  
- XLNet’s permutation modeling  
- Practical performance comparisons  

### 🧩 Combined Understanding
You now have a complete foundation in:

- Decoder‑only models (GPT)  
- Encoder‑only models (BERT family)  
- Permutation‑based models (XLNet)  
- Classical NLP vs modern LLMs  
- Hugging Face ecosystem  
- Practical inference workflows  

---

# ⭐ Next Steps

- Add RoBERTa and DistilBERT examples to the QA notebook  
- Add XLNet fine‑tuning examples  
- Add a comparison notebook: **GPT vs BERT vs XLNet**  
- Add a RAG demo (Retrieval‑Augmented Generation)  
- Add LangChain & LangGraph in the next module (`09_llm_application_frameworks`)  

---

