import random
def leet_decoration(nick):
    if len(nick) < 21:
        count_nick = len(nick)
        i = 0
        if count_nick < 7:
            nickd = nick
            nickd = nickd.title()
            nickd = nickd.swapcase()
            list_nick_low = []
            list_nick_low.extend(nickd)
            rr = random.randint(1, len(nickd) - 1)
            string_extra = '%^#@'

            list_nick_low[rr] = list_nick_low[rr] + list_nick_low[rr] + random.choice(string_extra)
            stringd = ''.join(list_nick_low)
            return stringd
        else:
            list_nick = []
            list_nick.extend(nick)
            posthree = None
            backspace_c = None
            count_i = 0
            while i < count_nick:
                if list_nick[i] == 'e' or list_nick[i] == 'E':
                    list_nick[i] = '3'
                    posthree = i - 1
                if list_nick[i] == 'l' and i!=0 and list_nick[i]!=list_nick[1] or list_nick[i] == 'i' or list_nick[i] == 'I':
                    count_i +=1
                    if count_i < 3:
                        list_nick[i] = '1'
                        posthree  = i - 1
                if list_nick[i] == 't':
                    list_nick[i] = 'T'
                if list_nick[i] == 'a' or list_nick[i] =='A':
                    list_nick[i] = '4'
                if list_nick[i] == ' ' or list_nick[i] == '-':
                    backspace_c = i
                i+=1
            rr = random.randint(1, len(nick) - 1)
            string_extra = '%^#@'

            list_nick[rr] = list_nick[rr] + random.choice(string_extra)
            if backspace_c == None:
                if posthree!=None:
                    if (posthree + 2) < count_nick:
                        for i in range(posthree + 2, count_nick):
                            list_nick[i] = list_nick[i].upper()
            elif posthree!=None and backspace_c > 0 and (posthree + 2) < count_nick:
                for i in range(posthree + 2, backspace_c):
                    list_nick[i] = list_nick[i].upper()

            if posthree!=None and posthree > 0:
                list_nick[posthree] = list_nick[posthree].upper()



        string = ''.join(list_nick)
        return string
    else:
        return 'Строка слишком большая! Максимальное количество символов для вызова функции - 20'
