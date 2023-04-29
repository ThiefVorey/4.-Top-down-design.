class CATDATE():
    global catdata
    global i
    i=-1
    catdata={"Name":[], "Health":[],"Location":[]}
    def catname():
        cat=input("Позывной котенка:")
        return cat
    def kitty(cat):
        print('Состояние котенка (1 ужасно, а 10 здоров) ',cat,':')
        while True:
            try:
                health=int(input())
                if (health>=1) and(health<=10):break
                else: raise ValueError
            except ValueError:
                print("Значения только от 1 до 10")    
        return health
    def location(cat, health):
        print('Местоположение котенка ',cat,' с состоянием ', health,':')
        place=input()
        return place
    def catinput():
        global i
        i+=1
        catdata.get("Name").append(CATDATE.catname())
        catdata.get("Health").append(CATDATE.kitty(catdata.get("Name")[i]))
        catdata.get("Location").append(CATDATE.location(catdata.get("Name")[i],catdata.get("Health")[i]))
        return 
    
class VETDATE():
    global j
    j=-1
    global vetdata
    vetdata={"Vet":[], "Busy":[]}
    def volunteer():
        print("Ветеринар:")
        who=input()
        return who
    def employment(who):
        while True:
            bus=''
            print(who,' состояние занятости(свободен или занят):')
            bus=input()
            if bus=='занят':
                break
            elif bus=='свободен':
                break
            else:
                print('Только свободен или занят')

        return bus
    def vetinput():
        global j
        j+=1
        vetdata.get("Vet").append(VETDATE.volunteer())
        vetdata.get("Busy").append(VETDATE.employment(vetdata.get("Vet")[j]))
        return
class treatment():
    global vetdata, catdata
    global j1,i1
    def svoboda(vetdata):
        global j1
        for c in range(len(vetdata.get("Vet"))):
            if vetdata.get("Busy")[c]=='свободен':
                j1=c
                break
        if vetdata.get("Busy")[j1]=='занят':
            print('Нет свободных ветеринаров')
            return menu.m()
        else:
            return j1
    def badcat(catdata):
        global i1
        buble=100
        for d in range(len(catdata.get("Name"))):
            if buble>(catdata.get("Health")[d]):
                buble=catdata.get("Health")[d]
                i1=d
        if catdata.get("Health")[i1]==10:
            print('Нет больных котят')
            return menu.m()
        else:
            return i1
    def gear():
        global vetdata, catdata
        global i1,j1
        j1=treatment.svoboda(vetdata)
        i1=treatment.badcat(catdata)
        return treatment. cure(vetdata.get("Vet")[j1],catdata.get("Name")[i1],catdata.get("Health")[i1],catdata.get("Location")[i1])
    def cure(who, cat, health, place ):
        print('Ветеринар ', who,' лечит котенка ',cat,' с состоянием здоровья ',health,' в месте ',place, '.')
        vetdata.get("Busy")[j1]='занят'
        catdata.get("Health")[i1]=10

        return treatment.result()
    def result():
        print('Котенок здоров!')
        return
