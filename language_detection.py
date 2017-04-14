from langdetect import detect
import nltk
import os

os.system('python -m nltk.downloader all')

txt = 'Министр культуры Индрек Саар намерен ввести в состав совета Русского театра новых членов. Одним из новичков в обозримом будущем очевидно станет вице-мэр Таллинна, центрист Михаил Кылварт.'
txt2 = 'Congress sent proposed legislation to President Trump on Tuesday that wipes away landmark online privacy protections, the first salvo in what is likely to become a significant reworking of the rules governing Internet access in an era of Republican dominance.In a party-line vote, House Republicans freed Internet service providers such as Verizon, AT&T and Comcast of protections approved just last year that had sought to limit what companies could do with information such as customer browsing habits, app usage history, location data and Social Security numbers. The rules also had required providers to strengthen safeguards for customer data against hackers and thieves.'

nltk.download()

def get_continuous_chunks(text):
    chunked = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []

    for i in chunked:
        if type(i) == nltk.Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    return continuous_chunk

lang = detect(txt2)

if lang == 'et':
    print('eesti')
elif lang == 'ru':
    print('vene')
else:
    print('eesti, unknown lang')




