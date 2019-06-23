boring_news  =  ['witnesses',
                 'allegedely',
                 'new study',
                 'rebuilt',
                 'space',
                 'google glass',
                 'smartphone',
                 'electric',
                 'senator',
                 'speaker',
                 'car',
                 'election',
                 'congressional leaders',
                 'homeland security',
                 'could not be reached for comment',
                 'republican',
                 'democrat']

xkcd = ['dudes I know',
        'kinda probably',
        'tumblr post',
        'avenge',
        'spaace',
        'virtual boy',
        'pokedex',
        'atomic',
        'elf-lord',
        'elf-lord',
        'cat',
        'eating contest',
        'river spirits',
        'homestar runner',
        'is guilty and everyone knows it',
        'orc',
        'hobbit']

def changeWord(word):
    if word in boring_news:
        idx = boring_news.index(word)
        return xkcd[idx]
    else:
        return word


print(changeWord('senator'))
print(changeWord('python'))