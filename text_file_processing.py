import string


def create_unigram_list(text_file):
    file = open(text_file, "r")
    text = file.read().lower()
    translation = str.maketrans('', '', string.punctuation)
    normalised_text = text.translate(translation)
    normalised_unigram_list = normalised_text.split()
    file.close()

    return normalised_unigram_list


def create_bigrams_and_trigrams(normalized_unigram_list):
    bigram_list = []
    trigram_list = []
    for idx, unigram in enumerate(normalized_unigram_list):
        if idx < len(normalized_unigram_list)-1:
            next_unigram = normalized_unigram_list[idx+1]
            bigram_list.append(' '.join([unigram,
                                         next_unigram]))
            if idx < len(normalized_unigram_list)-2:
                scnd_next_unigram = normalized_unigram_list[idx+2]
                trigram_list.append(' '.join([unigram,
                                              next_unigram,
                                              scnd_next_unigram]))

    return bigram_list, trigram_list


def create_frequency_dict(ngram_list):
    freq_dict = {}
    for ngram in ngram_list:
        if ngram not in freq_dict.keys():
            freq_dict[f'{ngram}'] = 1
        else:
            freq_dict[f'{ngram}'] += 1

    return freq_dict
