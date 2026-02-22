# 📰 Fake News Categorization — NLP Case Study  
*A practical end‑to‑end project exploring linguistic patterns, sentiment, topics, and classification of fake vs. real news.*

## 📌 Overview  
This project walks through a full Natural Language Processing (NLP) workflow to analyze and categorize fake news. It is based on a structured case study that explores linguistic features, sentiment differences, topic modeling, and finally builds a custom classifier.

The goal is to understand **how fake news differs from real news** and how NLP techniques can be used to detect misleading content.

---

## 📂 Project Structure  
This repository contains the following modules, aligned with the course section:

### **1. Case Study Introduction**  
A brief overview of the dataset, objectives, and the analytical approach.

### **2. Project Setup & Data Exploration**  
- Understanding the dataset  
- Initial observations  
- Preparing text for deeper analysis  

### **3. POS Tag Analysis**  
Using Part‑of‑Speech tagging to explore linguistic patterns in fake vs. real news.

### **4. Named Entity Recognition (NER)**  
Extracting entities (people, places, organizations) to see how fake news differs in entity usage.

### **5. Text Processing Pipeline**  
Tokenization, stopword removal, lemmatization, and normalization steps.

### **6. Sentiment Analysis**  
Comparing sentiment distributions between fake and real news categories.

### **7. Topic Modeling**  
Identifying key themes using:  
- **LDA (Latent Dirichlet Allocation)**  
- **LSA (Latent Semantic Analysis)**  

### **8. Fake News Classifier**  
Building a custom machine‑learning classifier to categorize news articles.

---

## 🛠️ Technologies Used  
- **Python 3.11** (required)  
- **NLTK**  
- **spaCy**  
- **scikit‑learn**  
- **Gensim** (for LDA & LSA topic modeling)  
- **Pandas / NumPy**  
- **Matplotlib / Seaborn**  

---

## 🚀 How to Run the Project  
1. Clone the repository  
2. Create a virtual environment  
3. Install dependencies  
4. Run the notebooks or scripts in order  

```bash
python3.11 -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🎯 Key Learning Outcomes  
- How linguistic features differ between fake and real news  
- How to extract and analyze named entities  
- How sentiment varies across news types  
- How to identify topics using LDA and LSA  
- How to build a custom classifier for fake news detection  

---

## 📘 Status  
This project is part of a larger NLP learning series.  

---
