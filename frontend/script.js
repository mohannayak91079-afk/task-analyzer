
function extractJSON(input) {
  // Find the first '[' and last ']'
  let start = input.indexOf('[');
  let end = input.lastIndexOf(']');
  if (start === -1 || end === -1 || start > end) {
    throw new Error('No valid JSON array found in input');
  }
  return input.substring(start, end + 1);
}

async function analyze(){
  try {
    let input = document.getElementById('taskInput').value;
    let jsonString = extractJSON(input);
    let t = JSON.parse(jsonString);
    let strategy = document.getElementById('strategySelect').value;
    let payload = { tasks: t, strategy: strategy };
    let r = await fetch('/api/tasks/analyze/', {
        method:'POST', headers:{'Content-Type':'application/json'},
        body: JSON.stringify(payload)
    });
    if (!r.ok) {
      document.getElementById('results').innerHTML = `<p>Error: ${r.status} ${r.statusText}</p>`;
      return;
    }
    let data = await r.json();
    let html = data.map(task => {
      let priority = task.score > 150 ? 'high' : task.score > 80 ? 'medium' : 'low';
      return `<div class="task-item ${priority}">
        <h3>${task.title}</h3>
        <p>Due Date: ${task.due_date}</p>
        <p>Importance: ${task.importance}</p>
        <p>Effort: ${task.estimated_hours} hours</p>
        <p>Score: ${task.score}</p>
        <p>Explanation: ${task.explain}</p>
      </div>`;
    }).join('');
    document.getElementById('results').innerHTML = html;
  } catch (e) {
    document.getElementById('results').innerHTML = `<p>Error: ${e.message}</p>`;
  }
}
async function suggest(){
  try {
    let input = document.getElementById('taskInput').value;
    let jsonString = extractJSON(input);
    let t = JSON.parse(jsonString);
    let strategy = document.getElementById('strategySelect').value;
    let payload = { tasks: t, strategy: strategy };
    let r = await fetch('/api/tasks/suggest/', {
        method:'POST', headers:{'Content-Type':'application/json'},
        body: JSON.stringify(payload)
    });
    if (!r.ok) {
      document.getElementById('results').innerText = `Error: ${r.status} ${r.statusText}`;
      return;
    }
    let data = await r.json();
    let formatted = data.map(task => `Task: ${task.title}\nImportance: ${task.importance}\nDue Date: ${task.due_date}\nScore: ${task.score}\nExplain: ${task.explain}\n`).join('\n---\n');
    document.getElementById('results').innerText = formatted;
  } catch (e) {
    document.getElementById('results').innerText = `Error: ${e.message}`;
  }
}
