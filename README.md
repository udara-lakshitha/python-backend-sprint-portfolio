# Professional Backend Developer Portfolio

Welcome to my portfolio, built during an intensive, accelerated sprint. This repository is a demonstration of my ability to architect, build, and containerize a modern, database-driven web application from the ground up.

## 🌟 Lighthouse Project: User & Post Management API

This is a complete, production-ready REST API built with FastAPI and backed by a PostgreSQL database. It showcases a full understanding of the modern backend development lifecycle, from database schema design to a containerized, multi-service architecture.

**➡️ Click here to view the project's detailed README, code, and architecture.**](./05-user-post-api/)

### Key Features & Skills Demonstrated:

- **Robust API Design:** Built with **FastAPI** and **Pydantic** for clear data validation and automatic, interactive documentation.
- **Database Architecture:** Designed a relational schema with **PostgreSQL** and managed it with **SQLModel**, implementing foreign key relationships for data integrity.
- **Containerization:** The entire application stack (API + Database) is fully containerized using **Docker** and orchestrated for local development with **Docker Compose**.
- **Resilient Startup:** Implemented a **Python-based database waiter script** and a shell **entrypoint** to handle container race conditions, ensuring the API only starts after the database is ready.
- **Professional Workflow:** Managed with **Git** for version control, with clear, conventional commit messages.

### Local Setup & Launch

This project is designed to be run locally with one simple command, demonstrating a professional development setup. **Docker Desktop is required.**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/python-backend-sprint-portfolio.git
    cd python-backend-sprint-portfolio
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd 05-user-post-api
    ```

3.  **Launch the application stack:**
    This single command builds the API image, starts the database, waits for the database to be healthy, and then starts the API.
    ```bash
    docker-compose up --build
    ```

4.  **Access the local API:**
    The API will be available at `http://localhost:8000`, with interactive documentation at `http://localhost:8000/docs`.

---

## 🧠 Foundational Skills & Drills

This portfolio also includes the foundational work completed during the sprint, proving core competencies.

- **[Data Structures & Algorithms](./04-dsa-essentials/):** A log of solved classic DSA problems (Two Sum, Valid Anagram, etc.), demonstrating readiness for technical interviews.
- **[Data Analysis with Pandas](./02-data-analysis-basics/):** A script showcasing data manipulation and analysis skills.
- **[Python Fundamentals CLI](./01-password-generator-cli/):** A command-line tool built to solidify core Python concepts.

---

## Core Competencies

- **Languages:** Python
- **Frameworks:** FastAPI
- **Databases:** PostgreSQL, SQL
- **DevOps & Containerization:** Docker, Docker Compose
- **Libraries:** Pandas, NumPy, SQLModel, Pydantic
- **CS Fundamentals:** Data Structures, Algorithms, OOP Principles
