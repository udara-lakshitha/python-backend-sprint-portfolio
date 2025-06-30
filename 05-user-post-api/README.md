# Lighthouse Project: User & Post Management API

This project is a complete, containerized REST API for managing users and their posts, built with a modern Python backend stack. It serves as a comprehensive demonstration of professional backend development practices, from database schema design to a robust, multi-container local development environment.

The entire application is orchestrated with **Docker Compose**, allowing for a one-command startup of both the API service and the PostgreSQL database.

---

## Core Technologies

| Category      | Technology / Library | Purpose                                                 |
|---------------|----------------------|---------------------------------------------------------|
| **Backend**   | FastAPI              | High-performance, modern web framework for building APIs. |
| **Database**  | PostgreSQL           | Powerful, open-source object-relational database system.|
| **ORM**       | SQLModel             | Pythonic, type-safe library for database interaction.     |
| **Validation**| Pydantic             | Data validation and settings management using type hints. |
| **Container** | Docker & Docker Compose | For creating a consistent, portable development environment. |

---

## Architectural Highlights & Key Features

### Robust Database Design
- **Relational Schema:** Implemented a one-to-many relationship between `Users` and `Posts`.
- **Data Integrity:** Utilizes `FOREIGN KEY` constraints to ensure a post cannot exist without a valid author, preventing orphan records.
- **Efficient Queries:** Usernames are indexed for fast lookups.

### Professional API Structure
- **CRUD Operations:** Provides full Create and Read functionality for both users and posts.
- **Nested Serialization:** Endpoints can return nested data (e.g., a user with a list of their posts, or a post with the author's details), demonstrating advanced data shaping.
- **Error Handling:** Implemented graceful error handling with `HTTPException` to return meaningful status codes (e.g., `404 Not Found`) for invalid requests.
- **Automatic Docs:** Leverages FastAPI's automatic generation of interactive Swagger UI documentation at the `/docs` endpoint.

### Resilient Startup Sequence
- **Container Race Condition Solved:** A custom Python script (`wait_for_db.py`) and a shell `entrypoint.sh` ensure the API container only starts after the PostgreSQL database is fully initialized and ready to accept connections. This is handled locally via a `healthcheck` in `docker-compose.yml`.

---

## Local Development Setup

**Prerequisites:** Docker and Docker Compose must be installed.

1.  **Clone the Main Portfolio Repository:**
    ```bash
    git clone https://github.com/your-username/python-backend-sprint-portfolio.git
    cd python-backend-sprint-portfolio
    ```

2.  **Navigate to this Project's Directory:**
    ```bash
    cd 05-user-post-api
    ```

3.  **Launch the Application Stack:**
    This single command reads the `docker-compose.yml` file, builds the `api` image from the `Dockerfile`, starts the `db` container, waits for it to be healthy, and then starts the `api` container.
    ```bash
    docker-compose up --build
    ```

4.  **Access the API:**
    - The API will be running at `http://localhost:8000`.
    - The interactive documentation is available at **`http://localhost:8000/docs`**.

    You can use the `/docs` interface to create users, create posts linked to those users, and retrieve the data.
