# coding=utf-8

from stanfordcorenlp import StanfordCoreNLP

_path = r'/Users/liuzhao/Projects/Data/stanford-corenlp'
nlp = StanfordCoreNLP(_path, lang='zh')


def test_nlp():
    fin = open('resources/news.txt', 'r')
    fner = open('resources/ner.txt', 'w')
    ftag = open('resources/tag.txt', 'w')

    for line in fin:
        line = line.strip()
        if len(line) < 1:
            continue
        fner.write(" ".join([each[0]+"/"+each[1] for each in nlp.ner(line) if len(each)==2])+'\n')
        ftag.write(" ".join([each[0]+'/'+each[1] for each in nlp.pos_tag(line) if len(each)==2])+'\n')

    fner.close()
    ftag.close()
    fin.close()

