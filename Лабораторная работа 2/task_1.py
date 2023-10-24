money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

budget = salary + money_capital # Бюджет на месяц
month = 0 # Количество месяцев

while budget >= spend:
    month += 1
    money_capital -= spend - salary

    budget = salary + money_capital
    spend += spend * increase

print("Количество месяцев, которое можно протянуть без долгов:", month)
