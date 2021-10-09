while True:
    alf_EU = "absdefghijklmnopqrstuvwxyzabsdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWABCDEFGHIJKLMNOPQRSTUVWabsdefghijklmnopqrstuvwxyzabsdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWABCDEFGHIJKLMNOPQRSTUVWабвгґдуєжзиіїйкльмншщпрстуфхцчшщьюяабвгґдуєжзиіїйкльмншщпрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
    step = int(input("Enter key: "))
    message = input("Enter symbols : ")
    result = ""
    for i in message:
        cell = alf_EU.find(i)
        new_cell = cell + step
        if i in alf_EU:
            result += alf_EU[new_cell]
        else:
            result += i
    print(result)
