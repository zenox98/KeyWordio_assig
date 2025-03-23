# KeyWordio Assignment

This project is a full-stack web application built with Django (REST Framework) for the backend and React.js with React Router for the frontend.  It allows users to save search the keyword and after search save it.

## Table of Contents

1.  [Project Overview](#project-overview)
2.  [Project Structure](#project-structure)
3.  [Prerequisites](#prerequisites)
4.  [Backend Setup (Django)](#backend-setup-django)
    *   [Installation](#backend-installation)
    *   [Environment Variables](#backend-environment-variables)
    *   [Database Setup](#backend-database-setup)
    *   [Running the Backend](#running-the-backend)
5.  [Frontend Setup (React)](#frontend-setup-react)
    *   [Installation](#frontend-installation)
    *   [Environment Variables (Optional)](#frontend-environment-variables-optional)
    *   [Running the Frontend](#running-the-frontend)
6.  [API Endpoints](#api-endpoints)
7.  [Testing](#testing)
8.  [Contributing](#contributing)
9.  [License](#license)

## 1. Project Overview

The project allow user to search keyword in the web and save in the database for further analysis.

## 2. Project Structure

The project is divided into two main parts: the backend (Django) and the frontend (React).

*   **`backend/`**:  Contains the Django REST Framework API.
    *   **`keywordio/`**:  The main Django application where you define models, views, serializers, and URLs for your API.
    *   **`keywordio_project/`**:  The Django project's settings, including database configuration, installed apps, middleware, and URL routing.
    *   **`manage.py`**:  The command-line utility for Django tasks (migrations, running the server, etc.).
*   **`frontend/`**: Contains the React.js application.
    *   **`src/`**:  The main source code for your React application.
        *   **`components/`**:  Reusable React components.
        *   **`App.js`**:  The main application component, likely handling routing.
        *   **`index.js`**:  The entry point for your React application.
    *   **`public/`**:  Static assets (like `index.html`).
    *   **`package.json`**:  Defines project dependencies and scripts.

## 3. Prerequisites

Before you begin, make sure you have the following installed:

*   **Python (>= 3.8 recommended)**:  [https://www.python.org/downloads/](https://www.python.org/downloads/)
*   **pip (Python package installer)**:  Usually comes with Python.
*   **Node.js (>= 14 recommended)**:  [https://nodejs.org/](https://nodejs.org/)
*   **npm (Node Package Manager) or yarn**: npm comes with Node.js.  Yarn is an alternative: [https://yarnpkg.com/](https://yarnpkg.com/)
*   **A code editor (VS Code, Sublime Text, etc.)**
* **Git** : [https://git-scm.com/downloads](https://git-scm.com/downloads)

## 4. Backend Setup (Django)

### 4.1 Backend Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/zenox98/KeyWordio_assig.git
    cd KeyWordio_assig/backend
    ```

2.  **Create a virtual environment (highly recommended):**

    ```bash
    python3 -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **On Windows:**

        ```bash
        venv\Scripts\activate
        ```

    *   **On macOS and Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### 4.2 Backend Environment Variables

*   There is no env file.

### 4.3 Backend Database Setup

1.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```
    This creates the necessary database tables based on your Django models.  By default, Django uses SQLite, which doesn't require any external database server.

### 4.4 Running the Backend

1.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```

    The backend will be accessible at `http://127.0.0.1:8000/`.

## 5. Frontend Setup (React)

### 5.1 Frontend Installation

1. **Navigate to the frontend directory:**

    ```bash
    cd ../frontend  # From the backend directory
    ```

2. **Install dependencies:**

    ```bash
    npm install
    # OR
    yarn install
    ```

### 5.2 Frontend Environment Variables (Optional)

* There is no env file. If you add any environment variables in the future (e.g., for API base URLs), create a `.env` file in the `frontend` directory and document them here.

### 5.3 Running the Frontend

1.  **Start the development server:**

    ```bash
    npm start
    # OR
    yarn start
    ```

    The frontend will be accessible at `http://localhost:3000/` (or a different port if 3000 is in use).  The React development server will automatically reload the page when you make changes to the code.

## 6. API Endpoints

Here are the main API endpoints provided by the Django backend:

*   **`GET /api/keywords/`**:  Retrieves a list of all saved keywords.
*   **`POST /api/keywords/`**:  Creates a new keyword entry.  Expects a JSON payload:

    ```json
    {
        "keyword": "your keyword here"
    }
    ```

* **`GET /search/?q=<keyword>`**: Search the Keyword in Google.

You can access these endpoints using tools like `curl`, Postman, or directly from your React application.  The frontend likely uses `fetch` or a library like `axios` to make these API calls.

## 7. Testing

* **Backend (Django):**

    ```bash
     cd backend
     python manage.py test
    ```
