# Expense Tracker – Personal Expense Management System

**Expense Tracker** is a backend application developed using Python, Django, and Django REST Framework (DRF) to manage personal expenses and analyze spending patterns.

The application provides RESTful APIs for expense management, user-specific expense access, spending summaries, and AI-powered budgeting recommendations through the Google Gemini API.

It combines backend API development, database aggregation, authentication, custom permissions, and external AI API integration.

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Application Architecture](#application-architecture)
- [Core Functionalities](#core-functionalities)
- [Expense Management Workflow](#expense-management-workflow)
- [Authentication and Permissions](#authentication-and-permissions)
- [AI Integration](#ai-integration)
- [Database Operations](#database-operations)
- [Installation and Setup](#installation-and-setup)
- [Running the Application](#running-the-application)
- [Future Improvements](#future-improvements)

## Project Overview

Expense Tracker is designed to help users record and manage their personal expenses while understanding their spending habits.

Users can create, retrieve, update, and delete expense records. The application also provides spending summaries using Django ORM aggregation and integrates Google Gemini API to generate personalized monthly budget plans and savings recommendations.

The project focuses on backend development using Django REST Framework, with an emphasis on authentication, data ownership, database operations, and third-party API integration.

## Key Features

### 1. Expense Management

- Create new expense records.
- Retrieve expense information.
- Update existing expense records.
- Delete expense records.
- Maintain user-specific expense data.

### 2. User Authentication

- Token-based authentication using Django REST Framework.
- Authentication for protected API operations.
- Access to expense records based on the authenticated user.

### 3. Custom Permissions

- Custom object-level permission handling.
- Expense ownership validation.
- Restrict access to records belonging to other users.

### 4. Expense Analytics

- Calculate daily expense totals.
- Generate monthly expense summaries.
- Analyze spending by category.
- Use Django ORM aggregation for database-level calculations.

### 5. AI-Powered Budget Recommendations

- Integration with Google Gemini API.
- Generate personalized monthly budget plans.
- Provide savings recommendations.
- Analyze spending information to support budgeting decisions.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Backend framework |
| Django REST Framework | REST API development |
| Django ORM | Database queries and aggregation |
| Database configured in project | Expense data storage |
| DRF Token Authentication | User authentication |
| Google Gemini API | AI-powered recommendations |
| Git and GitHub | Version control |

## Application Architecture

The application follows a Django REST Framework-based backend architecture.

The main components include:

**Models**
- Define expense-related database structures.
- Maintain relationships between users and expenses.
- Store expense information.

**Serializers**
- Convert model instances into API responses.
- Validate incoming API data.
- Handle serialization and deserialization.

**Views**
- Process incoming API requests.
- Perform expense CRUD operations.
- Generate expense summaries.
- Handle AI recommendation requests.

**Permissions**
- Control access to expense records.
- Validate ownership before allowing protected operations.

**Django ORM**
- Perform database queries.
- Aggregate daily and monthly expense totals.
- Generate category-wise spending summaries.

## Core Functionalities

### 1. CRUD Operations

The application implements the four fundamental CRUD operations:

| Operation | Description |
|---|---|
| Create | Add a new expense |
| Read | Retrieve expense records |
| Update | Modify existing expenses |
| Delete | Remove expense records |

These operations are implemented through Django REST Framework APIs.

### 2. User-Specific Expense Management

Expense records are associated with users.

The application retrieves expense information based on the authenticated user, helping maintain separation between individual users' data.

### 3. Expense Aggregation

The application uses Django ORM aggregation to calculate:

- Daily spending totals.
- Monthly spending totals.
- Category-wise expense summaries.

Using database-level aggregation helps generate summaries without manually processing every expense record in Python.

### 4. AI-Based Budget Planning

The Google Gemini API is integrated to provide additional budgeting functionality.

The application can use expense-related information to generate:

- Personalized monthly budget plans.
- Savings recommendations.
- Budgeting suggestions based on spending patterns.

## Expense Management Workflow

1. A user authenticates using token-based authentication.
2. The user creates expense records through the API.
3. Expense information is validated and stored in the database.
4. The user retrieves their expense records.
5. Custom permissions help restrict access to records based on ownership.
6. Django ORM aggregation generates spending summaries.
7. The Google Gemini API is used to generate personalized budget recommendations.

## Authentication and Permissions

### Token Authentication

The application uses Django REST Framework token authentication to identify authenticated users accessing protected APIs.

### Object-Level Permissions

Custom permissions are implemented to control access to individual expense records.

The ownership checks help ensure that users can access and manage only the expense records they are authorized to use.

## AI Integration

The project integrates the Google Gemini API to provide AI-assisted financial recommendations.

The integration extends the basic expense management functionality by generating personalized budgeting suggestions.

The AI functionality focuses on:

- Monthly budget planning.
- Savings recommendations.
- Spending-related suggestions.

An API key is required to use the Gemini integration. Keep the key private and configure it through the application's expected configuration mechanism.

## Database Operations

Django ORM is used for database interaction.

The application uses ORM aggregation to calculate expense summaries, including:

- Daily expense totals.
- Monthly expense totals.
- Category-wise spending.

This keeps database operations integrated with Django's model and query system.

## Installation and Setup

### Prerequisites

Install the following:

- Python
- pip
- Git
- Database configured for the project

### 1. Clone the Repository

```bash
git clone https://github.com/aravindbalaji4851-cmd/Expense_Tracker.git
```

### 2. Navigate to the Project Directory

```bash
cd Expense_Tracker
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Database Settings

Review the Django database configuration and make sure the required database is available.

Update the database credentials if necessary.

### 7. Configure Google Gemini API

Obtain a Google Gemini API key and configure it using the method expected by the application.

Never upload API keys or other sensitive credentials to GitHub.

### 8. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 9. Create a Superuser

```bash
python manage.py createsuperuser
```

### 10. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at:

`http://127.0.0.1:8000/`

## Future Improvements

- Add advanced expense filtering and search.
- Introduce monthly budget limits.
- Add expense visualization and graphical reports.
- Improve API documentation.
- Add automated tests for authentication and permissions.
- Improve AI recommendation handling and validation.

## Author

**Aravind Balaji K J**

[GitHub Profile](https://github.com/aravindbalaji4851-cmd)

[Project Repository](https://github.com/aravindbalaji4851-cmd/Expense_Tracker)
