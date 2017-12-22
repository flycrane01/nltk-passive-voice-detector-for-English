import nltk

def isPassive(sentence):
    beforms = ['am', 'is', 'are', 'been', 'was', 'were', 'be', 'being']               # all forms of "be"
    aux = ['do', 'did', 'does', 'have', 'has', 'had']                                  # NLTK tags "do" and "have" as verbs, which can be misleading in the following section.
    words = nltk.word_tokenize(sentence)
    tokens = nltk.pos_tag(words)
    tags = [i[1] for i in tokens]
    if tags.count('VBN') == 0:                                                            # no PP, no passive voice.
        return False
    elif tags.count('VBN') == 1 and 'been' in words:                                    # one PP "been", still no passive voice.
        return False
    else:
        pos = [i for i in range(len(tags)) if tags[i] == 'VBN' and words[i] != 'been']  # gather all the PPs that are not "been".
        for end in pos:
            queue = tags[:end]
            start = 0
            backup = queue[:]
            for i in range(len(backup) - 1, 0, -1):
                last = queue.pop()
                if last == 'NN' or last == 'PRP':
                    start = i + 1                                                          # get the chunk between PP and the previous NN or PRP (which in most cases are subjects)
            sentchunk = words[start:end]
            tagschunk = tags[start:end]
            verbspos = [i for i in range(len(tagschunk)) if tagschunk[i].startswith('V')] # get all the verbs in between
            if verbspos != []:
                for i in verbspos:
                    if sentchunk[i].lower() not in beforms and sentchunk[i].lower() not in aux:  # check if they are all forms of "be" or auxiliaries such as "do" or "have".
                        break
                else:
                    return True
    return False


if __name__ == '__main__':

    samples = '''I like being hunted.
    The man is being hunted.
    Don't be frightened by what he said.
    I assume that you are not informed of the matter.
    Please be advised that the park is closing soon.
    The book will be released tomorrow.
    We're astonished to see the building torn down.
    The hunter is literally being chased by the tiger.
    He has been awesome since birth.
    She has been beautiful since birth.'''                                                   # "awesome" is wrongly tagged as PP. So the sentence gets a "True".

    sents = nltk.sent_tokenize(samples)
    for sent in sents:
        print(sent + '--> %s' % isPassive(sent))