language = input("Язык программирования 'Python', 'Java', 'Javascript' :  ")
age = int(input("Возраст : "))
experience = int(input("Опыт :"))
the = int(input("Желаемая зарплата :"))
if language in ["Python", "Java", "javascript"] and 18<= age <= 65 and experience >= 3 and the >= 60000:
    print("Кандидат принят")
else:
    print("Кандидат не принят")
