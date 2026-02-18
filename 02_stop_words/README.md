rlodhi-code (github) - https://github.com/rlodhi-code/nlp_lab

This project.
https://github.com/rlodhi-code/nlp_lab/tree/main/stop_words

Link to jupyter notebook.
https://github.com/rlodhi-code/nlp_lab/blob/main/stop_words/Stopwords.ipynb

Following steps have been implemented in this project. 
Step  	Transformation				Example
1     	Lowercasing					“Clean Room” --> “clean room”
2     	Stopword removal			“the hotel was not clean” --> “hotel not clean”
3 		Punctuation removal			“hotel!” --> “hotel”
4 		Tokenization 				“hotel not clean” --> ['hotel', 'not', 'clean']
5 		Stemming 					“cleaned” --> “clean”
6 		Lemmatization 				“better” --> “good”
7 		n-Grams 					“friendly staff” --> ('friendly', 'staff')


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



