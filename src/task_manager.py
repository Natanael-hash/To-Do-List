import json


class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task_name):
        if not task_name.strip():
            raise ValueError("Numele sarcinii nu poate fi gol!")

        new_id = self.tasks[-1]['id'] + 1 if self.tasks else 1
        self.tasks.append({
            'id': new_id,
            'sarcina': task_name
        })
        self.save_tasks()
        return new_id

    def delete_task(self, task_id):
        for index, task in enumerate(self.tasks):
            if task['id'] == task_id:
                del self.tasks[index]
                self.save_tasks()
                return True
        return False

    @property
    def all_tasks(self):
        return self.tasks.copy()