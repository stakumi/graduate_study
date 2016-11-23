# coding:utf-8

import MeCab
import sys
import gensim

filename= sys.argv
f = open(filename[1],"r")
line = f.readline()
u"""textを形態素解析し、名詞のみのリストを返す"""
tagger = MeCab.Tagger()
sentences = []
while line:
  keywords = []
  #encoded_text = line.encode('utf-8')
  node = tagger.parseToNode(line).next
  line = f.readline()
  while node:
    if node.feature.split(",")[0] == "名詞":
      keywords.append(node.surface)
    node = node.next
  sentences.append(keywords)
f.close
print(sentences)
labeledSentences = gensim.models.doc2vec.LabeledListSentence(sentences)
model = gensim.models.doc2vec.Doc2Vec(labeledSentences, size=100, min_count=0)