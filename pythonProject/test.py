per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input("Введите сумму вклада"))

deposit = [money/100*i for i in per_cent.values()]

print("максимальная сумма которую вы можете заработать",round(max(deposit),2))