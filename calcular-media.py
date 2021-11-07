import time
def CalculateAverage():
    i = 1
    error_msg = "Por favor coloque um número entre 0 e 10 (exemplo: 7.5)"
    again_error_msg = "Digite: sim ou não"
    end_error_msg = "Digite: sim ou não"
    while i >= 1 and i <= 4:
            try:
                if i == 1:
                    N1 = round(float(input('Digite sua N1: ')), 2)
                    if N1 >= 0 and N1 <= 10:
                        i += 1
                        continue
                    else:
                        print(error_msg)
                        continue
                if i == 2:
                    N2 = round(float(input('Digite sua N2: ')), 2)
                    if N2 >= 0 and N2 <= 10:
                        i += 1
                        continue
                    else:
                        print(error_msg)
                        continue
                if i == 3:
                    N3 = round(float(input('Digite sua N3: ')), 2)
                    if N3 >= 0 and N3 <= 10:
                        i += 1
                        continue
                    else:
                        print(error_msg)
                        continue
                if i == 4:
                    N4 = round(float(input('Digite sua N4: ')), 2)
                    if N4 >= 0 and N4 <= 10:
                        i += 1
                        continue
                    else:
                        print(error_msg)
                        continue
            except:
                print(error_msg)
                continue
    average = round((N1+N2+N3+N4)/(4), 2)
    average_msg = "Sua média é: {average}"
    print(average_msg.format(average = average))
    while i == 5:
        try:
            end = input("Deseja calcular novamente? (s/n): ")
            if end == "s" or end == "sim" or end == "y" or end == "yes":
                i = 0
                CalculateAverage()
            elif end == "n" or end == "não" or end == "nao" or end == "n" or end == "no":
                i = 6
                break
            else:
                print(again_error_msg)
                continue
        except:
            print(again_error_msg)
    while i == 6:
        try:
            end = input("Deseja finalizar a aplicação? (s/n): ")
            if end == "s" or end == "sim" or end == "y" or end == "yes":
                break
            elif end == "n" or end == "não" or end == "nao" or end == "n" or end == "no":
                i = 7
                break
            else:
                print(end_error_msg)
                continue
        except:
            print(end_error_msg)
    while i == 7:
        time.sleep(60)

CalculateAverage()