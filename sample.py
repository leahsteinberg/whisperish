import unicodedata, random


def make_chain(text):
  chain = {}
  for i in range(len(text)-1):
    if chain.has_key(text[i]):
      chain[text[i]].append(text[i+1])
    else:
      chain[text[i]] = [text[i+1]]
  
  for key in chain.keys():
    word_list = chain[key]
    word_dict = {}
    for word in word_list: # go through each of the values lists
      if word_dict.has_key(word):
        word_dict[word]+=1
      else:
        word_dict.update({word: 1})
    total_words = 0
    for value in word_dict.values():
      total_words+=value
    for word in word_dict.keys():
      #change from count of that word to percentage
      word_dict[word] = float(word_dict[word])/float(total_words)
    chain[key] = word_dict
    key_list = []
    for key in chain.keys():
      key_list.append(key)
  generate_text(chain)




def generate_text(chain):
  text = ''
  word = start_word(chain)
  text+=word
  for i in range(40):
    word = next_word(word, chain)
    text+=' ' + word
  text+='.'
  print text
  return text

def get_key_count(chain, word):
  num_words = 0
  for key in chain.keys():
    num_words+=1
  return num_words


def start_word(chain):
  num_words = 0
  for key in chain.keys():
    num_words+=1
  index = random.randrange(0, num_words)
  start_word = chain.keys()[index]
  return start_word


def next_word(word, chain):
  rand_num = random.randrange(10)*.1
  word_dict = chain[word]
  prob_num=0
  for entry in word_dict.keys():
    prob_num+=word_dict[entry]
    if rand_num < prob_num:
      return entry


def get_text(text):
  text2 = text#.encode('ascii', 'ignore')
  #print "~~~~"
  text3 = ''
  for c in text2:
    text3+=c
  text = text3.split(' ')
  text2 = []
  for word in text:
    if '@' in word or 'http' in word or word[:8] == 'nyti.ms/' or 'RT' in word or word == ' ' or word == '':
      pass
    else:
      text2.append(word)
  make_chain(text2)












