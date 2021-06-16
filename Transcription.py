import re
from typing import List

marks = ['\n', '/', ' ']
preffs = ['ві', 'пі', 'на', 'пере', 'сере']
vowels = ['і', 'и', 'І', 'И', 'ĩ', 'и̃', 'ɴ', 'ɴ́', 'Ĩ', 'Ṹ', 'а', 'о', 'А', 'О', 'у', 'е', 'У', 'Е', 'ã', 'õ', 'Ã', 'Õ', 'ỹ', 'ẽ', 'Ỹ́', 'Ẽ', 'ə', 'ǝ̃']
    #['і', 'и', 'n', 'ĩ', 'ũ', 'а', 'о', 'у', 'е', 'ǝ', 'ã', 'õ', 'ỹ', 'ẽ', 'ǝ̃']
cons = ['р', 'д', 'ӡ', 'з', 'л', 'н', 'с', 'т', 'ц', 'б', 'в', 'г',
        'ґ', 'Ԫ', 'ж', 'к', 'м', 'п', 'ф', 'х', 'ч', 'ш', 'j', 'й']
soft = ['р', 'д', 'л', 'н', 'т', 'ӡ', 'з', 'с', 'ц']
semisoft = ['б', 'в', 'г', 'ґ', 'Ԫ', 'ж', 'к', 'м', 'п', 'ф', 'х', 'ч', 'ш']
voice = ['й', 'б', 'д', 'ӡ', 'з', 'г', 'ґ', 'Ԫ', 'ж']
mute = ['п', 'т', 'ц', 'с', 'х', 'к', 'ч', 'ш', 'ф']
ssssss = ['з', 'ц', 'с', 'ӡ']
shshsh = ['ж', 'ч', 'ш', 'Ԫ']
softy = ["д´", "т´", "з´", "с´", "ц´", "л´", "н´", "ӡ´"]
semisofty = ["ж’", "ч’", "ш’", "Ԫ’", "г’", "к’",
             "х’", "ґ’", "б’", "п’", "в’", "м’", "ф’"]

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

