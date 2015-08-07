__author__ = 'Rockie Yang'
# -*- coding: utf-8 -*-

references = ['http://www.guidetojapanese.org/learn/grammar/hiragana',
              'http://www.guidetojapanese.org/audio/basic_sounds.zip']

def display(t):
    if len(t) > 3 and t[3] == 'placeholder':
        pass
    else:
        print(t)

basic = [
    [('あ行'),
     ('あ', 'a', '安'),
     ('い', 'i', '以'),
     ('う', 'u', '宇'),
     ('え', 'e', '衣'),
     ('お', 'o', '於')],

    [('か行'),
     ('か', 'ka', '加'),
     ('き', 'ki', '幾'),
     ('く', 'ku', '久'),
     ('け', 'ke', '計'),
     ('こ', 'ko', '己')],

    [('さ行'),
     ('さ', 'sa', '左'),
     ('し', 'shi', '之'),
     ('す', 'su', '寸'),
     ('せ', 'se', '世'),
     ('そ', 'so', '曽')],

    [('た行'),
     ('た', 'ta', '太'),
     ('ち', 'chi', '知'),
     ('つ', 'tsu', '川'),
     ('て', 'te', '天'),
     ('と', 'to', '止')],

    [('な行'),
     ('な', 'na', '奈'),
     ('に', 'ni', '仁'),
     ('ぬ', 'nu', '奴'),
     ('ね', 'ne', '祢'),
     ('の', 'no', '乃')],

    [('は行'),
     ('は', 'ha', '波'),
     ('ひ', 'hi', '比'),
     ('ふ', 'fu', '不'),
     ('へ', 'he', '部'),
     ('ほ', 'ho', '保')],

    [('ま行'),
     ('ま', 'ma', '末'),
     ('み', 'mi', '美'),
     ('む', 'mu', '武'),
     ('め', 'me', '女'),
     ('も', 'mo', '毛')],

    [('や行'),
     ('や', 'ya', '也'),
     ('い', 'i', '以', "placeholder"),
     ('ゆ', 'yu', '由'),
     ('え', 'e', '衣', "placeholder"),
     ('よ', 'yu', '与')],

    [('ら行'),
     ('ら', 'ra', '良'),
     ('り', 'ri', '利'),
     ('る', 'ru', '留'),
     ('れ', 're', '礼'),
     ('ろ', 'ro', '呂')],

    [('わ行'),
     ('わ', 'wa', '和'),
     ('い', 'i', '以', "placeholder"),
     ('う', 'u', '宇', "placeholder"),
     ('え', 'e', '衣', "placeholder"),
     ('を', 'o', '遠')]]

voiced = [
    [('が行'),
     ('が', 'ga', ''),
     ('ぎ', 'gi', ''),
     ('ぐ', 'gu', ''),
     ('げ', 'ge', ''),
     ('ご', 'go', '')],
    [('ざ行'),
     ('ざ', 'za', ''),
     ('じ', 'ji', ''),
     ('ず', 'zu', ''),
     ('ぜ', 'ze', ''),
     ('ぞ', 'zo', '')],
    [('だ行'),
     ('だ', 'da', ''),
     ('ぢ', 'ji', ''),
     ('づ', 'dzu', ''),
     ('で', 'de', ''),
     ('ど', 'do', '')],
    [('ば行'),
     ('ば', 'ba', ''),
     ('び', 'bi', ''),
     ('ぶ', 'bu', ''),
     ('べ', 'be', ''),
     ('ぼ', 'bo', '')],
    [('ぱ行'),
     ('ぱ', 'pa', ''),
     ('ぴ', 'bi', ''),
     ('ぷ', 'bu', ''),
     ('ぺ', 'pe', ''),
     ('ぽ', 'po', '')]]

combined = [
    [('あ行'),
     ('きゃ', 'kya', ''),
     ('きゅ', 'kyu', ''),
     ('きょ', 'kyo', '')],
    [('あ行'),
     ('しゃ', 'sya', ''),
     ('しゅ', 'syu', ''),
     ('しょ', 'syo', '')],
    [('ちゃ', 'cya', ''),
     ('ちゅ', 'cyu', ''),
     ('ちょ', 'cyo', '')],
    [('にゃ', 'nya', ''),
     ('にゅ', 'nyu', ''),
     ('にょ', 'nyo', '')],
    [('ひゃ', 'hya', ''),
     ('ひゅ', 'hyu', ''),
     ('ひょ', 'hyo', '')],
    [('みゃ', 'mya', ''),
     ('みゅ', 'myu', ''),
     ('みょ', 'myo', '')],
    [('りゃ', 'rya', ''),
     ('りゅ', 'ryu', ''),
     ('りょ', 'ryo', '')],
    [('ぎゃ', 'gya', ''),
     ('ぎゅ', 'gyu', ''),
     ('ぎょ', 'gyo', '')],
    [('じゃ', 'jya', ''),
     ('じゅ', 'jyu', ''),
     ('じょ', 'jyo', '')],
    [('びゃ', 'bya', ''),
     ('びゅ', 'byu', ''),
     ('びょ', 'byo', '')],
    [('ぴゃ', 'pya', ''),
     ('ぴゅ', 'pyu', ''),
     ('ぴょ', 'pyo', '')]
    ]