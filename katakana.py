__author__ = 'Rockie Yang'

references = ['http://www.guidetojapanese.org/learn/grammar/hiragana',
              'http://www.guidetojapanese.org/audio/basic_sounds.zip']


def display(t):
    if len(t) > 3 and t[3] == 'placeholder':
        pass
    else:
        print(t)


monographs = \
    [{'name': 'ア行',
      'words': [{'kana': 'ア', 'romaji': 'a', 'origin': '安'},
                {'kana': 'イ', 'romaji': 'i', 'origin': '以'},
                {'kana': 'ウ', 'romaji': 'u', 'origin': '宇'},
                {'kana': 'エ', 'romaji': 'e', 'origin': '衣'},
                {'kana': 'オ', 'romaji': 'o', 'origin': '於'}]},

     {'name': 'カ行',
      'words': [{'kana': 'カ', 'romaji': 'ka', 'origin': '加'},
                {'kana': 'キ', 'romaji': 'ki', 'origin': '幾'},
                {'kana': 'ク', 'romaji': 'ku', 'origin': '久'},
                {'kana': 'ケ', 'romaji': 'ke', 'origin': '計'},
                {'kana': 'コ', 'romaji': 'ko', 'origin': '己'}]},

     {'name': 'サ行',
      'words': [{'kana': 'サ', 'romaji': 'sa', 'origin': '左'},
                {'kana': 'シ', 'romaji': 'shi', 'origin': '之'},
                {'kana': 'ス', 'romaji': 'su', 'origin': '寸'},
                {'kana': 'セ', 'romaji': 'se', 'origin': '世'},
                {'kana': 'ソ', 'romaji': 'so', 'origin': '曽'}]},

     {'name': 'タ行',
      'words': [{'kana': 'タ', 'romaji': 'ta', 'origin': '太'},
                {'kana': 'チ', 'romaji': 'chi', 'origin': '知'},
                {'kana': 'ツ', 'romaji': 'tsu', 'origin': '川'},
                {'kana': 'テ', 'romaji': 'te', 'origin': '天'},
                {'kana': 'ト', 'romaji': 'to', 'origin': '止'}]},

     {'name': 'ナ行',
      'words': [{'kana': 'ナ', 'romaji': 'na', 'origin': '奈'},
                {'kana': 'ニ', 'romaji': 'ni', 'origin': '仁'},
                {'kana': 'ヌ', 'romaji': 'nu', 'origin': '奴'},
                {'kana': 'ネ', 'romaji': 'ne', 'origin': '祢'},
                {'kana': 'ノ', 'romaji': 'no', 'origin': '乃'}]},

     {'name': 'ハ行',
      'words': [{'kana': 'ハ', 'romaji': 'ha', 'origin': '波'},
                {'kana': 'ヒ', 'romaji': 'hi', 'origin': '比'},
                {'kana': 'フ', 'romaji': 'fu', 'origin': '不'},
                {'kana': 'ヘ', 'romaji': 'he', 'origin': '部'},
                {'kana': 'ホ', 'romaji': 'ho', 'origin': '保'}]},

     {'name': 'マ行',
      'words': [{'kana': 'マ', 'romaji': 'ma', 'origin': '末'},
                {'kana': 'ミ', 'romaji': 'mi', 'origin': '美'},
                {'kana': 'ム', 'romaji': 'mu', 'origin': '武'},
                {'kana': 'メ', 'romaji': 'me', 'origin': '女'},
                {'kana': 'モ', 'romaji': 'mo', 'origin': '毛'}]},

     {'name': 'ヤ行',
      'words': [{'kana': 'ヤ', 'romaji': 'ya', 'origin': '也'},
                {'kana': 'い', 'romaji': 'i', 'origin': '以', "placeholder": True},
                {'kana': 'ユ', 'romaji': 'yu', 'origin': '由'},
                {'kana': 'え', 'romaji': 'e', 'origin': '衣', "placeholder": True},
                {'kana': 'ヨ', 'romaji': 'yo', 'origin': '与'}]},

     {'name': 'ラ行',
      'words': [{'kana': 'ラ', 'romaji': 'ra', 'origin': '良'},
                {'kana': 'リ', 'romaji': 'ri', 'origin': '利'},
                {'kana': 'ル', 'romaji': 'ru', 'origin': '留'},
                {'kana': 'レ', 'romaji': 're', 'origin': '礼'},
                {'kana': 'ロ', 'romaji': 'ro', 'origin': '呂'}]},

     {'name': 'ワ行',
      'words': [{'kana': 'ワ', 'romaji': 'wa', 'origin': '和'},
                {'kana': 'い', 'romaji': 'i', 'origin': '以', "placeholder": True},
                {'kana': 'う', 'romaji': 'u', 'origin': '宇', "placeholder": True},
                {'kana': 'え', 'romaji': 'e', 'origin': '衣', "placeholder": True},
                {'kana': 'ヲ', 'romaji': 'o', 'origin': '遠'}]}]

