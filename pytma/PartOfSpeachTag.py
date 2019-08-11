import nltk

#
# Universal Part-of-Speech Tagset
#
# Tag	Meaning	English Examples
# ADJ	adjective	new, good, high, special, big, local
# ADP	adposition	on, of, at, with, by, into, under
# ADV	adverb	really, already, still, early, now
# CONJ	conjunction	and, or, but, if, while, although
# DET	determiner, article	the, a, some, most, every, no, which
# NOUN	noun	year, home, costs, time, Africa
# NUM	numeral	twenty-four, fourth, 1991, 14:24
# PRT	particle	at, on, out, over per, that, up, with
# PRON	pronoun	he, their, her, its, my, I, us
# VERB	verb	is, say, told, given, playing, would
# .	punctuation marks	. , ; !
# X	other	ersatz, esprit, dunno, gr8, univeristy

def get_nltk_POS(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    pos_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return pos_dict.get(tag, wordnet.NOUN)