def transcript_the_text_phonetic(the_text: str, pickedLetters: str) -> str:
    text = the_text.encode('UTF-8').decode('UTF-8').lower()

    # наголос
    if pickedLetters != '':
        stress = pickedLetters.split(',')
        stress = list(map(lambda s: int(s), stress))
        text = Convert(text)
        for (index, letter) in enumerate(text):
            if index in stress:
                text[index] = text[index].upper()
        text = listToString(text)
        print(text)

    # розділові знаки
    text = re.sub(r' +', ' ', text)
    text = re.sub(r"’", "'", text)
    text = re.sub(r' ,', ',', text)
    #text = re.sub(r' , ', ', ', text)
    text = re.sub(r' \.', '.', text)
    text = re.sub(r'"', '', text)
    text = re.sub(r',', '/', text)
    text = re.sub(r':', '/', text)
    text = re.sub(r';', '/', text)
    text = re.sub(r'"', '/', text)
    text = re.sub(r' -', '/', text)
    text = re.sub(r' –', '/', text)
    text = re.sub(r' —', '/', text)
    text = re.sub(r'\(', '/', text)
    text = re.sub(r'\)', '/', text)
    text = re.sub(r' /', '/', text)
    text = re.sub(r'(\.|,|!|\?)+', '\\1', text)
    text = re.sub(r'\.', '//', text)
    text = re.sub(r'\?', '//', text)
    text = re.sub(r'!', '//', text)
    text = re.sub(r'//+', '//', text)
    text = re.sub(r'\n ', '\n', text)
    text = re.sub(r'\n ', ' \n', text)
    # text = re.sub(r'//', '//\n', text)
    # text = re.sub(r'utils', '//', text)
    text = '    /' + text + '/    '

    # фонетичні слова
    text = re.sub(r' з ', ' з', text)
    text = re.sub(r'\nз ', '\nз', text)
    text = re.sub(r'\sі ', ' і', text)
    text = re.sub(r' й ', ' й', text)
    text = re.sub(r'\sв ', ' в', text)
    text = re.sub(r'\sта ', ' та', text)
    text = re.sub(r'\sа ', ' а', text)
    text = re.sub(r'\sб ', 'б ', text)
    text = re.sub(r'\sби ', 'би ', text)
    text = re.sub(r' би', 'би', text)
    text = re.sub(r'під ', ' під', text)
    text = re.sub(r'\sні ', ' ні', text)
    text = re.sub(r'\sані ', ' ані', text)
    text = re.sub(r'\sще й ', ' щей', text)
    text = re.sub(r'\nхоч ', '\nхоч', text)
    text = re.sub(r'\sчи ', ' чи', text)
    text = re.sub(r'\sто ', ' то', text)
    text = re.sub(r'\sбо ', ' бо', text)
    text = re.sub(r'\sще ', ' ще', text)
    text = re.sub(r'\sні ', ' ні', text)
    text = re.sub(r'\sані ', ' ані', text)
    text = re.sub(r'\sще й ', ' щей', text)
    text = re.sub(r'\sпо ', ' по', text)
    text = re.sub(r'\sна ', ' на', text)
    text = re.sub(r' не ', ' не', text)
    text = re.sub(r'\sза ', ' за', text)
    text = re.sub(r'\sдо ', ' до', text)
    text = re.sub(r' як ', ' як', text)
    text = re.sub(r'\nяк ', '\nяк', text)
    text = re.sub(r'\sа ', ' а', text)
    text = re.sub(r' не ', ' не', text)
    text = re.sub(r'\nне ', '\nне', text)
    text = re.sub(r' від ', ' від', text)
    text = re.sub(r' хай ', ' хай', text)
    text = re.sub(r'\sнехай ', ' нехай', text)
    text = re.sub(r'\nу ', '\nу', text)
    text = re.sub(r' без ', ' без', text)
    text = re.sub(r'\sтак ', ' так', text)
    text = re.sub(r'\nось ', '\nось', text)
    text = re.sub(r'\nчерез ', '\nчерез', text)
    text = re.sub(r'\nіпо ', '\nіпо', text)
    text = re.sub(r' іпо ', ' іпо', text)
    text = re.sub(r' зо ', ' зо', text)
    text = re.sub(r' чизо ', ' чизо', text)
    text = re.sub(r' у ', ' у', text)
    text = re.sub(r' да ', ' да', text)
    text = re.sub(r' із ', ' із', text)

    # оглушення
    text = re.sub(r'кігт', 'кіхт', text)
    text = re.sub(r'нігт', 'ніхт', text)
    text = re.sub(r'легк', 'лехк', text)
    text = re.sub(r'вогк', 'вохк', text)
    text = re.sub(r'дьогт', 'дьохт', text)

    # спрощення
    text = re.sub(r'стс', 'сс', text)
    text = re.sub(r'стц', 'сц', text)
    text = re.sub(r'стч', 'сч', text)
    text = re.sub(r'стд', 'сд', text)
    text = re.sub(r'нтст', 'нст', text)
    text = re.sub(r'стськ', 'ськ', text)
    text = re.sub(r'нтськ', 'нськ', text)
    text = re.sub(r'нтств', 'нств', text)
    text = re.sub(r'кісляв', 'кістляв', text)
    text = re.sub(r'хваслив', 'хвастлив', text)
    text = re.sub(r'хвасн', 'хвастн', text)
    text = re.sub(r'песлив', 'пестлив', text)
    text = re.sub(r"зап'ясн", "зап'ястн", text)
    text = re.sub(r"хворосняк", "хворостняк", text)

    text = re.sub(r"ться", 'тьця', text)

    for symb in range(len(text) - 1):

        #дефіс
        if text[symb] == '-':
            if text[symb - 1].isalpha() and text[symb + 1].isalpha():
                text = text.replace(text[symb - 1] + text[symb] + text[symb + 1],
                                    text[symb - 1] + ' ' + text[symb + 1])

        # ї, щ
        if text[symb] == 'щ':
            text = text.replace(text[symb], 'ш' + 'ч')
        if text[symb] == 'ї'.lower():
            text = text.replace(text[symb], 'j' + 'і')
            if text[symb - 1] == "'":
                text = text.replace(
                    text[symb - 1] + text[symb], '' + text[symb])

        # дз, дж
        if text[symb] == 'д' and text[symb + 1] == 'з':
            text = text.replace(text[symb] + text[symb + 1], '' + 'ӡ')
        if text[symb] == 'ӡ' and (text[symb - 2] + text[symb - 1]) in preffs:
            text = text.replace(
                text[symb] + text[symb + 1], 'д' + 'з' + text[symb + 1])
        if text[symb] == 'ӡ' and (text[symb - 4] + text[symb - 3] + text[symb - 2] + text[symb - 1]) in preffs:
            text = text.replace(
                text[symb] + text[symb + 1], 'д' + 'з' + text[symb + 1])

    for symb in range(len(text) - 1):
        if text[symb] == 'д' and text[symb + 1] == 'ж':
            text = text.replace(text[symb] + text[symb + 1], '' + 'Ԫ')
        if text[symb] == 'Ԫ' and (text[symb - 2] + text[symb - 1]) in preffs:
            text = text.replace(
                text[symb] + text[symb + 1], 'д' + 'ж' + text[symb + 1])
        if text[symb] == 'Ԫ' and (text[symb - 4] + text[symb - 3] + text[symb - 2] + text[symb - 1]) in preffs:
            text = text.replace(
                text[symb] + text[symb + 1], 'д' + 'ж' + text[symb + 1])

        # нескладові ў, ĭ
        if text[symb] == 'в':
            if text[symb - 1] in marks[:2] and text[symb + 1] in cons:
                text = text.replace(
                    text[symb] + text[symb + 1], 'ў' + text[symb + 1])
            if text[symb - 1] in vowels and text[symb + 1] in cons:
                text = text.replace(
                    text[symb] + text[symb + 1], 'ў' + text[symb + 1])
            if text[symb - 1] in vowels and text[symb + 1] in marks[:2]:
                text = text.replace(
                    text[symb] + text[symb + 1], 'ў' + text[symb + 1])
            if text[symb - 1] in vowels and text[symb + 1] == ' ' and text[symb + 2] in cons:
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], 'ў' + text[symb + 1] + text[symb + 2])
            if text[symb - 2] in vowels and text[symb - 1] == ' ' and text[symb + 1] in cons:
                text = text.replace(
                    text[symb - 1] + text[symb] + text[symb + 1], text[symb - 1] + 'ў' + text[symb + 1])

        if text[symb] == 'й':
            if text[symb - 1] in marks[:2] and text[symb + 1] in cons:
                text = text.replace(
                    text[symb] + text[symb + 1], 'ĭ' + text[symb + 1])
            if text[symb - 1] in vowels and text[symb + 1] in cons:
                text = text.replace(
                    text[symb] + text[symb + 1], 'ĭ' + text[symb + 1])
            if text[symb - 1] in vowels and text[symb + 1] in marks[:2]:
                text = text.replace(
                    text[symb] + text[symb + 1], 'ĭ' + text[symb + 1])
            if text[symb - 1] in vowels and text[symb + 1] == ' ' and text[symb + 2] in cons:
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], 'ĭ' + text[symb + 1] + text[symb + 2])
            if text[symb - 2] in vowels and text[symb - 1] == ' ' and text[symb + 1] in cons:
                text = text.replace(
                    text[symb - 1] + text[symb] + text[symb + 1], text[symb - 1] + 'ĭ' + text[symb + 1])


    for symb in range(len(text) - 1):
        # я, ю, є
        if text[symb + 1] == 'я':
            if text[symb] == "'":
                text = text.replace(
                    text[symb] + text[symb + 1], "" + 'j' + 'а')
            if text[symb] in soft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "´" + 'а')
            if text[symb] in semisoft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "’" + 'а')
            if text[symb] in vowels or text[symb] in marks:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'j' + 'а')
            if text[symb] == 'ь':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'j' + 'а')
        if text[symb + 1] == 'ю':
            if text[symb] == "'":
                text = text.replace(
                    text[symb] + text[symb + 1], "" + 'j' + 'у')
            if text[symb] in soft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "´" + 'у')
            if text[symb] in semisoft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "’" + 'у')
            if text[symb] in vowels or text[symb] in marks:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'j' + 'у')
            if text[symb] == 'ь':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'j' + 'у')
        if text[symb + 1] == 'є':
            if text[symb] == "'":
                text = text.replace(
                    text[symb] + text[symb + 1], "" + 'j' + 'е')
            if text[symb] in soft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "´" + 'е')
            if text[symb] in semisoft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "’" + 'е')
            if text[symb] in vowels or text[symb] in marks:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'j' + 'е')
            if text[symb] == 'ь':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'j' + 'е')

        if text[symb + 1] == 'Я':
            if text[symb] == "'":
                text = text.replace(
                    text[symb] + text[symb + 1], "" + 'j' + 'А')
            if text[symb] in soft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "´" + 'А')
            if text[symb] in semisoft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "’" + 'А')
            if text[symb] in vowels or text[symb] in marks:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'j' + 'А')
            if text[symb] == 'ь':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'j' + 'А')
        if text[symb + 1] == 'Ю':
            if text[symb] == "'":
                text = text.replace(
                    text[symb] + text[symb + 1], "" + 'j' + 'У')
            if text[symb] in soft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "´" + 'У')
            if text[symb] in semisoft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "’" + 'У')
            if text[symb] in vowels or text[symb] in marks:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'j' + 'У')
            if text[symb] == 'ь':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'j' + 'У')
        if text[symb + 1] == 'Є':
            if text[symb] == "'":
                text = text.replace(
                    text[symb] + text[symb + 1], "" + 'j' + 'Е')
            if text[symb] in soft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "´" + 'Е')
            if text[symb] in semisoft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "’" + 'Е')
            if text[symb] in vowels or text[symb] in marks:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'j' + 'Е')
            if text[symb] == 'ь':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'j' + 'Е')

    # наближення голосних
    if pickedLetters != '':
        for symb in text:
            if symb.islower():
                if symb == 'е':
                    text = text.replace(symb, 'ə')
                if symb == 'и':
                    text = text.replace(symb, 'ɴ')
    #text = re.sub(r'о\w+˚+У', 'ŏ', text)

    for symb in range(len(text) - 1):
        # пом'якшення
        if text[symb + 1] == 'і'.lower():
            if text[symb] in soft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "´" + text[symb + 1])
            if text[symb] in semisoft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "’" + text[symb + 1])
    #for symb in range(len(text) - 1):
        #if text[symb + 1] == ' ' and text[symb + 2] == 'і':
            #if text[symb] in soft:
                #text = text.replace(
                    #[symb] + text[symb + 1] + text[symb + 2], text[symb] + "´" + text[symb + 1] + text[symb + 2])
            #if text[symb] in semisoft:
                #text = text.replace(
                    #text[symb] + text[symb + 1] + text[symb + 2], text[symb] + "’" + text[symb + 1] + text[symb + 2])
    for symb in range(len(text) - 1):
        if text[symb + 1] == 'ь':
            if text[symb] in soft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "´" + '')
            if text[symb] in semisoft:
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + "’" + '')

    for symb in range(len(text) - 1):
        # асиміляція за дзвінкістю !! мйяк поменятьместами !!
        if text[symb] in voice:
            if text[symb - 1] == 'п':
                text = text.replace(
                    text[symb - 1] + text[symb], 'б' + text[symb])
            if text[symb - 2] == 'п' and text[symb - 1] == "’":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'б' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'п' and text[symb - 1] == ":":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'б' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'п' and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'б' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'п' and text[symb - 2] == "’" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'б' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 3] == 'п' and text[symb - 2] == ":" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'б' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 3] == 'п' and text[symb - 2] == ":" and text[symb - 1] == "’":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'б' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 4] == 'п' and text[symb - 3] == ":" and text[symb - 2] == "’" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 4] + text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'б' + text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'т':
                text = text.replace(
                    text[symb - 1] + text[symb], 'д' + text[symb])
            if text[symb - 2] == 'т' and text[symb - 1] == "´":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'д' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'т' and text[symb - 1] == ":":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'д' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'т' and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'д' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'т' and text[symb - 2] == "´" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'д' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 3] == 'т' and text[symb - 2] == ":" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'д' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 3] == 'т' and text[symb - 2] == "´" and text[symb - 1] == ":":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'д' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 4] == 'т' and text[symb - 3] == "´" and text[symb - 2] == ":" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 4] + text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'д' + text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'ц':
                text = text.replace(
                    text[symb - 1] + text[symb], 'ӡ' + text[symb])
            if text[symb - 2] == 'ц' and text[symb - 1] == "´":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ӡ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'ц' and text[symb - 1] == ":":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ӡ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'ц' and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ӡ' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'ц' and text[symb - 2] == "´" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'ӡ' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 3] == 'ц' and text[symb - 2] == ":" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'ӡ' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 3] == 'ц' and text[symb - 2] == "´" and text[symb - 1] == ":":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'ӡ' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 4] == 'ц' and text[symb - 3] == "´" and text[symb - 2] == ":" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 4] + text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'ӡ' + text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'с':
                text = text.replace(
                    text[symb - 1] + text[symb], 'з' + text[symb])
            if text[symb - 2] == 'с' and text[symb - 1] == "´":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'з' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'с' and text[symb - 1] == ":":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'з' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'с' and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'з' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'с' and text[symb - 2] == "´" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'з' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 3] == 'с' and text[symb - 2] == ":" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'з' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 3] == 'с' and text[symb - 2] == "´" and text[symb - 1] == ":":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'з' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 4] == 'с' and text[symb - 3] == "´" and text[symb - 2] == ":" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 4] + text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'з' + text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'к':
                text = text.replace(
                    text[symb - 1] + text[symb], 'ґ' + text[symb])
            if text[symb - 2] == 'к' and text[symb - 1] == "’":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ґ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'к' and text[symb - 1] == ":":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ґ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'к' and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ґ' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'к' and text[symb - 2] == "’" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'ґ' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 3] == 'к' and text[symb - 2] == ":" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'ґ' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 3] == 'к' and text[symb - 2] == ":" and text[symb - 1] == "’":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'ґ' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 4] == 'к' and text[symb - 3] == ":" and text[symb - 2] == "’" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 4] + text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'ґ' + text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'ч':
                text = text.replace(
                    text[symb - 1] + text[symb], 'Ԫ' + text[symb])
            if text[symb - 2] == 'ч' and text[symb - 1] == "’":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'Ԫ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'ч' and text[symb - 1] == ":":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'Ԫ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'ч' and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'Ԫ' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'ч' and text[symb - 2] == "’" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'Ԫ' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 3] == 'ч' and text[symb - 2] == ":" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'Ԫ' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 3] == 'ч' and text[symb - 2] == ":" and text[symb - 1] == "’":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'Ԫ' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 4] == 'ч' and text[symb - 3] == ":" and text[symb - 2] == "’" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 4] + text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'Ԫ' + text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb])

        # асиміляція за місцем і способом творення
        if text[symb] in ssssss:
            if text[symb - 1] == 'д':
                text = text.replace(
                    text[symb - 1] + text[symb], 'ӡ' + text[symb])
            if text[symb - 2] == 'д' and text[symb - 1] == "´":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ӡ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'д' and text[symb - 1] == ":":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ӡ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'д' and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ӡ' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'д' and text[symb - 2] == "´" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3], text[symb - 2] + text[symb - 1] + text[symb],
                    'ӡ' + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'т':
                text = text.replace(
                    text[symb - 1] + text[symb], 'ц' + text[symb])
            if text[symb - 2] == 'т' and text[symb - 1] == "´":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ц' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'т' and text[symb - 1] == ":":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ц' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'т' and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ц' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'т' and text[symb - 2] == "´" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3], text[symb - 2] + text[symb - 1] + text[symb],
                    'ц' + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'ж':
                text = text.replace(
                    text[symb - 1] + text[symb], 'з' + text[symb])
            if text[symb - 2] == 'ж' and text[symb - 1] == "’":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'з' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'ж' and text[symb - 1] == ":":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'з' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'ж' and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'з' + text[symb - 1] + text[symb])

            if text[symb - 1] == 'ш':
                text = text.replace(
                    text[symb - 1] + text[symb], 'с' + text[symb])
            if text[symb - 2] == 'ш' and text[symb - 1] == "’":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'с' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'ш' and text[symb - 1] == ":":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'с' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'ш' and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'с' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'ш' and text[symb - 2] == "’" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                    'с' + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'ч':
                text = text.replace(
                    text[symb - 1] + text[symb], 'ц' + text[symb])
            if text[symb - 2] == 'ч' and text[symb - 1] == "’":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ц' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'ч' and text[symb - 1] == ":":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ц' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'ч' and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ц' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'ч' and text[symb - 2] == "’" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3], text[symb - 2] + text[symb - 1] + text[symb],
                    'ц' + text[symb - 2] + text[symb - 1] + text[symb])
            if text[symb - 3] == 'ч' and text[symb - 2] == ":" and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 3], text[symb - 2] + text[symb - 1] + text[symb],
                    'ц' + text[symb - 2] + text[symb - 1] + text[symb])

        if text[symb] in shshsh:
            if text[symb - 1] == 'д':
                text = text.replace(
                    text[symb - 1] + text[symb], 'Ԫ' + text[symb])
            if text[symb - 2] == 'д' and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'Ԫ' + text[symb - 1] + text[symb])
            if text[symb - 1] == 'т':
                text = text.replace(
                    text[symb - 1] + text[symb], 'ч' + text[symb])
            if text[symb - 2] == 'т' and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ч' + text[symb - 1] + text[symb])
            if text[symb - 1] == 'с':
                text = text.replace(
                    text[symb - 1] + text[symb], 'ш' + text[symb])
            if text[symb - 2] == 'с' and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ш' + text[symb - 1] + text[symb])
            if text[symb - 1] == 'з':
                text = text.replace(
                    text[symb - 1] + text[symb], 'ж' + text[symb])
            if text[symb - 2] == 'з' and text[symb - 1] == " ":
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ж' + text[symb - 1] + text[symb])

        # подовження
        if text[symb].isalpha() and text[symb] in cons:
            if text[symb - 1] == text[symb]:
                if text[symb + 1] == "´":
                    text = text.replace(
                        text[symb - 1] + text[symb] + text[symb + 1], '' + text[symb] + text[symb + 1] + ':')
                elif text[symb + 1] == "’":
                    text = text.replace(
                        text[symb - 1] + text[symb] + text[symb + 1], '' + text[symb] + ':' + text[symb + 1])
                else:
                    text = text.replace(
                        text[symb - 1] + text[symb], '' + text[symb] + ':')
            if text[symb - 2] == text[symb] and text[symb - 1] == "´":
                if text[symb + 1] == "´":
                    text = text.replace(
                        text[symb - 2] + text[symb - 1] +
                        text[symb] + text[symb + 1],
                        '' + '' + text[symb] + text[symb + 1] + ':')
            if text[symb - 2] == text[symb] and text[symb - 1] == "’":
                if text[symb + 1] == "’":
                    text = text.replace(
                        text[symb - 2] + text[symb - 1] +
                        text[symb] + text[symb + 1],
                        '' + '' + text[symb] + ':' + text[symb + 1])

    for symb in range(len(text) - 1):
        # асиміляція за м'якістю
        if text[symb] in soft[1:] and (text[symb + 1] + text[symb + 2]) in softy:
            text = text.replace(text[symb] + text[symb + 1] + text[symb + 2],
                                text[symb] + "´" + text[symb + 1] + text[symb + 2])
        if text[symb] in soft[5:] and (text[symb + 1] + text[symb + 2]) in semisofty[8:]:
            text = text.replace(text[symb] + text[symb + 1] + text[symb + 2],
                                text[symb] + "´" + text[symb + 1] + text[symb + 2])
        if text[symb] in soft[5:] and (text[symb + 1] + text[symb + 2]) == 'р' + "´":
            text = text.replace(text[symb] + text[symb + 1] + text[symb + 2],
                                text[symb] + "´" + text[symb + 1] + text[symb + 2])

        # лабіалізація
        if text[symb].lower() == 'о' or text[symb].lower() == 'у':
            if text[symb - 1] == ':':
                text = text.replace(
                    text[symb - 1] + text[symb], text[symb - 1] + '˚' + text[symb])
            if text[symb - 1] == '´':
                text = text.replace(
                    text[symb - 1] + text[symb], text[symb - 1] + '˚' + text[symb])
            if text[symb - 1] == '’':
                text = text.replace(
                    text[symb - 1] + text[symb], text[symb - 1] + '˚' + text[symb])
            if text[symb - 1] in cons:
                text = text.replace(
                    text[symb - 1] + text[symb], text[symb - 1] + '˚' + text[symb])
            if text[symb - 2] == ':' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 2] + '˚' + text[symb - 1] + text[symb])
            if text[symb - 2] == '´' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 2] + '˚' + text[symb - 1] + text[symb])
            if text[symb - 2] == '’' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 2] + '˚' + text[symb - 1] + text[symb])
            if text[symb - 2] in cons and text[symb - 1] == ' ':
                text = text.replace(text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 2] + '˚' + text[symb - 1] + text[symb])


    for symb in range(len(text) - 1):
        # назалізація регресивна
        if text[symb] == 'м' or text[symb] == 'н':
            if text[symb - 1] == 'а':
                text = text.replace(
                    text[symb - 1] + text[symb], 'ã' + text[symb])
            if text[symb - 2] == 'а' and text[symb - 1] == '˙':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ã' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'а' and text[symb - 1] == ' ':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ã' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'а' and text[symb - 2] == '˙' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    'ã' + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'А':
                text = text.replace(
                    text[symb - 1] + text[symb], 'Ã' + text[symb])
            if text[symb - 2] == 'А' and text[symb - 1] == '˙':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'Ã' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'А' and text[symb - 1] == ' ':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'Ã' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'А' and text[symb - 2] == '˙' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    'Ã' + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'о':
                text = text.replace(
                    text[symb - 1] + text[symb], 'õ' + text[symb])
            if text[symb - 2] == 'о' and text[symb - 1] == '˙':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'õ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'о' and text[symb - 1] == ' ':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'õ' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'о' and text[symb - 2] == '˙' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    'õ' + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'О':
                text = text.replace(
                    text[symb - 1] + text[symb], 'Õ' + text[symb])
            if text[symb - 2] == 'О' and text[symb - 1] == '˙':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'Õ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'О' and text[symb - 1] == ' ':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'Õ' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'О' and text[symb - 2] == '˙' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    'Õ' + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'у':
                text = text.replace(
                    text[symb - 1] + text[symb], 'ỹ' + text[symb])
            if text[symb - 2] == 'у' and text[symb - 1] == '˙':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ỹ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'у' and text[symb - 1] == ' ':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ỹ' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'у' and text[symb - 2] == '˙' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    'ỹ' + text[symb - 2] + text[symb - 1] + text[symb])
   #'і', 'и', 'І', 'И', 'ĩ', 'ũ', 'ɴ', 'ɴ́', 'Ĩ', 'Ṹ', 'а', 'о', 'А', 'О', 'у', 'е', 'У', 'Е', 'ã', 'õ', 'Ã', 'Õ', 'ỹ', 'ẽ', 'Ỹ́', 'Ẽ', 'ǝ', 'ǝ̃'
            if text[symb - 1] == 'У':
                text = text.replace(
                    text[symb - 1] + text[symb], 'Ỹ' + text[symb])
            if text[symb - 2] == 'У' and text[symb - 1] == '˙':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'Ỹ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'У' and text[symb - 1] == ' ':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'Ỹ' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'У' and text[symb - 2] == '˙' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    'Ỹ' + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'е':
                text = text.replace(
                    text[symb - 1] + text[symb], 'ẽ' + text[symb])
            if text[symb - 2] == 'е' and text[symb - 1] == '˙':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ẽ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'е' and text[symb - 1] == ' ':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ẽ' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'е' and text[symb - 2] == '˙' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    'ẽ' + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'ə':
                text = text.replace(
                    text[symb - 1] + text[symb], 'ǝ̃' + text[symb])
            if text[symb - 2] == 'ə' and text[symb - 1] == '˙':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ǝ̃' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'ə' and text[symb - 1] == ' ':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ǝ̃' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'ə' and text[symb - 2] == '˙' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    'ǝ̃' + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'Е':
                text = text.replace(
                    text[symb - 1] + text[symb], 'Ẽ' + text[symb])
            if text[symb - 2] == 'Е' and text[symb - 1] == '˙':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'Ẽ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'Е' and text[symb - 1] == ' ':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'Ẽ' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'Е' and text[symb - 2] == '˙' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    'Ẽ' + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'и':
                text = text.replace(
                    text[symb - 1] + text[symb], 'ũ' + text[symb])
            if text[symb - 2] == 'и' and text[symb - 1] == '˙':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ũ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'и' and text[symb - 1] == ' ':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ũ' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'и' and text[symb - 2] == '˙' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    'ũ' + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'ɴ':
                text = text.replace(
                    text[symb - 1] + text[symb], 'ɴ́' + text[symb])
            if text[symb - 2] == 'ɴ' and text[symb - 1] == '˙':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ɴ́' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'ɴ' and text[symb - 1] == ' ':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ɴ́' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'ɴ' and text[symb - 2] == '˙' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    'ɴ́' + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'И':
                text = text.replace(
                    text[symb - 1] + text[symb], 'И̃' + text[symb])
            if text[symb - 2] == 'И' and text[symb - 1] == '˙':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'И̃' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'И' and text[symb - 1] == ' ':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'И̃' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'И' and text[symb - 2] == '˙' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    'И̃' + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'і':
                text = text.replace(
                    text[symb - 1] + text[symb], 'ĩ' + text[symb])
            if text[symb - 2] == 'і' and text[symb - 1] == '˙':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ĩ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'і' and text[symb - 1] == ' ':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'ĩ' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'і' and text[symb - 2] == '˙' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    'ĩ' + text[symb - 2] + text[symb - 1] + text[symb])

            if text[symb - 1] == 'І':
                text = text.replace(
                    text[symb - 1] + text[symb], 'Ĩ' + text[symb])
            if text[symb - 2] == 'І' and text[symb - 1] == '˙':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'Ĩ' + text[symb - 1] + text[symb])
            if text[symb - 2] == 'І' and text[symb - 1] == ' ':
                text = text.replace(
                    text[symb - 2] + text[symb - 1] + text[symb], 'Ĩ' + text[symb - 1] + text[symb])
            if text[symb - 3] == 'І' and text[symb - 2] == '˙' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    'Ĩ' + text[symb - 2] + text[symb - 1] + text[symb])

            # назалізація прогресивна
            if text[symb + 1] == 'а':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'ã')
            if text[symb + 1] == " " and text[symb + 2] == 'а':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ã')
            if text[symb + 1] == "´" and text[symb + 2] == 'а':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ã')
            if text[symb + 1] == '´' and text[symb + 2] == ' ' and text[symb + 3] == 'а':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ã')
            if text[symb + 1] == "’" and text[symb + 2] == 'а':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ã')
            if text[symb + 1] == '’' and text[symb + 2] == ' ' and text[symb + 3] == 'а':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ã')
            if text[symb + 1] == ':' and text[symb + 2] == 'а':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ã')
            if text[symb + 1] == ':' and text[symb + 2] == ' ' and text[symb + 3] == 'а':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ã')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == 'а':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ã')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == 'а':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ã')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == ' ' and text[symb + 4] == 'а':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ã')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == ' ' and text[symb + 4] == 'а':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ã')
 #'і', 'и', 'І', 'И', 'ĩ', 'и̃', 'ɴ', 'ɴ́', 'Ĩ', 'Ṹ', 'а', 'о', 'А', 'О', 'у', 'е', 'У', 'Е', 'ã', 'õ', 'Ã', 'Õ', 'ỹ', 'ẽ', 'Ỹ́', 'Ẽ', 'ə', 'ǝ̃'
            if text[symb + 1] == 'А':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'Ã')
            if text[symb + 1] == " " and text[symb + 2] == 'А':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ã')
            if text[symb + 1] == "´" and text[symb + 2] == 'А':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ã')
            if text[symb + 1] == '´' and text[symb + 2] == ' ' and text[symb + 3] == 'А':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ã')
            if text[symb + 1] == "’" and text[symb + 2] == 'А':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ã')
            if text[symb + 1] == '’' and text[symb + 2] == ' ' and text[symb + 3] == 'А':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ã')
            if text[symb + 1] == ':' and text[symb + 2] == 'А':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ã')
            if text[symb + 1] == ':' and text[symb + 2] == ' ' and text[symb + 3] == 'А':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ã')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == 'А':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ã')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == 'А':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ã')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == ' ' and text[symb + 4] == 'А':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Ã')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == ' ' and text[symb + 4] == 'А':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Ã')

            if text[symb + 1] == "˚" and text[symb + 2] == 'о':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'õ')
            if text[symb + 1] == '˚' and text[symb + 2] == ' ' and text[symb + 3] == 'о':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'õ')
            if text[symb + 1] == '´' and text[symb + 2] == '˚' and text[symb + 3] == 'о':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'õ')
            if text[symb + 1] == '´' and text[symb + 2] == '˚' and text[symb + 3] == ' ' and text[symb + 4] == 'о':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'õ')
            if text[symb + 1] == '’' and text[symb + 2] == '˚' and text[symb + 3] == 'о':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'õ')
            if text[symb + 1] == '’' and text[symb + 2] == '˚' and text[symb + 3] == ' ' and text[symb + 4] == 'о':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'õ')
            if text[symb + 1] == ':' and text[symb + 2] == '˚' and text[symb + 3] == 'о':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'õ')
            if text[symb + 1] == ':' and text[symb + 2] == '˚' and text[symb + 3] == ' ' and text[symb + 4] == 'о':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'õ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == '˚' and text[symb + 4] == 'о':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'õ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == '˚' and text[symb + 4] == 'о':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'õ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == '˚' and text[symb + 4] == ' ' \
                                                                                        and text[symb + 5] == 'о':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4] + text[symb + 5],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4] + 'õ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == '˚' and text[symb + 4] == ' ' \
                                                                                        and text[symb + 5] == 'о':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4] + text[symb + 5],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4] + 'õ')

            if text[symb + 1] == "˚" and text[symb + 2] == 'О':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Õ')
            if text[symb + 1] == '˚' and text[symb + 2] == ' ' and text[symb + 3] == 'О':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Õ')
            if text[symb + 1] == '´' and text[symb + 2] == '˚' and text[symb + 3] == 'О':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Õ')
            if text[symb + 1] == '´' and text[symb + 2] == '˚' and text[symb + 3] == ' ' and text[symb + 4] == 'О':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Õ')
            if text[symb + 1] == '’' and text[symb + 2] == '˚' and text[symb + 3] == 'О':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Õ')
            if text[symb + 1] == '’' and text[symb + 2] == '˚' and text[symb + 3] == ' ' and text[symb + 4] == 'О':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Õ')
            if text[symb + 1] == ':' and text[symb + 2] == '˚' and text[symb + 3] == 'О':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Õ')
            if text[symb + 1] == ':' and text[symb + 2] == '˚' and text[symb + 3] == ' ' and text[symb + 4] == 'О':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Õ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == '˚' and text[symb + 4] == 'О':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Õ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == '˚' and text[symb + 4] == 'О':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Õ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == '˚' and text[symb + 4] == ' ' \
                                                                                        and text[symb + 5] == 'О':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4] + text[symb + 5],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4] + 'Õ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == '˚' and text[symb + 4] == ' ' \
                                                                                        and text[symb + 5] == 'О':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4] + text[symb + 5],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4] + 'Õ')

            if text[symb + 1] == "˚" and text[symb + 2] == 'у':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ỹ')
            if text[symb + 1] == '˚' and text[symb + 2] == ' ' and text[symb + 3] == 'у':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ỹ')
            if text[symb + 1] == '´' and text[symb + 2] == '˚' and text[symb + 3] == 'у':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ỹ')
            if text[symb + 1] == '´' and text[symb + 2] == '˚' and text[symb + 3] == ' ' and text[symb + 4] == 'у':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ỹ')
            if text[symb + 1] == '’' and text[symb + 2] == '˚' and text[symb + 3] == 'у':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ỹ')
            if text[symb + 1] == '’' and text[symb + 2] == '˚' and text[symb + 3] == ' ' and text[symb + 4] == 'у':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ỹ')
            if text[symb + 1] == ':' and text[symb + 2] == '˚' and text[symb + 3] == 'у':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ỹ')
            if text[symb + 1] == ':' and text[symb + 2] == '˚' and text[symb + 3] == ' ' and text[symb + 4] == 'у':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ỹ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == '˚' and text[symb + 4] == 'у':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ỹ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == '˚' and text[symb + 4] == 'у':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ỹ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == '˚' and text[symb + 4] == ' ' \
                                                                                        and text[symb + 5] == 'у':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4] + text[symb + 5],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4] + 'ỹ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == '˚' and text[symb + 4] == ' ' \
                                                                                        and text[symb + 5] == 'у':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4] + text[symb + 5],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4] + 'ỹ')

            if text[symb + 1] == "˚" and text[symb + 2] == 'У':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ỹ')
            if text[symb + 1] == '˚' and text[symb + 2] == ' ' and text[symb + 3] == 'У':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ỹ')
            if text[symb + 1] == '´' and text[symb + 2] == '˚' and text[symb + 3] == 'У':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ỹ')
            if text[symb + 1] == '´' and text[symb + 2] == '˚' and text[symb + 3] == ' ' and text[symb + 4] == 'У':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Ỹ')
            if text[symb + 1] == '’' and text[symb + 2] == '˚' and text[symb + 3] == 'У':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ỹ')
            if text[symb + 1] == '’' and text[symb + 2] == '˚' and text[symb + 3] == ' ' and text[symb + 4] == 'У':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Ỹ')
            if text[symb + 1] == ':' and text[symb + 2] == '˚' and text[symb + 3] == 'У':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ỹ')
            if text[symb + 1] == ':' and text[symb + 2] == '˚' and text[symb + 3] == ' ' and text[symb + 4] == 'У':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Ỹ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == '˚' and text[symb + 4] == 'У':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Ỹ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == '˚' and text[symb + 4] == 'У':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Ỹ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == '˚' and text[symb + 4] == ' ' \
                                                                                        and text[symb + 5] == 'У':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4] + text[symb + 5],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4] + 'Ỹ')

            if text[symb + 1] == 'е':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'ẽ')
            if text[symb + 1] == " " and text[symb + 2] == 'е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ẽ')
            if text[symb + 1] == "´" and text[symb + 2] == 'е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ẽ')
            if text[symb + 1] == '´' and text[symb + 2] == ' ' and text[symb + 3] == 'е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ẽ')
            if text[symb + 1] == "’" and text[symb + 2] == 'е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ẽ')
            if text[symb + 1] == '’' and text[symb + 2] == ' ' and text[symb + 3] == 'е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ẽ')
            if text[symb + 1] == ':' and text[symb + 2] == 'е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ẽ')
            if text[symb + 1] == ':' and text[symb + 2] == ' ' and text[symb + 3] == 'е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ẽ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == 'е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ẽ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == 'е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ẽ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == ' ' and text[symb + 4] == 'е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ẽ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == ' ' and text[symb + 4] == 'е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ẽ')

            if text[symb + 1] == 'ə':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'ǝ̃')
            if text[symb + 1] == " " and text[symb + 2] == 'ə':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ǝ̃')
            if text[symb + 1] == "´" and text[symb + 2] == 'ə':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ǝ̃')
            if text[symb + 1] == '´' and text[symb + 2] == ' ' and text[symb + 3] == 'ə':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ǝ̃')
            if text[symb + 1] == "’" and text[symb + 2] == 'ə':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ǝ̃')
            if text[symb + 1] == '’' and text[symb + 2] == ' ' and text[symb + 3] == 'ə':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ǝ̃')
            if text[symb + 1] == ':' and text[symb + 2] == 'ə':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ǝ̃')
            if text[symb + 1] == ':' and text[symb + 2] == ' ' and text[symb + 3] == 'ə':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ǝ̃')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == 'ə':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ǝ̃')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == 'ə':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ǝ̃')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == ' ' and text[symb + 4] == 'ə':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ǝ̃')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == ' ' and text[symb + 4] == 'ə':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ǝ̃')

            if text[symb + 1] == 'Е':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'Ẽ')
            if text[symb + 1] == " " and text[symb + 2] == 'Е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ẽ')
            if text[symb + 1] == "´" and text[symb + 2] == 'Е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ẽ')
            if text[symb + 1] == '´' and text[symb + 2] == ' ' and text[symb + 3] == 'Е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ẽ')
            if text[symb + 1] == "’" and text[symb + 2] == 'Е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ẽ')
            if text[symb + 1] == '’' and text[symb + 2] == ' ' and text[symb + 3] == 'Е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ẽ')
            if text[symb + 1] == ':' and text[symb + 2] == 'Е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ẽ')
            if text[symb + 1] == ':' and text[symb + 2] == ' ' and text[symb + 3] == 'Е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ẽ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == 'Е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ẽ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == 'Е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ẽ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == ' ' and text[symb + 4] == 'Е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Ẽ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == ' ' and text[symb + 4] == 'Е':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Ẽ')
