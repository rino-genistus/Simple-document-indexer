import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import math
from os import listdir
import pprint

stop_words = set(ENGLISH_STOP_WORDS)
stop_words.update('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

ALNUM_RE = re.compile(r'[^a-z0-9]+')

base_dir = '/Users/rino/Downloads/' #Set the Base Directory where you want to search for your files.

items = listdir(base_dir)
#print(items)
items = [item for item in items if item.split('.')[-1] == 'txt']
"""for item in items:
    print(item + '\n')"""

class VectorCompare:
    def concordance(self, document):
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
        for word, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)
    
    def relation(self, concordance1, concordance2):
        if type(concordance1) != dict:
            raise ValueError('Supplied Argument 1 should be of type dict')
        if type(concordance2) != dict:
            raise ValueError('Supplied Argument should be of type dict')
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                topvalue += count * concordance2[word]
        if (self.magnitude(concordance1) * self.magnitude(concordance2)) != 0:
            return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))
        else:
                return 0


v = VectorCompare()

"""doc1_path = '/Users/rino/Downloads/The Reconstruction of Black Servitude (2).txt'
doc2_path = '/Users/rino/Downloads/02WBAI Ch2.txt'
with open(doc1_path, 'r', encoding='utf-8') as f:
    doc1_content = f.read()
    doc1_content = doc1_content.lower()
    doc1_content = re.sub(ALNUM_RE, " ", doc1_content)
with open(doc2_path, 'r', encoding='utf-8') as f:
    doc2_content = f.read()
    doc2_content = doc2_content.lower()
    doc2_content = re.sub(ALNUM_RE, " ", doc2_content)

word_content_dict = {doc1_path:doc1_content, doc2_path:doc2_content}
word_count_path1 = v.concordance(doc1_path)
word_count_content1 = v.concordance(doc1_content)
word_count_path2 = v.concordance(doc2_path)
word_count_content2 = v.concordance(doc2_content)
documents = [doc1_path, doc1_content, doc2_path, doc2_content]"""
word_content_dict = {}
documents = []
#print(items[:5])
for item in items:
    """if item.split('.')[-1] != 'txt':
        continue
    else:"""
    try:
        with open(base_dir + item, 'r', encoding='utf-8') as f:
            print(item)
            doc_content = f.read()
            doc_content = doc_content.lower()
            doc_content = re.sub(ALNUM_RE, " ", doc_content)
            doc_content = re.sub(r'(\d+)', r' \1 ', doc_content)

            file_name = item.lower()
            file_name = re.sub(r'(\d+)', r' \1 ', file_name)
            clean_file_name = re.sub(ALNUM_RE, " ", file_name)
            weighted_file_name = (clean_file_name + " ") * 15

            combined_text = weighted_file_name + doc_content
        word_content_dict[base_dir + item] = combined_text
        documents.append(base_dir + item)
        documents.append(doc_content)
    except Exception as e:
        print(e)
index = {doc_path: v.concordance(doc_content) for doc_id, (doc_path, doc_content) in enumerate(word_content_dict.items())}
#index.update({doc_path: v.concordance(doc_path) for doc_id, (doc_path, doc_content) in enumerate(word_content_dict.items())})
#top_words = sorted(word_count_content1.items(), key=lambda x: x[1], reverse=True)[:10]
search_term = input('Enter Search term: ')
matches = []
search_concordance = v.concordance(search_term.lower())

for doc_name, concordance in index.items():
    relation = v.relation(search_concordance, concordance)
    if relation != 0:
        #print(documents[i])
        #match = [doc_name.split('/')[-1] for doc_name, doc_content in word_content_dict.items() if doc_content == documents[i]]
        #print(match)
        match = doc_name.split('/')[-1]
        matches.append((relation, match))

matches.sort(reverse=True)

print("Matches: ", matches)



#print("DEBUG DEBUG DEBUG")
#print("DOCUMENTS: ", documents)
#print("WORD_CONTENT_DICT: ", word_content_dict)
#print("INDEX", index)
#print("ITEMS", items)
