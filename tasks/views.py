
import json
from datetime import date
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .scoring import calculate_task_score

def generate_explanation(task):
    score = task['score']
    due = task['due_date']
    if isinstance(due, str):
        from datetime import date as d
        due = d.fromisoformat(due)
    today = date.today()
    diff = (due - today).days
    explanation = f"Score {score}: "
    if diff < 0:
        explanation += "Overdue task (+200). "
    elif diff == 0:
        explanation += "Due today (+120). "
    elif diff <= 3:
        explanation += "Due soon (+80). "
    elif diff <= 7:
        explanation += "Due this week (+40). "
    else:
        explanation += "Due later (+10). "
    explanation += f"Importance {task.get('importance',5)} (+{task.get('importance',5)*10}). "
    if task.get('estimated_hours',1) <= 1:
        explanation += "Quick task (+15). "
    deps = len(task.get('dependencies', []))
    if deps > 0:
        explanation += f"Has {deps} dependencies (-{5*deps})."
    return explanation

@csrf_exempt
def analyze(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST required")

    payload = json.loads(request.body)
    strategy = payload.get('strategy', 'default')
    data = payload.get('tasks', [])

    for t in data:
        if isinstance(t['due_date'], date):
            t['due_date'] = t['due_date'].isoformat()
        t['score'] = calculate_task_score(t)

    if strategy == 'priority':
        sorted_data = sorted(data, key=lambda x: x.get('importance', 0), reverse=True)
    elif strategy == 'due_date':
        sorted_data = sorted(data, key=lambda x: x['due_date'])
    else:  # default
        sorted_data = sorted(data, key=lambda x: x['score'], reverse=True)

    return JsonResponse(sorted_data, safe=False)

@csrf_exempt
def suggest(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST required")

    payload = json.loads(request.body)
    strategy = payload.get('strategy', 'default')
    data = payload.get('tasks', [])

    for t in data:
        if isinstance(t['due_date'], date):
            t['due_date'] = t['due_date'].isoformat()
        t['score'] = calculate_task_score(t)
        t['explain'] = generate_explanation(t)

    if strategy == 'priority':
        sorted_data = sorted(data, key=lambda x: x.get('importance', 0), reverse=True)
    elif strategy == 'due_date':
        sorted_data = sorted(data, key=lambda x: x['due_date'])
    else:  # default
        sorted_data = sorted(data, key=lambda x: x['score'], reverse=True)

    return JsonResponse(sorted_data[:3], safe=False)
