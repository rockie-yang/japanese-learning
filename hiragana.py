__author__ = 'Rockie Yang'

references = ['http://www.guidetojapanese.org/learn/grammar/hiragana',
              'http://www.guidetojapanese.org/audio/basic_sounds.zip',
              'http://www.tokyowithkids.com/fyi/japanese/kana_sounds/cha.wav',
              'https://en.wikipedia.org/wiki/Hiragana']


def display(t):
    if len(t) > 3 and t[3] == 'placeholder':
        pass
    else:
        print(t)


monographs = \
    [{'name': 'あ行',
      'words': [{'kana': 'あ', 'romaji': 'a', 'origin': '安'},
                {'kana': 'い', 'romaji': 'i', 'origin': '以'},
                {'kana': 'う', 'romaji': 'u', 'origin': '宇'},
                {'kana': 'え', 'romaji': 'e', 'origin': '衣'},
                {'kana': 'お', 'romaji': 'o', 'origin': '於'}]},

     {'name': 'か行',
      'words': [{'kana': 'か', 'romaji': 'ka', 'origin': '加'},
                {'kana': 'き', 'romaji': 'ki', 'origin': '幾'},
                {'kana': 'く', 'romaji': 'ku', 'origin': '久'},
                {'kana': 'け', 'romaji': 'ke', 'origin': '計'},
                {'kana': 'こ', 'romaji': 'ko', 'origin': '己'}]},

     {'name': 'さ行',
      'words': [{'kana': 'さ', 'romaji': 'sa', 'origin': '左'},
                {'kana': 'し', 'romaji': 'shi', 'origin': '之'},
                {'kana': 'す', 'romaji': 'su', 'origin': '寸'},
                {'kana': 'せ', 'romaji': 'se', 'origin': '世'},
                {'kana': 'そ', 'romaji': 'so', 'origin': '曽'}]},

     {'name': 'た行',
      'words': [{'kana': 'た', 'romaji': 'ta', 'origin': '太'},
                {'kana': 'ち', 'romaji': 'chi', 'origin': '知'},
                {'kana': 'つ', 'romaji': 'tsu', 'origin': '川'},
                {'kana': 'て', 'romaji': 'te', 'origin': '天'},
                {'kana': 'と', 'romaji': 'to', 'origin': '止'}]},

     {'name': 'な行',
      'words': [{'kana': 'な', 'romaji': 'na', 'origin': '奈'},
                {'kana': 'に', 'romaji': 'ni', 'origin': '仁'},
                {'kana': 'ぬ', 'romaji': 'nu', 'origin': '奴'},
                {'kana': 'ね', 'romaji': 'ne', 'origin': '祢'},
                {'kana': 'の', 'romaji': 'no', 'origin': '乃'}]},

     {'name': 'は行',
      'words': [{'kana': 'は', 'romaji': 'ha', 'origin': '波'},
                {'kana': 'ひ', 'romaji': 'hi', 'origin': '比'},
                {'kana': 'ふ', 'romaji': 'fu', 'origin': '不'},
                {'kana': 'へ', 'romaji': 'he', 'origin': '部'},
                {'kana': 'ほ', 'romaji': 'ho', 'origin': '保'}]},

     {'name': 'ま行',
      'words': [{'kana': 'ま', 'romaji': 'ma', 'origin': '末'},
                {'kana': 'み', 'romaji': 'mi', 'origin': '美'},
                {'kana': 'む', 'romaji': 'mu', 'origin': '武'},
                {'kana': 'め', 'romaji': 'me', 'origin': '女'},
                {'kana': 'も', 'romaji': 'mo', 'origin': '毛'}]},

     {'name': 'や行',
      'words': [{'kana': 'や', 'romaji': 'ya', 'origin': '也'},
                {'kana': 'い', 'romaji': 'i', 'origin': '以', "placeholder": True},
                {'kana': 'ゆ', 'romaji': 'yu', 'origin': '由'},
                {'kana': 'え', 'romaji': 'e', 'origin': '衣', "placeholder": True},
                {'kana': 'よ', 'romaji': 'yo', 'origin': '与'}]},

     {'name': 'ら行',
      'words': [{'kana': 'ら', 'romaji': 'ra', 'origin': '良'},
                {'kana': 'り', 'romaji': 'ri', 'origin': '利'},
                {'kana': 'る', 'romaji': 'ru', 'origin': '留'},
                {'kana': 'れ', 'romaji': 're', 'origin': '礼'},
                {'kana': 'ろ', 'romaji': 'ro', 'origin': '呂'}]},

     {'name': 'わ行',
      'words': [{'kana': 'わ', 'romaji': 'wa', 'origin': '和'},
                {'kana': 'い', 'romaji': 'i', 'origin': '以', "placeholder": True},
                {'kana': 'う', 'romaji': 'u', 'origin': '宇', "placeholder": True},
                {'kana': 'え', 'romaji': 'e', 'origin': '衣', "placeholder": True},
                {'kana': 'を', 'romaji': 'o', 'origin': '遠'}]}]

