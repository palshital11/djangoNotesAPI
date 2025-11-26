# djangoNotesAPI

A simple and clean **Notes CRUD REST API** built using Django and Django REST Framework.  
Users can register, log in, and manage personal notes securely(CRUD). This project helped me learn DRF fundamentals, Token Authentication, and how to build a complete CRUD API with Django.

---

## Features
### User Authentication
- User Registration (returns auth token)
- User Login (returns auth token)
- Token-based protected endpoints
- Notes accessible only by the authenticated user

### Notes CRUD (Authenticated)
- Create Notes
- List all Notes
- View a Single Note
- Update Notes
- Delete Notes

---

## Tech Stack
- Python 3
- Django 5
- Django REST Framework
- Token Authentication
- SQLite
- Postman (API testing)

## Project Structure
```
djangoNotesAPI/
│
├── notes/              # Notes App (CRUD)
├── users/              # User Auth App (Register/Login)
├── notes_api/          # Django Project Settings
│
├── screenshots/        # API testing screenshots
├── postman/            # Postman collection JSON
│
├── manage.py
├── requirements.txt
└── README.md
```

## API Endpoints

### Authentication
| Method | Endpoint          | Description                     |
| ------ | ----------------- | ------------------------------- |
| POST   | `/auth/register/` | Register new user and get token |
| POST   | `/auth/login/`    | Log in and get token            |

### Notes (Require Token)
#### Header required:
#### Authorization: Token <your_token>
| Method | Endpoint       | Description     |
| ------ | -------------- | --------------- |
| GET    | `/notes/`      | List all notes  |
| POST   | `/notes/`      | Create new note |
| GET    | `/notes/<id>/` | Retrieve a note |
| PUT    | `/notes/<id>/` | Update a note   |
| DELETE | `/notes/<id>/` | Delete a note   |

## Screenshots
All API testing screenshots are included in screenshots folder

## Postman Collection
Import the collection from postman/Notes_API.postman_collection.json .
It Contains all API endpoints for quick testing.
