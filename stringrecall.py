word = "Bobo mo L"
word2 = ["franz", "lance" , "cj", "brent"]
new_word2 = set (word2)
strip_word = "       stripper"

word_len = len(word)
word_rep = word.replace("Franz","Lance")
word2_join = " , ".join(word2)
word_stripped = strip_word.strip()
s_with = word.startswith("F")
e_with = word_rep.endswith("B")
w_find = word.find("B")
w_find2 = word.find("L") #-1 kasi wala bobo
w_rfind = word.rfind("o")
w_rfind2 = word.rfind("B")
w_index = word.index("B") #walang neggative kasi basta
w_index2 = word.index("L")
w_rindex = word.rindex("o")
w_rindex2 = word.rindex("B")


print(word_len)
print(word_rep)
print(word2_join)
print(",".join(new_word2))
print(word_stripped)
print(s_with)
print(e_with)
print(w_find , w_find2)
print(w_rfind, w_rfind2)
print(w_index, w_index2)
print(w_rindex, w_rindex2)