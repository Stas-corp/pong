import json
workers = {
    'Stas':{
        'должность':'препод',
        'эффективность':100,
        'портфолио':['Main', 'NFS', 'XCOM']
    },

    'Ivan':{
        'должность':'ученик',
        'эффективность':70,
        'портфолио':['Arcanoid', 'Cliker', 'WoT']
    },

    'Cat':{
        'должность':'домашнее живтное',
        'эффективность':2,
        'портфолио':['Ссаные тапки', 'Куча по среди комнаты']
    },

    'Vadim':{
        'должность':'главный по Pepsi',
        'эффективность':17,
        'портфолио':['0.5 за один глоток', 'Куча по среди комнаты']
    }
}

with open ('workers.json','w', encoding='utf-8') as f:
    json.dump(workers, f)

employees = workers.keys()

print('Имена сотрудников:')
for i in employees:
    print('-', i + ', должность:', workers[i]['должность'])

print('Портфолио сотрудника:')
for i in employees:
    print('-', i + ', портфолио:')
    for e in workers[i]['портфолио']:
        print('Проект:','"' + e + '"')

with open('workers.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(data)