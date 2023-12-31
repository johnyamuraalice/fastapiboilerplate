# FastAPI Boilerplate

## Introduction

This repository is a boilerplate for web application development using FastAPI. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.6 or higher.
- You have installed pip, Python's package manager.

### Installation

1. Clone the repository:

   ```bash
   git clone <repository URL>
   ```

2. Navigate to the project directory:

   ```bash
   cd <project name>
   ```

3. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install all necessary dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

You can run the application locally with Uvicorn, simply execute:

```bash
uvicorn main:app --reload
```

## Development

After making changes, if you want to push them to the main repository, do the following:

```bash
    git add .
    git commit -m "Describe your changes here"
    git push
```

##Visual Studio Code Settings

To configure Visual Studio Code for Python development, add the following settings to your workspace settings file (.vscode/settings.json):

```json
{
  "[python]": {
    "editor.defaultFormatter": "ms-python.autopep8"
  },
  "python.formatting.provider": "autopep8"
}
```

These settings configure the default Python formatter to be autopep8, and it sets it as the default formatter for Python files.

### Docker

To run the application using Docker, follow these steps:

1. Build the Docker image:

   ```bash
   docker build -t myapp .
   ```

2. Run the Docker container:

   ```bash
   docker run -d -p 8000:8000 myapp
   ```

The application will be accessible at http://localhost:8000.
