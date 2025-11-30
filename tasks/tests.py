
from datetime import date, timedelta
from .scoring import calculate_task_score

def test():
    t1 = {'due_date': (date.today() - timedelta(days=1)).isoformat(), 'importance': 10, 'estimated_hours':1, 'dependencies':[]}
    t2 = {'due_date': (date.today() + timedelta(days=10)).isoformat(), 'importance': 1, 'estimated_hours':5, 'dependencies':[1,2]}
    assert calculate_task_score(t1) > calculate_task_score(t2)

if __name__ == "__main__":
    test()
    print("OK")
