# Task Analyzer

A web application for analyzing and prioritizing tasks based on various strategies. Built with Django backend and a simple HTML/CSS/JavaScript frontend.

## Features

- **Task Input**: Paste JSON array of tasks with title, due_date, importance, estimated_hours, and dependencies.
- **Analysis Strategies**:
  - **Default**: Sorts tasks based on a calculated score considering due date, importance, and estimated hours.
  - **Priority-based**: Sorts tasks by importance level (highest first).
  - **Due Date-based**: Sorts tasks by due date (earliest first).
- **Analyze**: Returns all tasks sorted according to the selected strategy.
- **Suggest**: Returns top 3 suggested tasks based on the selected strategy.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd task-analyzer
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```
   python manage.py migrate
   ```

4. Start the development server:
   ```
   python manage.py runserver
   ```

5. Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

1. Select an analysis strategy from the dropdown.
2. Paste your tasks in JSON format into the textarea. Example format:
   ```json
   [
     {
       "title": "Complete project report",
       "due_date": "2023-12-15",
       "importance": 8,
       "estimated_hours": 4,
       "dependencies": []
     },
     {
       "title": "Review code",
       "due_date": "2023-12-10",
       "importance": 6,
       "estimated_hours": 2,
       "dependencies": ["Complete project report"]
     }
   ]
   ```
3. Click "Analyze" to see all tasks sorted, or "Suggest" to see top 3 recommendations.
4. View results in the results section.

## API Endpoints

### POST /api/tasks/analyze/
Analyzes and sorts all tasks based on the selected strategy.

**Request Body:**
```json
{
  "tasks": [
    {
      "title": "string",
      "due_date": "YYYY-MM-DD",
      "importance": number,
      "estimated_hours": number,
      "dependencies": []
    }
  ],
  "strategy": "default|priority|due_date"
}
```

**Response:** JSON array of sorted tasks with added "score" field.

### POST /api/tasks/suggest/
Suggests top 3 tasks based on the selected strategy.

**Request Body:** Same as analyze endpoint.

**Response:** JSON array of top 3 sorted tasks with added "score" and "explain" fields.

## Project Structure

```
taskanna/
├── backend/                 # Django project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── tasks/                  # Django app for task management
│   ├── models.py           # Task model
│   ├── views.py            # API views for analyze and suggest
│   ├── scoring.py          # Task scoring logic
│   ├── urls.py             # App URL configuration
│   └── migrations/         # Database migrations
├── frontend/               # Static frontend files
│   ├── index.html          # Main HTML page
│   ├── styles.css          # CSS styles
│   └── script.js           # JavaScript for API calls
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── db.sqlite3              # SQLite database
```

## Technologies Used

- **Backend**: Django 4.2+, Python
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **CORS**: django-cors-headers for cross-origin requests

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request



