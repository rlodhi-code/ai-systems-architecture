The nlp_lab has several small projects.  First project helps setup the environment with anaconda and jupyter notebook and has one notebook with some sample code to verify that the environment works. 

Second project introduces the concept of stopwords and provides full introduction. This is a stepping stone and will be used in future exercises. 

Third project "bbc_news_pos_ner" implements a real world use case:
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



