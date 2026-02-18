# 🧠 Text Processing & NLP Foundations  
Part of the **ai-systems-architecture** Series

This section of the **ai-systems-architecture** repository introduces essential Natural Language Processing (NLP) concepts through small, focused projects. Each project builds on the previous one, forming a clear learning path from environment setup to real‑world text analysis.

---

## 📁 Repository Links

**Main GitHub Repo:**  
`https://github.com/rlodhi-code/ai-systems-architecture` [(github.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fgithub.com%2Frlodhi-code%2Fai-systems-architecture")

**This Project Folder:**  
`https://github.com/rlodhi-code/ai-systems-architecture/tree/main/stop_words` [(github.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fgithub.com%2Frlodhi-code%2Fai-systems-architecture%2Ftree%2Fmain%2Fstop_words")

**Jupyter Notebook:**  
`https://github.com/rlodhi-code/ai-systems-architecture/blob/main/stop_words/Stopwords.ipynb` [(github.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fgithub.com%2Frlodhi-code%2Fai-systems-architecture%2Fblob%2Fmain%2Fstop_words%2FStopwords.ipynb")

---

## 🧹 Text Preprocessing Steps Implemented

| Step | Transformation | Example |
|------|----------------|---------|
| 1 | Lowercasing | “Clean Room” → “clean room” |
| 2 | Stopword removal | “the hotel was not clean” → “hotel not clean” |
| 3 | Punctuation removal | “hotel!” → “hotel” |
| 4 | Tokenization | “hotel not clean” → `['hotel', 'not', 'clean']` |
| 5 | Stemming | “cleaned” → “clean” |
| 6 | Lemmatization | “better” → “good” |
| 7 | n‑Grams | “friendly staff” → `('friendly', 'staff')` |

---

## 📚 Project Overview

### **1. Environment Setup (Project 1)**  
The first project in the **ai-systems-architecture** series focuses on:

- Creating a clean Python environment using Anaconda  
- Launching Jupyter Notebook  
- Running a sample notebook to verify the setup  

This ensures a consistent foundation for all future exercises.

---

### **2. Stopwords & Basic Text Cleaning (Project 2)**  
This project introduces:

- What stopwords are  
- Why they matter in NLP  
- How to remove them  
- Additional preprocessing steps (tokenization, stemming, lemmatization, n‑grams)

This serves as a stepping stone for more advanced NLP workflows.

---

### **3. BBC News POS & NER Pipeline (Project 3)**  
A real‑world example applying multiple NLP techniques:

#### **Data Preparation**
- Read `.csv` dataset  
- Convert text to lowercase  
- Remove stopwords  
- Remove punctuation  
- Tokenize  
- Lemmatize  
- Build token lists  

#### **POS — Parts of Speech Tagging**
- Create a spaCy `Doc` object for accurate tagging  
- Extract tokens + POS tags into a DataFrame  
- Compute token frequency  
- Identify:  
  - Most common nouns  
  - Most common verbs  
  - Most common adjectives  

#### **NER — Named Entity Recognition**
- Extract tokens + entity labels into a DataFrame  
- Compute entity frequency  
- Identify:  
  - Most common people  
  - Most common places  

