def first_step():
    print ("enter the calcul : ")
    number = raw_input()
    numbeleght = list(number)  # list of all number and operateur and a9wass
    nmbr = []  # list of number only
    placeoper = []  # list of place of operateur
    a9wass = []  # list of a9waas place
    vip = ''
    # loop to sheqr in number and split from it and operateur
    for i in range(len(numbeleght)):
        # conditon to know this a condition and add the full number
        if numbeleght[i] == '+' or numbeleght[i] == '-' or numbeleght[i] == '/' or numbeleght[i] == '*':
            nmbr.append(vip)  # add the full number
            placeoper.append(i)  # creat order to know place of operateur
            vip = ''  # emty var
            continue  # countinue to new case with out saving operateur with number
        elif numbeleght[i] == '(' or numbeleght[i] == ')':  # place of a9waass
            a9wass.append(i)  # add place of a9wass
            continue
        vip = vip + numbeleght[i]  # variable who save the value of number in cases befor add the full number
    nmbr.append(vip)  # this make us to add the last number to the list of number who createt
    print ordering(nmbr, numbeleght, placeoper, a9wass)


def operat(nmbr, placeoper, numbeleght):  # do the cal bethwen number and the operateur ( + , _)
    cal = nmbr[0]  # the first number in nmbr
    for j in range(len(placeoper)):
        if numbeleght[placeoper[j]] == '+':
            cal = float(cal) + float(nmbr[j + 1])
        elif numbeleght[placeoper[j]] == '-':
            cal = float(cal) - float(nmbr[j + 1])
    return cal


def bettwen_a9wass(nmbr, numbeleght, placeoper, a9wass):
    f = 0
    l = 0
    o = 0
    for i in placeoper:

        if int(a9wass[0]) - 1 == int(i):
            break
        f = f + 1

    for i in placeoper:

        if int(a9wass[1]) + 1 == int(i):
            break
        l = l + 1

    f = f + 1
    #l = l - 1
    j = f
    #for i in range(f, l):
    i=f
    while l > f:

        if numbeleght[placeoper[i]] == '*':
            o = int(nmbr[i]) * int(nmbr[i + 1])
            l = l - 1
            placeoper[i] = ''
            nmbr[i] = o
            nmbr[i + 1] = ''
            placeoper.remove('')
            nmbr.remove('')

        elif numbeleght[placeoper[i]] == '/':

            o = int(nmbr[i]) / int(nmbr[i + 1])
            l = l - 1
            placeoper[i] = ''
            nmbr[i] = o
            nmbr[i + 1] = ''
            placeoper.remove('')
            nmbr.remove('')
        i=i+1
    #for j in range(f, l):
    while l > f:
        if numbeleght[placeoper[j]] == '+':

            o = int(nmbr[j]) + int(nmbr[j + 1])
            l = l - 1
            placeoper[j] = ''
            nmbr[j] = o
            nmbr[j + 1] = ''
            placeoper.remove('')
            nmbr.remove('')

        elif numbeleght[placeoper[j]] == '-':

            o = int(nmbr[j]) - int(nmbr[j + 1])
            l = l - 1
            placeoper[j] = ''
            nmbr[j] = o
            nmbr[j + 1] = ''
            placeoper.remove('')
            nmbr.remove('')
        j=j+1


def ordering(nmbr, numbeleght, placeoper, a9wass):
    for k in placeoper:
        if numbeleght[k]=='(':
            bettwen_a9wass(nmbr, numbeleght, placeoper, a9wass)
    p = 0
    o = 0
    for i in placeoper:
        if numbeleght[i] == '/' or numbeleght[i] == '*':
            if numbeleght[i] == '*':
                o = int(nmbr[p]) * int(nmbr[p + 1])
            elif numbeleght[placeoper[p]] == '/':
                o = int(nmbr[p]) / int(nmbr[p + 1])
            placeoper[p] = ''
            nmbr[p] = o
            nmbr[p + 1] = ''
            placeoper.remove('')
            nmbr.remove('')
        p = p + 1
    print placeoper
    print numbeleght
    print nmbr
    print a9wass
    cal = operat(nmbr, placeoper, numbeleght)
    return cal


if __name__ == '__main__':
    first_step()
