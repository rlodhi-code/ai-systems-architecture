# **LLM Fundamentals**

This module introduces foundational concepts behind modern Large Language Models (LLMs) through practical, hands‑on notebooks. It covers GPT‑based text generation, prompt engineering, embeddings, retrieval‑augmented generation (RAG), and introductory transformer workflows. The goal is to build a working understanding of how LLMs are used, configured, and integrated into applications.

---

## **Module Overview**

The notebooks in this folder explore several core areas of LLM development:

- Text generation using GPT models  
- Prompt design and output control  
- Summarization and keyword extraction  
- Conversational agents and stylistic generation  
- Embeddings and vector stores  
- Retrieval‑augmented generation (RAG)  
- Introduction to transformer‑based architectures  
- Question answering with BERT  
- Text classification with XLNet  

This module serves as a foundation for more advanced AI and NLP engineering work.

---

## **Notebooks Included**

### **1. gpt_models.ipynb**
A hands‑on introduction to GPT‑style models, including:

- API setup and authentication  
- Secure API key loading  
- Prompt‑based text generation  
- Temperature, max tokens, and output shaping  
- Summaries, keyword extraction, and structured outputs  
- A simple poetic chatbot  
- Embeddings and vector store creation  
- Conversational retrieval chains for Q&A  

### **2. transformers_intro.ipynb** *(placeholder)*
Introduces transformer architectures:

- Loading pretrained models  
- Tokenization and encoding  
- Running inference locally  
- Comparing transformer outputs with GPT models  

### **3. bert_question_answering.ipynb** *(placeholder)*
Explores extractive question‑answering:

- BERT‑based QA pipelines  
- Handling context windows  
- Extracting answer spans  
- Evaluating responses  

### **4. xlnet_text_classification.ipynb** *(placeholder)*
Covers text classification using XLNet:

- Loading XLNet classification models  
- Preparing text inputs  
- Running predictions  
- Understanding permutation‑based modeling  

---

## **API Key Management**

This module uses the OpenAI API. The API key must be stored securely and never hard‑coded in notebooks.

### **.env file (recommended approach)**

Create a `.env` file in the root of `08_llm_fundamentals`:

```
OPENAI_API_KEY=your_api_key_here
```

This file should **not** be committed to Git.

### **config.py**

Your `config.py` file loads the environment variable:

```python
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

### **Using the key inside notebooks**

```python
import config
import openai

openai.api_key = config.OPENAI_API_KEY
```

This approach keeps credentials secure, avoids accidental exposure, and maintains clean notebooks.

---

## **Key Code Concepts from gpt_models.ipynb**

### **Text Generation**
```python
def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=10,
        temperature=0.7
    )
    return response.choices[0].text.strip()
```

### **Chat‑Based Summarization**
```python
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Extract keywords from the text."},
        {"role": "user", "content": prompt}
    ]
)
```

### **Retrieval‑Augmented Generation (RAG)**

- Document loading  
- Text splitting  
- Embedding creation  
- FAISS vector store construction  
- Conversational retrieval for Q&A  

---

## **Folder Structure**

```
08_llm_fundamentals/
│
├── gpt_models.ipynb
├── transformers_intro.ipynb
├── bert_question_answering.ipynb
├── xlnet_text_classification.ipynb
├── config.py
├── .env                  (not committed to Git)
├── requirements.txt
└── README.md
```

---

## **Requirements**

A `requirements.txt` file supports reproducibility.  
Typical dependencies include:

```
openai
langchain
faiss-cpu
tiktoken
transformers
torch
beautifulsoup4
requests
python-dotenv
```

Adjust based on the exact imports used in your notebooks.

---

## **Learning Outcomes**

By completing this module, you will:

- Understand how GPT models generate and structure text  
- Learn how to shape model outputs through prompts and parameters  
- Build simple conversational and stylistic agents  
- Apply embeddings and vector stores for retrieval workflows  
- Gain familiarity with transformer‑based pipelines  
- Explore question answering and classification using BERT and XLNet  

---

## **Next Steps**

This module prepares you for deeper work in:

- Fine‑tuning transformer models  
- Semantic search and embedding‑based retrieval  
- Multi‑model evaluation and comparison  
- Practical LLM engineering patterns  

---
