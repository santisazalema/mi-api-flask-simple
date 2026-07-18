# Task API with Flask

Simple REST API built with Flask to manage tasks. This project demonstrates backend development concepts such as routing, JSON responses, request validation, database persistence, and CRUD operations.

## Features

- Get all tasks
- Get one task by ID
- Create a new task
- Update an existing task
- Delete a task
- JSON request and response handling
- Basic input validation
- SQLite database integration with SQLAlchemy
- Automated tests with pytest

## Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- pytest

## Project Structure

```bash
mi-api-flask-simple/
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── tests/
│   └── test_tasks.py
├── .env.example
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/santisazalema/mi-api-flask-simple.git
cd mi-api-flask-simple
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file based on `.env.example`.

Example:

```env
DATABASE_URL=sqlite:///tasks.db
FLASK_ENV=development
```

## Run the project

```bash
python run.py
```

The API will run locally at:

```text
http://127.0.0.1:5000
```

## Run tests

```bash
python -m pytest
```

## Endpoints

### Get all tasks

```http
GET /tareas
```

Example:

```bash
curl http://127.0.0.1:5000/tareas
```

### Get one task

```http
GET /tareas/<id>
```

Example:

```bash
curl http://127.0.0.1:5000/tareas/1
```

### Create a new task

```http
POST /tareas
```

Example:

```bash
curl -X POST http://127.0.0.1:5000/tareas \
-H "Content-Type: application/json" \
-d '{"titulo":"Practicar APIs REST"}'
```

### Update a task

```http
PUT /tareas/<id>
```

Example:

```bash
curl -X PUT http://127.0.0.1:5000/tareas/1 \
-H "Content-Type: application/json" \
-d '{"titulo":"Practicar Flask API","completada":true}'
```

### Delete a task

```http
DELETE /tareas/<id>
```

Example:

```bash
curl -X DELETE http://127.0.0.1:5000/tareas/1
```

## Example Response

```json
{
  "id": 1,
  "titulo": "Aprender Flask",
  "completada": false
}
```

## Current Limitations

- No authentication
- Basic validation only
- No pagination or filtering

## Planned Improvements

- Add Swagger or API documentation
- Add better validation
- Add authentication
- Add deployment configuration

## Author

**Santiago I**  
Junior Software Developer focused on backend, APIs, Python, and web development.

GitHub: https://github.com/santisazalema

## License

This project is licensed under the MIT License.
