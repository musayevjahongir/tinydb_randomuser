from tinydb import TinyDB
from api import get_users_by_gender

db = TinyDB('data.json', indent=4)

male=get_users_by_gender("male", 30)
female=get_users_by_gender("female", 30)

males=db.table(name='males')
females=db.table(name='females')


for i in male:
    males.insert(i)
for i in female:
    females.insert(i)
