"""
To-do List application
======================

PHASE 1 CAPSTONE: finish this and you move to Phase 2.

Uses only what you've covered so far: variables, input and typecasting, operators,
strings, lists, tuples, dicts, sets, if/elif/else, for/while, break/continue,
functions (with parameters, return values and *args), and f-string formatting.
No classes, no files, no try/except. Those come later.

-------------------------------------------------------------------------------
WHAT TO BUILD
-------------------------------------------------------------------------------
A command-line to-do app that keeps running until the user quits.

Each task is a DICT:
    {"id": 1, "title": "Buy milk", "priority": "high", "done": False, "tags": {"home"}}

All tasks live in a LIST of those dicts: tasks = []

The menu, shown again after every action:

    ===== TO-DO =====
    1. Add task
    2. View tasks
    3. Mark task done
    4. Delete task
    5. Search
    6. Stats
    7. Quit
    Choose:

-------------------------------------------------------------------------------
REQUIRED FUNCTIONS (signatures are fixed; write the bodies)
-------------------------------------------------------------------------------
Each function does ONE job. Only main() and the prompt functions call input().

1. show_menu() -> None
       Print the menu.

2. read_choice() -> int
       Keep asking until the user types a number from 1 to 7, then return it as an int.
       "abc", "", "9" and " 3 " should all be handled (hint: .strip(), .isdigit()).
       Use a while loop. Don't crash on bad input.

3. add_task(tasks, title, priority, *tags) -> dict
       Create the task dict and append it to tasks. Return the new task.
       - id = 1 more than the largest existing id (NOT len(tasks): think about why
         after you write delete_task)
       - title: whitespace cleaned up, as in debugging.py ("  buy   milk " -> "Buy milk")
       - priority must be "low", "medium" or "high" (case-insensitive). Default to
         "medium" if it's anything else.
       - tags: a SET of lowercased tags built from *tags (duplicates disappear by themselves)
       - Reject an empty title: return None and don't add anything.

4. find_task(tasks, task_id) -> dict | None
       Loop through and return the matching task, or None.

5. mark_done(tasks, task_id) -> bool
       True if it worked, False if the id doesn't exist OR the task was already done.
       Reuse find_task.

6. delete_task(tasks, task_id) -> bool
       Remove the task. Return True or False. Reuse find_task.

7. stats(tasks) -> dict
       Return (don't print):
           {"total": 5, "done": 2, "pending": 3, "percent_done": 40.0,
            "by_priority": {"high": 1, "medium": 3, "low": 1},
            "all_tags": {"home", "study", "errands"}}
       percent_done is rounded to 1 decimal place. It must not crash when tasks is empty.

11. main() -> None
       The loop: show menu, read choice, ask for any extra input, call the right
       function, print a friendly result. Choice 7 breaks out with "Bye!".
       For "Add task": ask for title, priority, and tags as comma-separated text,
       then pass the tags in with * unpacking:  add_task(tasks, title, prio, *tag_list)

-------------------------------------------------------------------------------
ACCEPTANCE CHECKS: all of these must pass
-------------------------------------------------------------------------------
Uncomment the self_test() call at the bottom. Every assert must pass before
you run main(). This is your first taste of testing (pytest comes later in
Phase 1).

-------------------------------------------------------------------------------
STRETCH (optional, once everything passes)
-------------------------------------------------------------------------------
a) "Edit task": change the title or priority of an existing task.
b) "Undo last delete": keep deleted tasks in a list used as a stack.
c) In view, show due-soon tasks first: add an optional "due" field as a
   (year, month, day) TUPLE. Tuples compare element by element, so you can
   compare dates with < directly. Work out why that works.

-------------------------------------------------------------------------------
WHEN YOU'RE DONE
-------------------------------------------------------------------------------
Paste the file back to me for review. I'll grade it on correctness, edge cases,
naming, whether each function does one job, and idiomatic Python, compared with
how you'd write it in TS.
"""


# ---------------------------------------------------------------------------
# Your code goes below. Delete each `pass` as you implement the function.
# ---------------------------------------------------------------------------

