
from datetime import date

def calculate_task_score(t):
    due = t['due_date']
    if isinstance(due, str):
        from datetime import date as d
        due = d.fromisoformat(due)

    today = date.today()
    diff = (due - today).days
    score = 0

    if diff < 0: score += 200
    elif diff == 0: score += 120
    elif diff <= 3: score += 80
    elif diff <= 7: score += 40
    else: score += 10

    score += t.get('importance', 5) * 10

    if t.get('estimated_hours',1) <= 1: score += 15

    score -= 5 * len(t.get('dependencies', []))

    return max(0, score)
