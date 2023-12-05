 ## Final Review 

# 1.การใช้lamda

case 1 (filter ปกติ) : print('#1: What player on a team with “ia” in the team name played less than 200 minutes and made more than 100 passes? Select to display the player surname, team, and position')
print()
filter_player = table3.filter(lambda x: 'ia' in x['team'] and int(x['minutes']) < 200 and int(x['passes']) > 100)
select_player = filter_player.select(['surname', 'team', 'position'])

case 2 (ใช้ aggreate function): print('#2: The average number of games played for teams ranking below 10 versus teams ranking above or equal 10')
print()
ranking_above_ten = table4.filter(lambda x: int(x['ranking']) >= 10)
ranking_below_ten = table4.filter(lambda x: int(x['ranking']) < 10)

avg_above_10 = ranking_above_ten.aggregate(lambda x: sum(x)/len(x), 'games')
avg_below_10 = ranking_below_ten.aggregate(lambda x: sum(x)/len(x), 'games')
#game คือ col นึงที่อยู่ใน Team.csv file 


# 2.วิธีเปิดไฟล์ csv
import csv

with open('test.csv' , mode = 'r') as f:
    csvFile = csv.DictReader(f)

    # print(csvFile)

    for i in csvFile:
        print(i)

# 3.วิธีอ่าน  + เขียน ไฟล์ json 

import json
#dump ข้อมูลเข้าไป

python_obj = {'name': 'John', 'age': 30}
with open('books.json', 'w') as file:
    json.dump(python_obj, file)

load ข้อมูลออกมา

with open('books.json', 'r') as file:
    python_obj = json.load(file)
print(python_obj)
 


# 4. เวลาเราจะ convert code จาก procederul code ไปเป็น OOP มีข้อควรระวังอะไรบ้าง

   Identifying Classes:
    Properly identifying and defining classes is foundational. Break down the procedural code into logical units and encapsulate related data        and behavior into appropriate classes.

    Encapsulation:
    Ensure effective encapsulation by using access modifiers to control the visibility of class members. This helps in hiding internal details       and providing a clear interface for interacting with objects.

   Inheritance vs. Composition:
     Understand when to use inheritance and when to favor composition. Avoid creating overly complex class hierarchies and choose the approach         that best models the relationships between classes.

   Refactoring:
   Incrementally refactor the codebase. Gradually convert procedural functions into methods within classes to maintain a working codebase while     transitioning to OOP.


# 5. วิธีเขียน file csv
import csv

data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

with open('example.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerows(data)
