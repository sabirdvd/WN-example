from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn


file1 = []

file2 = []

#original the word is here 
with open('word.txt','rU') as f:
        
    for line in f:
        #print line.rstrip()
       file1.append(line.rstrip())


#original the cpation is here 
with open('caption.txt','rU') as f1:    
    
    for line1 in f1:
       #print line1.rstrip()
       file2.append(line1.rstrip())
       #break

 
def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'
 
    if tag.startswith('V'):
        return 'v'
 
    if tag.startswith('J'):
        return 'a'
 
    if tag.startswith('R'):
        return 'r'
 
    return None
 
def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None
 
    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None
 
def sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))
 
    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
 
    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
 
    score, count = 0.0, 0
 
    # For each word in the first sentence
    for synset in synsets1:

        
        try :
        # Get the similarity value of the most similar word in the other sentence
            best_score = max([synset.path_similarity(ss) for ss in synsets2])

            #if best_score is not None:
            #    score += best_score
            #    count += 1
 
        except: 
            #best_score = None 
 
        # Check that the similarity could have been computed

    # Average the values
    #score /= count
            return 0

        if best_score is not None:
                score += best_score
                count += 1
    return score 
     
 
f=open('word_net_LSTM-w1.txt', "w")

for i in range(len(file1)):
    temp =[]

    try :
        #w = model.similarity(file1[i],file2[i])
        #w = sentence_similarity(file1[i], file2[i])
        # Reverse sim
        # Run the similarity
        w = sentence_similarity(file2[i], file1[i])
    except KeyError : 
        print('out_of_dict')
        w = 0 
    #w =  float(file1[i])**(1-float(file2[i])//1+float(file2[i]))
    #w = (file1[i])**(1-(file2[i])//(1+(file2[i])))
    print "1", file1
    print "2", file2
    temp.append(w)
    result= file1[i]+','+file2[i]+','+str(w)
    #result = file1[i]+',',+file2[i]+','+(w)
    f.write(result)
    f.write('\n')
    print w
f.close()



