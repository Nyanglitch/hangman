import hangman as h

def test_word_length():
    word = "testword"
    hword = h.hide_word(word)
    assert len(hword) == len(word)

def test_good_word():
	word = "testword"
	assert h.word_validation(word) == True

def test_bad_word():
	word = "tesT  1w_ord"
	assert h.word_validation(word) == False
