# 🧠 NLP Custom Classifiers

This project focuses on building and applying **custom machine learning classifiers** for Natural Language Processing (NLP) tasks. It demonstrates how traditional supervised learning algorithms can be effectively used for text classification problems such as sentiment analysis, spam detection, topic classification, and fake news detection.

The project includes practical implementations and applications of:

* Logistic Regression
* Naive Bayes
* Linear Support Vector Machine (Linear SVM)

---

## 📌 Project Overview

Text data is converted into numerical representations using common NLP preprocessing techniques such as:

* Tokenization
* Stopword removal
* Lemmatization
* TF-IDF Vectorization

The transformed features are then used to train and evaluate different classification models.

---

## 🔹 Logistic Regression

Logistic Regression is a **linear classification algorithm** used for binary and multi-class problems.

### Key Characteristics:

* Uses the **sigmoid function** to estimate probabilities
* Outputs class probabilities between 0 and 1
* Works well for linearly separable data
* Efficient and interpretable

### Why It’s Useful in NLP:

Logistic Regression performs strongly with high-dimensional sparse text data (like TF-IDF vectors) and serves as a reliable baseline model for text classification tasks.

---

## 🔹 Naive Bayes

Naive Bayes is a **probabilistic classifier** based on Bayes’ Theorem with the assumption of feature independence.

### Key Characteristics:

* Fast and computationally efficient
* Performs well on text classification tasks
* Works especially well with word frequency features

### Common Variant in NLP:

* Multinomial Naive Bayes (commonly used for document classification)

### Why It’s Useful in NLP:

Despite its “naive” independence assumption, it often delivers surprisingly strong performance for tasks like spam detection and sentiment analysis.

---

## 🔹 Linear Support Vector Machine (Linear SVM)

Linear SVM is a **maximum-margin classifier** that finds the optimal separating hyperplane between classes.

### Key Characteristics:

* Effective in high-dimensional spaces
* Robust to overfitting
* Focuses on maximizing classification margin

### Why It’s Useful in NLP:

Text data is typically high-dimensional and sparse. Linear SVM performs exceptionally well under these conditions and is often one of the strongest traditional ML models for text classification.

---

## 📊 Applications in This Project

This project demonstrates practical applications of the above classifiers in:

* Sentiment analysis
* Fake news classification
* Topic classification
* Custom text classification pipelines

Each model is trained, evaluated, and compared to understand performance trade-offs.

---

## 🛠️ Technologies Used

* Python
* scikit-learn
* pandas
* NumPy
* NLTK / spaCy
* TF-IDF Vectorization

---

## 🎯 Goal of This Project

The primary objective is to:

* Build custom NLP classifiers from scratch using classical ML algorithms
* Compare model performance
* Understand trade-offs between probabilistic and margin-based approaches
* Create reusable pipelines for real-world NLP tasks

---

```markdown
# NLP Custom Classifiers – Sentiment Analysis Baseline

This repository contains a Jupyter notebook demonstrating a **simple end-to-end pipeline** for training traditional machine learning classifiers on a small, custom sentiment analysis dataset.

Part of the **AI Systems Architecture** learning path / experiments.

## Overview

The notebook shows how to:

- Create and prepare a tiny handmade sentiment dataset
- Apply basic **Bag-of-Words (BoW)** text vectorization
- Train and compare three classic ML classifiers:
  - Logistic Regression
  - Multinomial Naive Bayes
  - Linear SVM (via SGDClassifier)
- Evaluate performance using accuracy and classification reports

Goal: illustrate the full workflow of traditional NLP classification before moving to deep learning / transformers.

## Dataset

- **Size**: 20 short sentences (manually created)
- **Classes**: binary sentiment – `positive` (10 samples) / `negative` (10 samples)
- **Examples**:

  Positive:
  - "I love spending time with my friends and family"
  - "Today was such an amazing and productive day"
  - "I feel so grateful for all the support I receive"

  Negative:
  - "I feel so overwhelmed with work and responsibilities"
  - "Nothing seems to be going right lately"
  - "I'm really disappointed with how things turned out"

- No external data files — dataset is hardcoded in the notebook
- Shuffled and split: **70% train / 30% test** (fixed `random_state=7`)

## Techniques Demonstrated

- Text vectorization: `CountVectorizer` (Bag-of-Words, binary counts)
- No stopword removal, no lemmatization, no TF-IDF (intentional baseline simplicity)
- Models from `scikit-learn`:
  - `LogisticRegression`
  - `MultinomialNB`
  - `SGDClassifier` (linear SVM approximation)

## Results Summary

| Model               | Accuracy | Notes                                      |
|---------------------|----------|--------------------------------------------|
| Logistic Regression | 33.33%   | Balanced but very low performance          |
| Multinomial NB      | 33.33%   | Same as logistic — struggles with tiny data|
| Linear SVM (SGD)    | 50.00%   | Best accuracy, but predicts *everything* as negative |

→ Very low scores are **expected** — small synthetic dataset + basic features = poor generalization.

## Notebook Structure

1. Library imports
2. Dataset creation + shuffling
3. Bag-of-Words vectorization → sparse → dense DataFrame
4. Train/test split
5. Training & evaluation of three models
6. Accuracy scores + full classification reports

## Requirements

```bash
pip install pandas scikit-learn
```

- Python ≥ 3.8 recommended (notebook uses 3.11 kernel)

## How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/rlodhi-code/ai-systems-architecture.git
   cd ai-systems-architecture/06_custom_classifier
   ```

2. Open the notebook:
   ```bash
   jupyter notebook nlp_custom_classifiers.ipynb
   # or
   jupyter lab
   ```

3. Run all cells top to bottom.

## Learning Takeaways / Next Steps

- Why tiny handmade datasets are useful for understanding pipelines (but terrible for real performance)
- Limitations of raw BoW vs TF-IDF / n-grams / embeddings
- Class bias can appear even in balanced datasets when data is extremely small
- Good baseline before trying:
  - Larger datasets (IMDB, SST-2, Twitter sentiment, etc.)
  - TF-IDF vectorizer
  - Pretrained embeddings + simple feed-forward net
  - Fine-tuning BERT / DistilBERT

Feel free to extend / improve — PRs welcome!

## License

MIT (or align with the rest of the repo)

Made with ❤️ as part of AI Systems Architecture experiments.
```