#'ə', 'ǝ̃'
            if text[symb + 1] == 'и':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'ũ')
            if text[symb + 1] == " " and text[symb + 2] == 'и':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ũ')
            if text[symb + 1] == "´" and text[symb + 2] == 'и':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ũ')
            if text[symb + 1] == '´' and text[symb + 2] == ' ' and text[symb + 3] == 'и':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ũ')
            if text[symb + 1] == "’" and text[symb + 2] == 'и':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ũ')
            if text[symb + 1] == '’' and text[symb + 2] == ' ' and text[symb + 3] == 'и':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ũ')
            if text[symb + 1] == ':' and text[symb + 2] == 'и':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ũ')
            if text[symb + 1] == ':' and text[symb + 2] == ' ' and text[symb + 3] == 'и':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ũ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == 'и':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ũ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == 'и':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ũ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == ' ' and text[symb + 4] == 'и':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ũ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == ' ' and text[symb + 4] == 'и':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ũ')

            if text[symb + 1] == 'ɴ':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'ɴ́')
            if text[symb + 1] == " " and text[symb + 2] == 'ɴ':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ɴ́')
            if text[symb + 1] == "´" and text[symb + 2] == 'ɴ':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ɴ́')
            if text[symb + 1] == '´' and text[symb + 2] == ' ' and text[symb + 3] == 'ɴ':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ɴ́')
            if text[symb + 1] == "’" and text[symb + 2] == 'ɴ':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ɴ́')
            if text[symb + 1] == '’' and text[symb + 2] == ' ' and text[symb + 3] == 'ɴ':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ɴ́')
            if text[symb + 1] == ':' and text[symb + 2] == 'ɴ':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ɴ́')
            if text[symb + 1] == ':' and text[symb + 2] == ' ' and text[symb + 3] == 'ɴ':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ɴ́')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == 'ɴ':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ɴ́')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == 'ɴ':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ɴ́')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == ' ' and text[symb + 4] == 'ɴ':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ɴ́')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == ' ' and text[symb + 4] == 'ɴ':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ɴ́')