diacritics = \
    [{'name': 'ガ行',
      'words': [{'kana': 'ガ', 'romaji': 'ga'},
                {'kana': 'ギ', 'romaji': 'gi'},
                {'kana': 'グ', 'romaji': 'gu'},
                {'kana': 'ゲ', 'romaji': 'ge'},
                {'kana': 'ゴ', 'romaji': 'go'}]},
     {'name': 'ザ行',
      'words': [{'kana': 'ザ', 'romaji': 'za'},
                {'kana': 'ジ', 'romaji': 'ji'},
                {'kana': 'ズ', 'romaji': 'zu'},
                {'kana': 'ゼ', 'romaji': 'ze'},
                {'kana': 'ゾ', 'romaji': 'zo'}]},
     {'name': 'ダ行',
      'words': [{'kana': 'ダ', 'romaji': 'da'},
                {'kana': 'ヂ', 'romaji': 'ji'},
                {'kana': 'ヅ', 'romaji': 'dzu'},
                {'kana': 'デ', 'romaji': 'de'},
                {'kana': 'ド', 'romaji': 'do'}]},
     {'name': 'バ行',
      'words': [{'kana': 'バ', 'romaji': 'ba'},
                {'kana': 'ビ', 'romaji': 'bi'},
                {'kana': 'ブ', 'romaji': 'bu'},
                {'kana': 'ベ', 'romaji': 'be'},
                {'kana': 'ボ', 'romaji': 'bo'}]},
     {'name': 'パ行',
      'words': [{'kana': 'パ', 'romaji': 'pa'},
                {'kana': 'ピ', 'romaji': 'bi'},
                {'kana': 'プ', 'romaji': 'bu'},
                {'kana': 'ぺ', 'romaji': 'pe'},
                {'kana': 'ポ', 'romaji': 'po'}]}]

misc = \
    {'name': 'misc',
     'words': [{'kana': 'ン', 'romaji': 'n'},
               {'kana': 'ッ', 'romaji': 'bi'},
               {'kana': 'ー', 'romaji': 'bu'},
               {'kana': 'ヽ', 'romaji': 'pe'},
               {'kana': 'ヾ', 'romaji': 'po'}]}

digraphs = \
    {'name': 'Digraphs (yōon)',
     'words': [{'kana': 'キャ', 'romaji': 'kya'},
               {'kana': 'キュ', 'romaji': 'kyu'},
               {'kana': 'キョ', 'romaji': 'kyo'},
               {'kana': 'シャ', 'romaji': 'sya'},
               {'kana': 'シュ', 'romaji': 'syu'},
               {'kana': 'ショ', 'romaji': 'syo'},
               {'name': 'チャ', 'romaji': 'cya'},
               {'kana': 'チュ', 'romaji': 'cyu'},
               {'kana': 'チョ', 'romaji': 'cyo'},
               {'name': 'ニャ', 'romaji': 'nya'},
               {'kana': 'ニュ', 'romaji': 'nyu'},
               {'kana': 'ニョ', 'romaji': 'nyo'},
               {'name': 'ヒャ', 'romaji': 'hya'},
               {'kana': 'ヒュ', 'romaji': 'hyu'},
               {'kana': 'ヒョ', 'romaji': 'hyo'},
               {'name': 'ミャ', 'romaji': 'mya'},
               {'kana': 'ミュ', 'romaji': 'myu'},
               {'kana': 'ミョ', 'romaji': 'myo'},
               {'name': 'リャ', 'romaji': 'rya'},
               {'kana': 'リュ', 'romaji': 'ryu'},
               {'kana': 'リョ', 'romaji': 'ryo'}]}

digraphsWithDiacritics = \
    {'name': 'Digraphs with diacritics: yōon with (han)dakuten',
     'words': [{'name': 'ギャ', 'romaji': 'gya'},
               {'kana': 'ギュ', 'romaji': 'gyu'},
               {'kana': 'ギョ', 'romaji': 'gyo'},
               {'name': 'ジャ', 'romaji': 'jya'},
               {'kana': 'ジュ', 'romaji': 'jyu'},
               {'kana': 'ジョ', 'romaji': 'jyo'},
               {'name': 'ヂャ', 'romaji': 'ja'},
               {'kana': 'ヂュ', 'romaji': 'ju'},
               {'kana': 'ヂョ', 'romaji': 'jo'},
               {'name': 'ビャ', 'romaji': 'bya'},
               {'kana': 'ビュ', 'romaji': 'byu'},
               {'kana': 'ビョ', 'romaji': 'byo'},
               {'name': 'ピャ', 'romaji': 'pya'},
               {'kana': 'ピュ', 'romaji': 'pyu'},
               {'kana': 'ピョ', 'romaji': 'pyo'}]}
