import argparse
import pickle
import os

tasks_list = []

def add_task(task):
    # TODO Essa funçaõ deve adicionar uma nova tarefa na variável tasks_list.
    print("not implemented")

def list_tasks():
    # TODO Essa funçaõ deve listar todas as tarefas que estão salvas na variável tasks_list.
    print("not implemented")

def load_tasks():
    global tasks_list
    if os.path.exists('./data/tasks.pkl'):
        with open('./data/tasks.pkl', 'rb') as f:
            tasks_list = pickle.load(f)            

def save_tasks():
    if not os.path.exists('./data'):
        os.makedirs('./data')
    with open('./data/tasks.pkl', 'wb') as f:
        pickle.dump(tasks_list, f)

def main():
    parser = argparse.ArgumentParser(description="Simple TODO CLI")
    parser.add_argument('-a', '--add', type=str, help="Add a new task")
    parser.add_argument('-l', '--list', action='store_true', help="List all tasks")

    args = parser.parse_args()

    load_tasks()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    else:
        parser.print_help()
    
    save_tasks()

if __name__ == "__main__":
    main()