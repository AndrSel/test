groupmates = [
{
"name": "Александр",
"surname": "Иванов",
"exams": ["Информатика", "ЭЭиС", "Web"],
"marks": [4, 3, 5]
},
{
 "name": "Андрей",
 "surname": "Селезнев",
 "exams": ["Философия", "Матан", "Ин.яз"],
 "marks": [3, 3, 3]
},
{
"name": "Кирилл",
"surname": "Смирнов",
"exams": ["Философия", "ИС", "КТП"],
"marks": [4, 3, 3]
},
{
"name": "Илья",
"surname": "Алексеев",
"exams": ["История", "ИС", "КТП"],
"marks": [3, 5, 5]
},
{
"name": "Артур",
"surname": "Лебедев",
"exams": ["Философия", "Web", "ИС"],
"marks": [5, 4, 3]
},
{
"name": "Ботан",
"surname": "Ботанов",
"exams": ["Философия", "Web", "ИС"],
"marks": [5, 5, 5]
}
]
#print(groupmates)

def function1(sredniy_ball_po_kotoromy_proishodit_filtr):
	for i in range(len(groupmates)):
		studenti = (groupmates[i])
		spisok_otsenok = studenti['marks']
		otsenka1 = spisok_otsenok[0]
		otsenka2 = spisok_otsenok[1]
		otsenka3 = spisok_otsenok[2]
		srednee_znachenie = int((otsenka1 + otsenka2 + otsenka3)/3)
		if srednee_znachenie >= sredniy_ball_po_kotoromy_proishodit_filtr:
			a = spisok_otsenok = studenti['name']
			b = spisok_otsenok = studenti['surname']
			print (a,b)

u = int(input('Введите средний балл, по которому будет проводиться фильтрация: '))
function1(u)