#'і', 'и', 'І', 'И', 'ĩ', 'и̃', 'ɴ', 'ɴ́', 'Ĩ', 'Ṹ'
            if text[symb + 1] == 'И':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'Ṹ')
            if text[symb + 1] == " " and text[symb + 2] == 'И':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ṹ')
            if text[symb + 1] == "´" and text[symb + 2] == 'И':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ṹ')
            if text[symb + 1] == '´' and text[symb + 2] == ' ' and text[symb + 3] == 'И':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ṹ')
            if text[symb + 1] == "’" and text[symb + 2] == 'И':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ṹ')
            if text[symb + 1] == '’' and text[symb + 2] == ' ' and text[symb + 3] == 'И':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ṹ')
            if text[symb + 1] == ':' and text[symb + 2] == 'И':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ṹ')
            if text[symb + 1] == ':' and text[symb + 2] == ' ' and text[symb + 3] == 'И':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ṹ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == 'И':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ṹ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == 'И':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ṹ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == ' ' and text[symb + 4] == 'И':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Ṹ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == ' ' and text[symb + 4] == 'И':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Ṹ')

            if text[symb + 1] == 'і':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'ĩ')
            if text[symb + 1] == " " and text[symb + 2] == 'і':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ĩ')
            if text[symb + 1] == "´" and text[symb + 2] == 'і':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ĩ')
            if text[symb + 1] == '´' and text[symb + 2] == ' ' and text[symb + 3] == 'і':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ĩ')
            if text[symb + 1] == "’" and text[symb + 2] == 'і':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ĩ')
            if text[symb + 1] == '’' and text[symb + 2] == ' ' and text[symb + 3] == 'і':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ĩ')
            if text[symb + 1] == ':' and text[symb + 2] == 'і':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'ĩ')
            if text[symb + 1] == ':' and text[symb + 2] == ' ' and text[symb + 3] == 'і':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ĩ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == 'і':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ĩ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == 'і':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'ĩ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == ' ' and text[symb + 4] == 'і':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ĩ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == ' ' and text[symb + 4] == 'і':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'ĩ')

            if text[symb + 1] == 'І':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + 'Ĩ')
            if text[symb + 1] == " " and text[symb + 2] == 'І':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ĩ')
            if text[symb + 1] == "´" and text[symb + 2] == 'І':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ĩ')
            if text[symb + 1] == '´' and text[symb + 2] == ' ' and text[symb + 3] == 'І':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ĩ')
            if text[symb + 1] == "’" and text[symb + 2] == 'І':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ĩ')
            if text[symb + 1] == '’' and text[symb + 2] == ' ' and text[symb + 3] == 'І':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ĩ')
            if text[symb + 1] == ':' and text[symb + 2] == 'І':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2], text[symb] + text[symb + 1] + 'Ĩ')
            if text[symb + 1] == ':' and text[symb + 2] == ' ' and text[symb + 3] == 'І':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ĩ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == 'І':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ĩ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == 'І':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                    text[symb] + text[symb + 1] + text[symb + 2] + 'Ĩ')
            if text[symb + 1] == '´' and text[symb + 2] == ':' and text[symb + 3] == ' ' and text[symb + 4] == 'І':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Ĩ')
            if text[symb + 1] == ':' and text[symb + 2] == '’' and text[symb + 3] == ' ' and text[symb + 4] == 'І':
                text = text.replace(
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + text[symb + 4],
                    text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3] + 'Ĩ')



        # і-подібна артикуляція прогресивна
        if text[symb] in vowels[10:]:
            if text[symb - 1] == 'й':
                text = text.replace(
                    text[symb - 1] + text[symb], text[symb - 1] + '˙' + text[symb])
            if text[symb - 2] == 'й' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 2] + text[symb - 1] + '˙' + text[symb])
            if text[symb - 2] == 'й' and text[symb - 1] == '˚':
                text = text.replace(text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 2] + text[symb - 1] + '˙' + text[symb])
            if text[symb - 3] == 'й' and text[symb - 2] == '˚' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 3] + text[symb - 2] + ' ' + '˙' + text[symb])
            if text[symb - 1] == 'j':
                text = text.replace(
                    text[symb - 1] + text[symb], text[symb - 1] + '˙' + text[symb])
            if text[symb - 2] == 'j' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 2] + text[symb - 1] + '˙' + text[symb])
            if text[symb - 2] == 'j' and text[symb - 1] == '˚':
                text = text.replace(text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 2] + text[symb - 1] + '˙' + text[symb])
            if text[symb - 3] == 'j' and text[symb - 2] == '˚' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 3] + text[symb - 2] + ' ' + '˙' + text[symb])
            if text[symb - 1] == '´':
                text = text.replace(
                    text[symb - 1] + text[symb], text[symb - 1] + '˙' + text[symb])
            if text[symb - 2] == '´' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 2] + text[symb - 1] + '˙' + text[symb])
            if text[symb - 2] == '´' and text[symb - 1] == '˚':
                text = text.replace(text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 2] + text[symb - 1] + '˙' + text[symb])
            if text[symb - 3] == '´' and text[symb - 2] == '˚' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 3] + text[symb - 2] + text[symb - 1] + '˙' + text[symb])
            if text[symb - 2] == '´' and text[symb - 1] == ':':
                text = text.replace(text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 2] + text[symb - 1] + '˙' + text[symb])
            if text[symb - 3] == '´' and text[symb - 2] == ':' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 3] + text[symb - 2] + text[symb - 1] + '˙' + text[symb])
            if text[symb - 3] == '´' and text[symb - 2] == ':' and text[symb - 1] == '˚':
                text = text.replace(text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 3] + text[symb - 2] + text[symb - 1] + '˙' + text[symb])
            if text[symb - 4] == '´' and text[symb - 3] == ':' and text[symb - 2] == '˚' and text[symb - 1] == ' ':
                text = text.replace(text[symb - 4] + text[symb - 3] + text[symb - 2] + text[symb - 1] + text[symb],
                                    text[symb - 4] + text[symb - 3] + text[symb - 2] + text[symb - 1] + '˙' +
                                    text[symb])

            # і-подібна артикуляція регресивна
            if text[symb + 1] == 'j':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + '˙' + text[symb + 1])
            if text[symb + 1] == ' ' and text[symb + 2] == 'j':
                text = text.replace(text[symb] + text[symb + 1] + text[symb + 2],
                                    text[symb] + '˙' + text[symb + 1] + text[symb + 2])
            if text[symb + 1] == 'й':
                text = text.replace(
                    text[symb] + text[symb + 1], text[symb] + '˙' + text[symb + 1])
            if text[symb + 1] == ' ' and text[symb + 2] == 'й':
                text = text.replace(text[symb] + text[symb + 1] + text[symb + 2],
                                    text[symb] + '˙' + text[symb + 1] + text[symb + 2])
            if (text[symb + 1] + text[symb + 2]) in softy:
                text = text.replace(text[symb] + text[symb + 1] + text[symb + 2],
                                    text[symb] + '˙' + text[symb + 1] + text[symb + 2])
            if (text[symb + 1] + text[symb + 2]) == 'р' + '´':
                text = text.replace(text[symb] + text[symb + 1] + text[symb + 2],
                                    text[symb] + '˙' + text[symb + 1] + text[symb + 2])
            if text[symb + 1] == ' ' and (text[symb + 2] + text[symb + 3]) in softy:
                text = text.replace(text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                                    text[symb] + '˙' + text[symb + 1] + text[symb + 2] + text[symb + 3])
            if text[symb + 1] == ' ' and (text[symb + 2] + text[symb + 3]) == 'р' + '´':
                text = text.replace(text[symb] + text[symb + 1] + text[symb + 2] + text[symb + 3],
                                    text[symb] + '˙' + text[symb + 1] + text[symb + 2] + text[symb + 3])


    text = re.sub(r'    /', '', text)
    text = re.sub(r'/    ', '', text)

    return f'[{text}]'

# print(transcript_the_text_phonetic("передзига"))
# "Садок вишневий коло хати, Хрущі над вишнями гудуть, Плугатарі з плугами йдуть, Співають ідучи дівчата, А матері вечерять ждуть."
