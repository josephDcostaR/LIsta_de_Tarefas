
class Task:
    
    def __init__(self, title, description, creation_date, status, priority, due_date=None):
        
        self.title = title
        self.description = description
        self.creation_date = creation_date
        self.status = status
        self.priority = priority
        self.due_date = due_date
        
    def formatted_due_date(self):
        if self.due_date:
            # Suponha que self.due_date seja uma string no formato "YYYY-MM-DD"
            parts = self.due_date.split('-')
            if len(parts) == 3:
                day, month, year = map(int, parts)
                return f"{day:02d}/{month:02d}/{year}"
        return ""
    
    
    def set_due_date(self, due_date):
        self.due_date = due_date
        
class TaskModel:
    
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description, creation_date, status, priority, due_date=None):
        task = Task(title, description, creation_date, status, priority, due_date)
        self.tasks.append(task)

    def read_tasks(self):
        return self.tasks

    def update_task(self, index, title, description, status, priority, due_date=None):
        if index >= 0 and index < len(self.tasks):
            self.tasks[index].title = title
            self.tasks[index].description = description
            self.tasks[index].status = status
            self.tasks[index].priority = priority
            if due_date is not None:
                self.tasks[index].set_due_date(due_date)
                
    def delete_task(self, index):
        if index >= 0 and index < len(self.tasks):
            del self.tasks[index]

        
    
 