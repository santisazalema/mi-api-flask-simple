# Task API with Flask

Simple REST API built with Flask to manage tasks. This project demonstrates basic backend development concepts such as routing, JSON responses, request validation, and CRUD-style API design.

## Features

- Get all tasks
- Create a new task
- JSON request and response handling
- Basic input validation
- Lightweight and easy to run locally

## Tech Stack

- Python 3
- Flask

## Project Structure

```bash
mi-api-flask-simple/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/santisazalema/mi-api-flask-simple.git
cd mi-api-flask-simple
```

2. Create and activate a virtual environment:

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

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the project

```bash
python app.py
```

The API will run locally at:

```bash
http://127.0.0.1:5000
```

## Endpoints

### Get all tasks

**GET** `/tareas`

Example:

```bash
curl http://127.0.0.1:5000/tareas
```

Response:

```json
{
  "tareas": [
    {
      "id": 1,
      "titulo": "Aprender Flask",
      "completada": false
    },
    {
      "id": 2,
      "titulo": "Subir API a GitHub",
      "completada": false
    }
  ]
}
```

### Create a new task

**POST** `/tareas`

Example:

```bash
curl -X POST http://127.0.0.1:5000/tareas \
-H "Content-Type: application/json" \
-d "{\"titulo\": \"Practicar APIs REST\"}"
```

Response:

```json
{
  "tarea": {
    "id": 3,
    "titulo": "Practicar APIs REST",
    "completada": false
  }
}
```

## Current Limitations

- Data is stored in memory
- No database integration yet
- No authentication
- No automated tests yet

## Planned Improvements

- Add full CRUD support
- Add SQLite or PostgreSQL persistence
- Organize routes into a cleaner structure
- Add tests with pytest
- Add error handling improvements

## Author

**Santiago I**  
Junior Software Developer focused on backend, APIs, Python, and web development.

GitHub: [https://github.com/santisazalema](https://github.com/santisazalema)

## License

This project can be released under the MIT License.
