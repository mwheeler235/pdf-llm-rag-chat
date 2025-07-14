## Introduction

Let's build a Chat solution for interfacing with PDF's. 

## What's in the "Big Beautiful Bill Act"?

This Act is easy to find with a quick google search (https://www.congress.gov/bill/119th-congress/house-bill/1/text). Given that the document is quite long and that I'd rather where my data science hat than my legal expert hat, let's leverage some applications and libraries to have a conversation about this Act.

## Tech

1. LangChain: It is a powerful framework of libraries for using large language models effectively.

2. Ollama: It is a platform which allows us to run the large language models locally in our machine, so that we don’t end up paying and using cloud based services to access the LLMs (also keeping data local).

3. OllamaEmbedings (nomic_embed_text): An API provided by Nomic to generate quality embeddings from text data. Embeddings are dense vector representation of text capturing the semantic meaning, enabling tasks like clustering, similarity search and visualization.

4. ChromaDB: Open-source vector database designed for managing querying embeddings.

5. Llama 3.1 LLM: Large language model created by Meta
  
6. Ragas: a library that provides tools to supercharge the evaluation of Large Language Model (LLM) applications. It is designed to help you evaluate your LLM applications with ease and confidence.
