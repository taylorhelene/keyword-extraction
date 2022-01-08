# import the gensim module and keywords function
from gensim.summarization import keywords
# Paragraph
paragraph = "Natural language processing (NLP) is the ability of a computer program to understand human language as it is spoken. NLP is a component of artificial intelligence (AI). The development of NLP applications is challenging because computers traditionally require humans to 'speak' to them in a programming language that is precise, unambiguous and highly structured, or through a limited number of clearly enunciated voice commands. Human speech, however, is not always precise -- it is often ambiguous and the linguistic structure can depend on many complex variables, including slang, regional dialects and social context."
# Get the keywords from the paragraph 
keywords_txt = keywords(paragraph) 
print(keywords_txt) 