import os
FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "progress_tracker.txt"
)
print(FILE_PATH)
import time
from datetime import date
PLATFORM = ['Leetcode', 'Codewars', 'Exercism']
DIFFICULTY = ['Easy', 'Medium', 'Hard']
TOPIC = [
    "Arrays",
    "Hashing",
    "Two Pointers",
    "Stack",
    "Binary Search",
    "Linked List",
    "Trees",
    "Heap",
    "Graphs",
    "Dynamic Programming"
]
def add_progress():
    print('''\t\t\t=== Add Completed Problem ===''')
    print("Enter the details of the problem you solved today.")
    while True:    
        name=input("Problem Name: ").strip()
        if name:
            break
        print("Problem name cannot be empty")
    for i in range(len(TOPIC)):
        print(f"{i+1}.{TOPIC[i]}")
    while True:
        topic=input("Enter Topic: ")
        if topic.isdigit() and int(topic)>0 and int(topic)<=len(TOPIC):
            break
        print("Enter valid input")
    topic=TOPIC[int(topic)-1]
    while True:
        platform=input('''\n1.Leetcode
        2.Codewars
        3.Exercism
        Enter platform name(1/2/3): ''')
        if platform in ['1','2','3']:
            break
        print("Enter valid input")
    platform=PLATFORM[int(platform)-1]
    while True:
        difficulty=input('''\n1.Easy
        2.Medium
        3.Hard
        Enter Difficulty level(1/2/3): ''')
        if difficulty in ['1','2','3']:
            break
        print("Enter valid input")
    difficulty=DIFFICULTY[int(difficulty)-1]
    while True:
        tm=input("Time taken(in min): ")
        if tm.isdigit() and int(tm)>0:
            break
        print("Enter valid input")
    today=date.today().strftime("%d %B %Y")
    save_progress(name,topic,platform,difficulty,tm,today)
    print("\nProblem recorded successfully!\n")
def save_progress(name,topic,platform,difficulty,tm,today):
    with open(FILE_PATH,'a')as f:
        f.write('|'.join([name,topic,platform,difficulty,tm,today])+'\n')
def view_progress():
    print("\t\t\t=== View Progress ===")
    print("Review your learning history and track the progress you have made so far.")
    try:
        with open(FILE_PATH, 'r') as f:
            records = list(f)
    except FileNotFoundError:
        print("\nNo progress file found.")
        print("Start by adding your first solved problem!\n")
        return
    if not records:
        print("\nNo records found.")
        print("Total problems solved: 0\n")
        return
    c = 1
    counts=dict.fromkeys(DIFFICULTY,0)
    min_prob=max_prob=''
    max_t=tot=0
    min_t=float('inf')
    pltfm=dict.fromkeys(PLATFORM,0)
    topic=dict.fromkeys(TOPIC,0)
    for record in records:
        record = record.strip().split('|')
        print("\nSL NO.:", c)
        print("Problem name:", record[0])
        print("Topic:", record[1])
        topic[record[1]]+=1
        print("Platform:", record[2])
        pltfm[record[2]]+=1
        print("Difficulty:", record[3])
        counts[record[3]]+=1
        print("Time taken:", record[4], "min")
        tot+=int(record[4])
        if max_t<int(record[4]):
            max_t=int(record[4])
            max_prob=record[0]
        if min_t>int(record[4]):
            min_t=int(record[4])
            min_prob=record[0]
        print("Date solved:", record[5])
        c += 1
        print("\n"+'-'*25)
    avg=tot/(c-1)
    print("\t\t\t===PROGRESS DASHBOARD===")
    print("Topic statistics:\n")
    for i,j in topic.items():
        print(f"{i}: {j}")
    print("Platform statistics:\n")
    for i,j in pltfm.items():
        print(f"{i}: {j}")
    print("\nTotal problems solved:", c - 1)
    for i,j in counts.items():
        print(f"{i} count: {j}")
    print("Fastest solve:", min_prob,min_t, "min")
    print("Slowest solve:", max_prob,max_t, "min")
    print(f"Average solving time: {avg:.2f} min")
print("\t\t\t=== Personal Learning Tracker ===")
print('''Learning new skills requires consistency and proper tracking. Personal Learning Tracker, helps
users keep a record of what they have learned, what they are currently studying, and what remains to
be completed. The goal is to make self-learning more organized and efficient.\n\n\n''')
while True:
    while True:
        print("\n1.Add completed problems")
        print("2.View progress")
        print("3.Exit")
        c=input("Enter your choice: ")
        if c in ['1','2','3']:
            break
        print("\nPlease enter a valid choice\n")
        time.sleep(1)
    c=int(c)
    if c==1:
        add_progress()
    elif c==2:
        view_progress()
    elif c==3:
        print("\nThank you for using Personal Learning Tracker\nGoodbye!\n\n")
        time.sleep(1)
        exit()
