# 📘 Retrieval-Augmented Generation (RAG): Indexing, Retrieval & Generation

This repository follows a structured **Learning Path** for building Retrieval‑Augmented Generation (RAG) systems. It covers the full workflow:

1. **Indexing**  
2. **Retrieval**  
3. **Generation**

Each section includes conceptual explanations and code patterns that match the notebook examples you are working with (similarity search, MMR search, vectorstore-backed retrievers, stuffing, and response generation).

---

# 🧭 The Learning Path

---

# 1️⃣ Indexing

Indexing prepares raw documents so they can be efficiently retrieved later. This includes splitting text, embedding it, and storing it in a vector database.

---

## 1.1 Document Splitting with Character Text Splitter (Theory)

Large documents must be broken into smaller, semantically meaningful chunks.  
A **CharacterTextSplitter** divides text based on character count, with optional overlap.

**Why this matters:**

- Prevents context overflow  
- Improves embedding quality  
- Ensures retrieval returns focused, relevant chunks  

---

## 1.2 Document Splitting with Character Text Splitter (Code)

```python
from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separator="\n"
)

chunks = splitter.split_text(raw_text)
```

---

## 1.3 Document Splitting with Markdown Header Text Splitter

Markdown documents contain hierarchical structure.  
A **MarkdownHeaderTextSplitter** preserves this structure by splitting based on headers.

Useful for:

- Technical documentation  
- Lecture notes  
- Multi-section articles  

---

## 1.4 Text Embedding with OpenAI

Each chunk is converted into a vector representation using an embedding model.

```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vectors = embeddings.embed_documents(chunks)
```

---

## 1.5 Creating a Chroma Vectorstore

Chroma is a lightweight, fast vector database ideal for local RAG workflows.

```python
from langchain_chroma import Chroma

vectorstore = Chroma.from_texts(
    texts=chunks,
    embedding=embeddings,
    collection_name="my_docs"
)
```

---

## 1.6 Inspecting & Managing Documents in a Vectorstore

You can inspect:

- Stored metadata  
- Number of documents  
- Embedding dimensions  
- Filters  

This is essential for debugging retrieval behavior.

---

# 2️⃣ Retrieval

Retrieval determines **which documents** are passed to the LLM.  
This learning path covers two major retrieval strategies:

- **Similarity Search**  
- **Maximal Marginal Relevance (MMR) Search**

---

## 2.1 Similarity Search

Similarity search retrieves the top‑k documents most similar to the query based on cosine similarity.

### What It Does

- Finds the closest matches  
- Prioritizes relevance  
- Does **not** consider redundancy  

### Example Code

```python
retrieved_docs = vectorstore.similarity_search(
    query_question,
    k=3,
    filter={"Lecture Title": "Programming Languages & Software Employed in Data Science - All the Tools You Need"}
)

for d in retrieved_docs:
    print(d.page_content, d.metadata)
```

### When to Use It

- When you want the most relevant chunks  
- When redundancy is acceptable  
- When the dataset is small or uniform  

---

## 2.2 Maximal Marginal Relevance (MMR) Search

MMR balances **relevance** and **diversity**.

### What It Does

- Avoids returning repetitive chunks  
- Ensures coverage of different subtopics  
- Improves context quality for generation  

### Example Code (from your notebook)

```python
retrieved_docs = vectorstore.max_marginal_relevance_search(
    query_question,
    k=3,
    lambda_mult=0.1,
    filter={"Lecture Title": "Programming Languages & Software Employed in Data Science - All the Tools You Need"}
)
```

### What the Output Shows

Your retrieved pages cover:

1. Programming languages (R, C, Python)  
2. Big data tools (Hadoop, HBase, MongoDB)  
3. Summary of applicability  

This is exactly the behavior expected from MMR — diverse, non‑redundant context.

---

## 2.3 Vectorstore‑Backed Retriever

LangChain allows you to wrap your vectorstore into a retriever object:

```python
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0.1}
)
```

This makes retrieval plug‑and‑play inside chains.

---

# 3️⃣ Generation

Once documents are retrieved, they must be passed to the LLM in a structured way.

---

## 3.1 Stuffing Documents

"Stuffing" means concatenating all retrieved documents into a single prompt.

Pros:

- Simple  
- Works well for small k  

Cons:

- Can exceed context window  
- No structure  

Example:

```python
context = "\n\n".join([d.page_content for d in retrieved_docs])
```

---

## 3.2 Generating a Response

Finally, the LLM uses the stuffed context to answer the query.

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

response = llm.invoke(
    f"Use the context below to answer the question.\n\nContext:\n{context}\n\nQuestion: {query_question}"
)

print(response)
```

---

# 📚 Summary of the Learning Path

| Section | Topic |
|--------|--------|
| Indexing | Character splitter (theory + code) |
| Indexing | Markdown header splitter |
| Indexing | Embeddings with OpenAI |
| Indexing | Creating a Chroma vectorstore |
| Indexing | Inspecting vectorstores |
| Retrieval | Similarity search |
| Retrieval | Maximal Marginal Relevance (MMR) search |
| Retrieval | Vectorstore-backed retriever |
| Generation | Stuffing documents |
| Generation | Generating a response |

---
