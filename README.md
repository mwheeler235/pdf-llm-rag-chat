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

## Questions & Responses

The first thing I want to know is for the LLM to "Describe the primary objectives of the 'One Big Beautiful Bill Act'".

Reponse:
'''
From the provided text, it seems that the "One Big Beautiful Bill Act" addresses several areas:

1. **Education**: The bill may aim to improve education by providing modifications to low-income housing credit.
2. **Taxation and Business**: It touches upon tax-related issues, such as modifying the gross receipts threshold for small manufacturing businesses and adjusting tax-exempt bond financing requirements.
3. **Economic Development**: By increasing the state housing credit ceiling for certain years, it could aim to stimulate economic growth in low-income areas.

Given these aspects, some primary objectives of the "One Big Beautiful Bill Act" might include:

1. **Economic Growth**: To support economic development, particularly in low-income and rural areas.
2. **Housing Development**: To encourage the construction or rehabilitation of affordable housing units through increased tax credits for developers.
3. **Business Incentives**: To provide incentives for small manufacturing businesses to grow by adjusting their gross receipts thresholds and providing them with more favorable tax conditions.
4. **Economic Stability**: By maintaining a stable economic environment, possibly through modifications in tax policies or financing requirements.'''

Well, then I'm curious - "Would this Act harm any particlar groups of people, and if so which groups?"

Reponse:
'''
1. **Low-income immigrants:** Those from lower socioeconomic backgrounds may struggle more with the increased fees.
2. **Asylum seekers and nonpermanent residents:** These groups might face additional challenges in accessing legal services due to the non-waivability of fees.
3. **Vulnerable populations within immigration applicant pools:** Individuals or families experiencing hardship, including those seeking asylum or nonpermanent residency, might be disproportionately affected by these changes.
'''

Then, obviously I'm also curious - "Resulting from this Act, which groups will benefit most?"