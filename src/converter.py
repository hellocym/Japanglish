# main
import argparse
import eng_to_ipa as ipa
import re

def SenSep(sen: str) -> list:
    """Separates sentence into words"""
    import nltk
    nltk.download('punkt', quiet=True)
    sentence = sen
    return nltk.word_tokenize(sentence)


def Eng2IPA(sen: str) -> str:
    """Converts English word to IPA"""
    result = ipa.convert(sen, keep_punct=True)
    return result


def dict_match(item: str) -> bool:
    """Checks if item is in dictionary"""
    pass
    return False

replace_list_ordered = [
    ('dz', 'zzu'),
    ('tu', 'to~u'),
    ('tɪ', 'ti'),
    ('dɪ', 'di'),
    ('w', 'u~'),
    ('fr', 'fur'),
    ('f', 'f'),
    ('θ', 'sh'),
    ('ð', 'z'),
    ('ʃ', 'sh'),

    ('ld', 'rudo'),
    ('l', 'r'),
    ('ŋ', 'n'),
    ('ˈv', 'v'),
    ('v', 'b'),
    ('eɪ', 'ei'),
    ('aɪ', 'ai'),
    ('ɔɪ', 'oi'),
    ('oʊ', 'ō'),
    ('aʊ', 'au'),
    ('ɪr', 'ia'),
    ('kɛ', 'kya'),
    ('ɛr', 'ea'),
    ('ʊr', 'uā'),
    ('ɑr', 'ā'),
    ('i', 'ī'),
    ('ɔr\0', 'oa'),
    ('ɔr', 'ō'),
    ('ər', 'ā'),
    ('ju', 'yū'),
    ('u', 'ū'),
    ('ɪ', 'i'),
    ('ɛ', 'e'),
    ('kæ', 'kya'),

    ('æ', 'a'),
    ('ɑ', 'o'),
    ('ʊ', 'u'),
    ('t\0', 'tto'),
    ('d\0', 'do'),
    ('p\0', 'ppu'),
    ('m\0', 'mu'),
    ('g\0', 'gu'),
    ('ks\0', 'kkusu'),
    ('k\0', 'kku'),
    ('s\0', 'su'),
    ('b\0', 'bu'),

]


def split(item):
    """Splits item into list of tuples"""
    for (a, b) in replace_list_ordered:
        clear = False
        while not clear:
            clear = True
            for loc, seg in enumerate(item):
                # print(seg)
                seg_str, seg_bool = seg
                if seg_bool:  # if already split and replaced
                    continue
                result = [_.start() for _ in re.finditer(a, seg_str)]
                if result:
                    clear = False
                    i = result[0]

                    # print(seg_str, a, b)
                    # print(f"replacing {a} with {b} at {i}")
                    
                    iloc = loc

                    # print(iloc)

                    pre = [(seg_str[:i], False)] if seg_str[:i] else []
                    post = [(seg_str[i + len(a):], False)] if seg_str[i + len(a):] else []

                    item = item[:iloc] + pre + [(b, True)] + post + item[iloc + 1:]

                    # print(item)



    return ''.join([x for x, y in item])

def convert(item: str) -> str:
    """Converts IPA to Romaji"""
    item += '\0'
    item = [(item, False)]
    item = split(item)
    return item.replace('ˈ', '').strip('\0')


def Ipa2Romaji(sen: str) -> str:
    """Converts IPA to Romaji"""
    IPA_sep = SenSep(sen)
    Ja = []
    for item in IPA_sep:
        # punctuation detection with re
        # if item is punctuation:
        if re.match(r'[?!.,]', item):
            result = item
        elif dict_match(item):
            # first lookup in dictionary
            pass
        else:
            result = convert(item)
            # print(item)
        Ja.append(result)
    return ' '.join(Ja)


def main():
    pass


if __name__ == '__main__':
    sen1 = "pit, pet, ham, cap, mug, socks, book"
    ans1 = "pitto , petto , hamu , kyappu , magu , sokkusu , bukku"

    sen1_1 = "monkey, front, London"
    ans1_1 = "monkī , furonto , rondon"

    sen2 = "about, pilot, London, carrier, hamburger"
    ans2 = "abauto , pairotto , rondon , kyariā , hambāgā"

    sen3 = "car, shield, horse, door, bird, shoe, cube"
    ans3 = "kā , shīrudo , hōsu , doa , bādo , shū , kyūbu"

    # test

    for sen, ans in zip([sen1, sen1_1, sen2, sen3], [ans1, ans1_1, ans2, ans3]):
        print(f"Original : {sen}")
        IPA = Eng2IPA(sen)
        print(f"IPA      : {IPA}")
        IPA_sep = SenSep(IPA)
        # print(IPA_sep)
        ja = Ipa2Romaji(IPA)
        print(f"Converted: {ja}")
        print(f"GroundTru: {ans}")
        print()
    # convert("pɪt")

