# nltk-passive-voice-detector-for-English
## 中文说明
依赖于NLTK库，感谢前人的贡献。

本脚本可以识别出英语文本中的被动语态，包括主句和从句。

被动语态识别规则：
* 若一个句子中没有被动分词，则该句不可能是被动句 *
* 若一个句子中仅有一个被动分词且其为“been”，则该句不可能为被动句 eg: He has been a teacher since 2000.
* 若一个句子中至少含有一个“been”之外的过去分词，且该过去分词到前方最近的人称代词或名词之间的所有动词均为be的某种形式，则该句中存在被动语态。

由于缺乏测试集，仅在少量文本中验证，正确率尚可。如果谁有大规模进行过被动语态标注的语料库，欢迎使用此脚本验证其正确识别比例。

主要缺点：所有的工作均在NLTK的词性标注下进行，词性标注的正确率直接影响后续工作的正确率。若想达到最佳效果，恐怕需要单独训练一个识别正确率正高的标注工具。

## Introduction
This script is based on NLTK. Sincerest gratitude goes to the predecessors.

As its name suggests, this script can automatically detect passive voice in English texts, be it in matrix clause or relative clause.

Rules of detection:
* If there is no PP in a sentence, the sentence can't be passive.
* If there is only one PP in a sentence and it is "been", the sentence can't be passive. eg: He has been a teacher since 2000.
* If there is at least one PP other than "been" in a sentence, and all the verbs between the PP(s) and the nearest preposition or noun in front are a certain form of "be", the sentence is passive.

(PP is short for "past participle")

Due to a lack of large passive-voice-annotated corpora, the script is only examine on small-scale texts and the success rate is acceptable.

A major drawback of this script is that all the work is entirely based on the POS_TAGGER of NLTK, whose accuracy determines the quality of the following work. To acheive the maximum efficiency, a tailor-made tagger must be trained first.
