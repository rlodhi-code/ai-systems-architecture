Description: "bbc_news_pos_ner" implements a real world use case:
* reads a data file in .csv format
* converts to lowercase
* removes stop words
* removes punctuation
* toknize
* lemmatizing 
* create lists for tokens
* POS - parts of speech tagging
	* creates a spacy doc from raw text - better for pos tagging
	* extracts the tokens and pos tags into a dataframe
	* token frequency count
	* builds most common nouns
	* most common verbs
	* most common adjectives
* NER - named entity recognition
	* extract the tokens and entity tags into a dataframe
	* token frequency count
	* most common people
	* most common places


Link to Jupyter Notebook: https://github.com/rlodhi-code/ai-systems-architecture/blob/main/03_bbc_news_pos_ner/bbc_news_pos_ner.ipynb




