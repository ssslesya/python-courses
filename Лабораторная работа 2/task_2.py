salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = spend - salary  # Подушка безопасности

for i in range(2, 11):
    spend += spend * increase
    money_capital += spend - salary

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