diacritics = \
    [{'name': 'が行',
      'words': [{'kana': 'が', 'romaji': 'ga', 'origin': ''},
                {'kana': 'ぎ', 'romaji': 'gi', 'origin': ''},
                {'kana': 'ぐ', 'romaji': 'gu', 'origin': ''},
                {'kana': 'げ', 'romaji': 'ge', 'origin': ''},
                {'kana': 'ご', 'romaji': 'go', 'origin': ''}]},
     {'name': 'ざ行',
      'words': [{'kana': 'ざ', 'romaji': 'za', 'origin': ''},
                {'kana': 'じ', 'romaji': 'ji', 'origin': ''},
                {'kana': 'ず', 'romaji': 'zu', 'origin': ''},
                {'kana': 'ぜ', 'romaji': 'ze', 'origin': ''},
                {'kana': 'ぞ', 'romaji': 'zo', 'origin': ''}]},
     {'name': 'だ行',
      'words': [{'kana': 'だ', 'romaji': 'da', 'origin': ''},
                {'kana': 'ぢ', 'romaji': 'ji', 'origin': ''},
                {'kana': 'づ', 'romaji': 'dzu', 'origin': '', 'sound': 'zu'},
                {'kana': 'で', 'romaji': 'de', 'origin': ''},
                {'kana': 'ど', 'romaji': 'do', 'origin': ''}]},
     {'name': 'ば行',
      'words': [{'kana': 'ば', 'romaji': 'ba', 'origin': ''},
                {'kana': 'び', 'romaji': 'bi', 'origin': ''},
                {'kana': 'ぶ', 'romaji': 'bu', 'origin': ''},
                {'kana': 'べ', 'romaji': 'be', 'origin': ''},
                {'kana': 'ぼ', 'romaji': 'bo', 'origin': ''}]},
     {'name': 'ぱ行',
      'words': [{'kana': 'ぱ', 'romaji': 'pa', 'origin': ''},
                {'kana': 'ぴ', 'romaji': 'pi', 'origin': ''},
                {'kana': 'ぷ', 'romaji': 'pu', 'origin': ''},
                {'kana': 'ぺ', 'romaji': 'pe', 'origin': ''},
                {'kana': 'ぽ', 'romaji': 'po', 'origin': ''}]}]

diagraphs = \
    {'name': 'Digraphs (yōon)',
     'words': [{'kana': 'きゃ', 'romaji': 'kya'},
               {'kana': 'きゅ', 'romaji': 'kyu'},
               {'kana': 'きょ', 'romaji': 'kyo'},
               {'kana': 'しゃ', 'romaji': 'sya'},
               {'kana': 'しゅ', 'romaji': 'syu'},
               {'kana': 'しょ', 'romaji': 'syo'},
               {'kana': 'ちゃ', 'romaji': 'cya'},
               {'kana': 'ちゅ', 'romaji': 'cyu'},
               {'kana': 'ちょ', 'romaji': 'cyo'},
               {'kana': 'にゃ', 'romaji': 'nya'},
               {'kana': 'にゅ', 'romaji': 'nyu'},
               {'kana': 'にょ', 'romaji': 'nyo'},
               {'kana': 'ひゃ', 'romaji': 'hya'},
               {'kana': 'ひゅ', 'romaji': 'hyu'},
               {'kana': 'ひょ', 'romaji': 'hyo'},
               {'kana': 'みゃ', 'romaji': 'mya'},
               {'kana': 'みゅ', 'romaji': 'myu'},
               {'kana': 'みょ', 'romaji': 'myo'},
               {'kana': 'りゃ', 'romaji': 'rya'},
               {'kana': 'りゅ', 'romaji': 'ryu'},
               {'kana': 'りょ', 'romaji': 'ryo'}]}

diagraphsWithDiacritics = \
    {'name': 'Digraphs with diacritics (yōon with (han)dakuten)',
     'words': [{'kana': 'ぎゃ', 'romaji': 'gya'},
               {'kana': 'ぎゅ', 'romaji': 'gyu'},
               {'kana': 'ぎょ', 'romaji': 'gyo'},

               {'kana': 'じゃ', 'romaji': 'jya'},
               {'kana': 'じゅ', 'romaji': 'jyu'},
               {'kana': 'じょ', 'romaji': 'jyo'},

               {'kana': 'びゃ', 'romaji': 'bya'},
               {'kana': 'びゅ', 'romaji': 'byu'},
               {'kana': 'びょ', 'romaji': 'byo'},

               {'kana': 'ぴゃ', 'romaji': 'pya'},
               {'kana': 'ぴゅ', 'romaji': 'pyu'},
               {'kana': 'ぴょ', 'romaji': 'pyo'}]}

