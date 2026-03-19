import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import math

stop_words = set(ENGLISH_STOP_WORDS)
stop_words.update('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

ALNUM_RE = re.compile(r'[^a-z0-9]+')

class VectorCompare:
    def concordance(document):
        if type(document) != str:
            raise ValueError('Supplied Argument should be of type String')
        con = {}
        for word in document.split():
            if word in stop_words:
                continue
            if word in con:
                con[word] = con[word] + 1
            else:
                con[word] = 1
        return con

    def magnitude(self, concordance):
        if type(concordance) != dict:
            raise ValueError('Supplied Argument must be of type dict')
        total = 0
        for word, count in iter(concordance):
            total += count ** 2
        return math.sqrt(total)
    
    def relation(self, concordance1, concordance2):
        if type(concordance1) != dict:
            raise ValueError('Supplied Argument 1 should be of type dict')
        if type(concordance2) != dict:
            raise ValueError('Supplied Argument should be of type dict')
        relevance = 0
        topvalue = 0


v = VectorCompare()

doc1_path = '/Users/rino/Downloads/The Reconstruction of Black Servitude (2).txt'
doc2_path = '/Users/rino/Downloads/02WBAI Ch2.txt'
with open(doc1_path, 'r', encoding='utf-8') as f:
    doc1_content = f.read()
    doc1_content = doc1_content.lower()
    doc1_content = re.sub(ALNUM_RE, " ", doc1_content)
with open(doc2_path, 'r', encoding='utf-8') as f:
    doc2_content = f.read()
    doc2_content = doc2_content.lower()
    doc2_content = re.sub(ALNUM_RE, " ", doc2_content)
word_count_path1 = concordance(doc1_path)
word_count_content1 = concordance(doc1_content)
word_count_path2 = concordance(doc2_path)
word_count_content2 = concordance(doc2_content)
#print("Word Count for Document Path:", word_count_path1)
#print("\nWord Count for Document content: ", word_count_content1)
print("Word Count for Document Path:", word_count_path2)
print("\nWord Count for Document content: ", word_count_content2)
top_words = sorted(word_count_content1.items(), key=lambda x: x[1], reverse=True)[:10]
print(top_words)

