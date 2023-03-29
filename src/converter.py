# main
import argparse
import eng_to_ipa as ipa
import re

def SenSep(sen: str) -> list:
    """Separates sentence into words"""
    import nltk
    nltk.download('punkt')
    sentence = sen
    return nltk.word_tokenize(sentence)


def Eng2IPA(sen: str) -> str:
    """Converts English word to IPA"""
    result = ipa.convert(sen, keep_punct=True)
    return result


def dict_match(item: str) -> bool:
    """Checks if item is in dictionary"""
    pass



def convert(item: str) -> str:
    """Converts IPA to Romaji"""
    while 'dz' in item:
        item = item.replace('dz', 'ッズ')
    while 'tu' in item:
        item = item.replace('tu', 'ツ')
    while 'tɪ' in item:
        item = item.replace('ti', 'ティ')
    while 'dɪ' in item:
        item = item.replace('ti', 'ディ')
    # while
    return item

def Ipa2Romaji(sen: str) -> str:
    """Converts IPA to Romaji"""
    IPA_sep = SenSep(sen)
    for item in IPA_sep:
        # punctuation detection with re
        # if item is punctuation:
        if re.match(r'[?!.,]', item):
            pass
        elif dict_match(item):
            # first lookup in dictionary
            pass
        else:
            result = convert(item)




def main():
    pass



if __name__ == '__main__':
    sen = "disney, tissue"
    IPA = Eng2IPA(sen)
    print(IPA)
    IPA_sep = SenSep(IPA)
    print(IPA_sep)
    romaji = Ipa2Romaji(IPA)



