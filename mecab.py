# coding:utf-8

import MeCab
import sys
import gensim

from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument


filename= sys.argv
tagger = MeCab.Tagger('-d /home/saito/local/lib/mecab/dic/mecab-ipadic-neologd')
f = open(filename[1],"r")
line = f.readline()
u"""textを形態素解析し、名詞のみのリストを返す"""
sentences = []
training_docs = []
n = 0
while line:
  n += 1 
  keywords = []
  #encoded_text = line.encode('utf-8')
  node = tagger.parseToNode(line).next
  line = f.readline()
  while node:
    if node.feature.split(",")[0] == "名詞":
      keywords.append(node.surface)
    node = node.next
    tag = str(n)
  training_docs.append(TaggedDocument(words=keywords,tags=tag))
  sentences.append(keywords)
f.close
print(sentences)
#labeledSentences = gensim.models.doc2vec.LabeledListSentence(sentences)
#model = gensim.models.doc2vec.Doc2Vec(labeledSentences, size=100, min_count=0)

model = Doc2Vec(documents=training_docs, min_count=1, dm=0)
