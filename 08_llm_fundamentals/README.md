# 🤖 LLM Fundamentals — GPT Models & Hugging Face Transformers

This module provides a hands‑on introduction to **Large Language Models (LLMs)** using two complementary approaches:

1. **OpenAI GPT Models** — API‑based inference  
2. **Hugging Face Transformers** — local or hosted model execution  

Both notebooks demonstrate practical, real‑world usage patterns including prompting, configuration management, environment variables, and safe handling of API keys.

---

## 📁 Project Structure

```
08_llm_fundamentals/
│
├── gpt_models.ipynb                 # OpenAI GPT examples
├── huggingface_transformers.ipynb   # Hugging Face Transformers examples
├── config.py                        # Loads environment variables (HF_TOKEN, etc.)
├── .env                             # API keys (not committed)
└── README.md                        # This file
```

---

# 1️⃣ GPT Models Notebook (OpenAI API)

This notebook walks through how to interact with GPT models using the OpenAI Python SDK.

### 🔍 Topics Covered

- Setting up API keys securely  
- Using `OpenAI()` client  
- Chat completions  
- System vs. user messages  
- Temperature, max tokens, and other parameters  
- Prompt engineering basics  
- Error handling and rate‑limit considerations  

### 🧠 Key Concepts

- **Stateless API calls** — each request includes full context  
- **Determinism vs. creativity** — controlled via temperature  
- **Token budgeting** — important for long prompts  
- **Model selection** — choosing between GPT‑4, GPT‑4o, GPT‑3.5, etc.  

### 🔐 Environment Variables

The notebook expects:

```
OPENAI_API_KEY=your_key_here
```

Stored in `.env` and loaded automatically.

---

# 2️⃣ Hugging Face Transformers Notebook

This notebook demonstrates how to run LLMs using the **Transformers** library — either locally or via Hugging Face Inference Endpoints.

It includes several important comments explaining *why* certain steps are taken, how to avoid common pitfalls, and how to structure your code for clarity.

---

## 🔧 Setup & Configuration

### 1. Save your Hugging Face token in `.env`

Create a `.env` file:

```
HF_TOKEN=your_huggingface_token
```

### 2. How the token is loaded

The notebook imports:

```python
from config import HF_TOKEN
```

Your `config.py` handles:

- Reading `.env`
- Validating required variables
- Exposing them as Python constants

This keeps notebooks clean and avoids hard‑coding secrets.

---

## 🚀 Topics Covered in the Transformers Notebook

### ✔️ Loading Models & Tokenizers

- AutoModelForCausalLM  
- AutoTokenizer  
- Pipeline API  
- Device mapping (CPU/GPU/MPS)  

### ✔️ Running Inference

- Text generation  
- Adjusting max_length, temperature, top_p  
- Batch inference  
- Handling long prompts  

### ✔️ Using Hugging Face Hub

- Authenticating with `HF_TOKEN`  
- Loading private models  
- Pulling models from the Hub  
- Understanding model sizes & hardware requirements  

### ✔️ Performance Considerations

- GPU vs CPU execution  
- Quantization (8‑bit, 4‑bit)  
- Memory footprint  
- Why some models load slowly  

### ✔️ Practical Notes Included in the Notebook

The notebook contains several helpful comments such as:

- Why tokenizers must match the model  
- Why pipelines simplify inference for beginners  
- How to avoid out‑of‑memory errors  
- Why some models require `trust_remote_code=True`  
- When to use local inference vs hosted endpoints  

All of these insights are preserved and reflected in this README.

---

# 🔒 Security & Environment Management

### `.env` is required for both notebooks

```
OPENAI_API_KEY=...
HF_TOKEN=...
```

### `.env` is **never committed**  
Your `.gitignore` already protects it.

### `config.py` centralizes all secrets  
This ensures:

- No secrets inside notebooks  
- Cleaner code  
- Easier debugging  
- Consistent environment handling  

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

### 3. Start Jupyter

```bash
jupyter notebook
```

Open:

- `gpt_models.ipynb`
- `huggingface_transformers.ipynb`

Run cells top‑to‑bottom.

---

# 📘 Learning Outcomes

By completing both notebooks, you will understand:

### 🧩 GPT Models (OpenAI)
- How to call hosted LLMs via API  
- How to structure prompts  
- How to control model behavior  
- How to manage tokens and cost  

### 🧩 Hugging Face Transformers
- How to run models locally  
- How to load models from the Hub  
- How tokenizers and models work together  
- How to configure generation parameters  
- How to authenticate and access private models  

### 🧩 Combined Understanding
You now have a complete view of:

- **Hosted LLMs** (OpenAI)  
- **Local / open‑source LLMs** (Transformers)  
- **Secure configuration**  
- **Practical inference workflows**  

---

# ⭐ Future Enhancements

- Add examples using **Hugging Face Inference Endpoints**  
- Add quantization examples (4‑bit, 8‑bit)  
- Add RAG (Retrieval‑Augmented Generation) demo  
- Add evaluation metrics (BLEU, ROUGE, perplexity)  
- Add comparison of model families (LLaMA, Mistral, Phi‑3, etc.)  

---