def show_menu():
    i = 0
    while i <= 7 :
        match i :
            case 1:
                print(f"{i} Add task")
            case 2:
                print(f"{i} View tasks")
            case 3:
                print(f"{i} Mark task done")
            case 4:
                print(f"{i} Delete task")
            case 5:
                print(f"{i} Search")
            case 6:
                print(f"{i} Stats")
            case 7:
                print(f"{i} Quit")



def read_choice():
    while True:
        user_input = input("Enter a number from 1 to 7")
        user_input = user_input.strip()
        if user_input.isdigit() : 
            return int(user_input)
        continue
    


def add_task(tasks, title, priority, *tags):
    max_id = -1
    new_title = title.split()
    new_title="".join(new_title).capitalize()
    for k,v in tasks: 
        if tasks[k].id > max_id:
            max_id = v
    if not len(new_title): 
        return None
    if priority.lower() not in ["high", "low", "medium"]: 
        priority = "medium"
    done =  False
    task = {}
    task["id"]= 1+max_id,
    task["title"] =new_title,
    task["priority"]=priority.lower(),
    task["done"]=done,
    task["tags"] = tags
    tag_set = set()
    for t in tags:         
        tag_set.add(t.lower())
    task[tags] = tag_set
    tasks.append(task)
    return task

def find_task(tasks, task_id):
    for v in tasks:
        if v["id"] == task_id: 
            return v
    return None


def mark_done(tasks, task_id):
    task = find_task(tasks, task_id)
    if  task == None or task["done"] == True:
         return False
    else :
        task["done"] = True
    return True


def delete_task(tasks, task_id):
     task = find_task(tasks, task_id)
     if task == None:
            return False
     tasks.remove(task)
     return True

def stats(tasks):
    priority = {
        "high": 0, "medium": 0, "low": 0
    }
    tags = set()
    totalTask = 0
    totalTaskDone = 0

    for task in tasks:
        totalTask += 1
        if task["done"] == True:
            totalTaskDone += 1
        priority[task["priority"]] = ( priority.get(task["priority"]) or 0 ) + 1
        tags.update(task["tags"])

    return {
        "total": totalTask,
        "done": totalTaskDone,
        "pending": totalTask - totalTaskDone,
        "percent_done":  round((totalTaskDone / totalTask) * 100, 1) if totalTask > 0 else 0,
        "by_priority": priority,
        "all_tags": tags
    }


def main():
    pass


# ---------------------------------------------------------------------------
# Self-test: don't edit this. Make it pass.
# ---------------------------------------------------------------------------

def self_test():
    t = []

    a = add_task(t, "  buy   milk ", "HIGH", "Home", "errands", "home")
    assert a["id"] == 1
    assert a["title"] == "Buy milk"
    assert a["priority"] == "high"
    assert a["tags"] == {"home", "errands"}
    assert a["done"] is False

    b = add_task(t, "finish loops video", "urgent")       # invalid -> medium
    assert b["priority"] == "medium"
    assert b["tags"] == set()

    assert add_task(t, "    ", "low") is None             # empty title rejected
    assert len(t) == 2

    c = add_task(t, "call mom", "low", "family")
    assert delete_task(t, 2) is True
    assert delete_task(t, 2) is False                     # already gone
    d = add_task(t, "read docs", "low")
    assert d["id"] == 4                                   # not len(t)+1 !

    assert mark_done(t, 1) is True
    assert mark_done(t, 1) is False                       # already done
    assert mark_done(t, 99) is False

    assert format_task(a).startswith("[x]")
    assert "#errands #home" in format_task(a)

    assert [x["id"] for x in search(t, "MILK")] == [1]
    assert [x["id"] for x in search(t, "family")] == [3]
    assert search(t, "nothing") == []

    s = stats(t)
    assert s["total"] == 3 and s["done"] == 1 and s["pending"] == 2
    assert s["percent_done"] == 33.3
    assert s["by_priority"] == {"high": 1, "medium": 0, "low": 2}
    assert s["all_tags"] == {"home", "errands", "family"}

    assert stats([])["percent_done"] == 0.0               # no ZeroDivisionError

    print("All checks passed. Now run main().")


# self_test()
# main()
