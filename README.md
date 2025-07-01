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

The first thing I want to know is for the LLM to "Describe the primary objectives of this Act".

Response:
***Some potential objectives of this Act could include:

1. Improving transparency in pharmacy benefit management
2. Enhancing accountability among pharmacy benefit managers
3. Protecting patients' access to prescription medications
4. Reducing costs associated with pharmacy benefit management
5. Promoting fair business practices within the industry***

Additionally, "What is the most controversial objective within this Act?"

Response:
```
Based on the provided text, it appears that the most controversial objective within this Act may be the "PROHIBITING WAIVER OF COMMUNITY ENGAGEMENT REQUIREMENTS" section (subsection 44141(10)). This section restricts states from waiving certain community engagement requirements for individuals receiving Medicaid benefits. The controversy surrounding this section is likely due to its potential impact on individual freedoms and autonomy, as well as the possibility that it may be overly restrictive or burdensome.
```

Well, then I'm curious - "Resulting from this Act, which groups would be harmed most?"

Response:
```
**Medicaid Expansion**

* The groups that could be harmed are those who might not benefit from Medicaid expansion or might lose some of their current benefits:
	+ Individuals with higher incomes who currently receive Medicaid benefits (if they exceed income limits, they might no longer qualify)
	+ Those who have private health insurance and don't need Medicaid
	+ Businesses or organizations that provide healthcare services to those who would no longer be covered by Medicaid

**Work Requirements**

* Low-income individuals and families with dependents:
	+ The work requirements could make it more difficult for them to access healthcare, especially if they don't have stable employment or transportation.
	+ Those who are elderly, disabled, or have caregiving responsibilities might find it challenging to meet the work requirements.

**Changes to Medicaid**

* Long-term care facilities and providers of in-home care services:
	+ The changes to Medicaid's cost-sharing requirements for certain expansion individuals could lead to reduced reimbursement rates for these providers.
	+ This might result in less funding for home- and community-based services, affecting the elderly or disabled individuals who rely on them.

**Changes to the Healthcare System**

* Undocumented immigrants and their families:
	+ The Act does not provide a clear pathway for undocumented immigrants to access healthcare or Medicaid benefits.
	+ This could leave them without access to essential medical care and exacerbate existing health disparities.
```
