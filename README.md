# Job Lander

JobLander is a comprehensive web application designed to help users manage their job search journey effectively. From tracking job applications and managing company contacts to logging interview questions and reviewing insightful statistics, JobLander provides all the tools a user needs to stay organized during their job hunt.

## Table of Contents
- [About JobLander](#about-joblander)
- [Features](#features)
- [API Documentation](#api-documentation)
- [Installation](#installation)
- [Usage](#usage)
- [Frontend Overview](#frontend-overview)
- [Backend Overview](#backend-overview)
- [Contributors](#contributors)
- [License](#license)

## About JobLander
JobLander is built to simplify job application management by allowing users to track applications, manage interview data, keep notes on company contacts, and analyze their job search performance through detailed statistics and visual reports.

## Features
- **User Management**: Users can sign up, update their profiles, and manage personal information.
- **Job Application Tracking**: Users can create, update, and delete job applications, track progress, and manage application history.
- **Company and Employee Management**: Manage companies and contacted employees during the hiring process, including adding and editing company and employee details.
- **Interview Preparation**: Keep track of questions asked during interviews or applications for future reference.
- **Save & Apply Later**: Save and manage applications link and title to apply for later through a todo list.
- **Analytics and Insights**: Generate useful statistics and insights, including overall application progress and job search trends over time.

## API Documentation
For detailed API documentation and usage, please refer to our [API Documentation](#) hosted externally. The API supports the following operations:
- User registration, login, and profile management
- Job application creation, update, and deletion
- Company and employee contact management
- Interview question logging
- Save job opportunities for applying later
- Statistics and insights retrieval for job search performance

## Installation
To run the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/JobLander.git
    ```

2. **Backend Setup (Django)**:
   - Navigate to the backend directory:
     ```bash
     cd workspace
     ```
    - Activate Virtual Environment:
     ```bash
     Scripts/activate
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Navigate to Backend Project Directory:
     ```bash
     cd joblander
     ```
   - Apply migrations:
     ```bash
     python manage.py migrate
     ```
   - Run the backend server:
     ```bash
     python manage.py runserver
     ```

3. **Frontend Setup**:
   - Navigate to the frontend directory:
     ```bash
     cd frontend
     ```
   - Install frontend dependencies:
     ```bash
     npm install
     ```
   - Run the frontend server:
     ```bash
     npm start
     ```

## Usage
Once the servers are running, navigate to [http://localhost:3000](http://localhost:3000) to access the JobLander application. Users can:
- Register or log in
- Add new job applications
- Track the status of their applications
- Review questions asked in interviews
- Save job opportunities in a to-do list for applying later
- Generate reports and statistics for better insights

## Frontend Overview
The frontend of JobLander is built with modern technologies, offering a smooth and intuitive user experience. Key frontend technologies include:
- **React.js**: For building the user interface and handling the overall application flow.
- **Chart.js**: For rendering insightful data visualizations and statistics.

## Backend Overview
The backend of JobLander is built using **Django** and follows a RESTful architecture, ensuring flexibility, scalability, and ease of integration with the frontend.

### Key Technologies:
- **Django**: The primary web framework used to build the backend.
- **Django Rest Framework (DRF)**: Extends Django to provide RESTful APIs.
- **Djoser**: Handles user authentication and authorization, including features like registration, login, password resets, and token-based authentication.
- **MySQL**: The relational database management system (RDBMS) used to store all persistent data.

### Database Schema

The backend of JobLander uses a relational database (MySQL) with the following schema. Below is a description of the key tables and their relationships:

#### **User**
This table comes from the default Django authentication model to store user information.

| Field         | Type    | Description                    |
|---------------|---------|--------------------------------|
| id            | Integer | Primary key                    |
| username      | String  | The user's unique username      |
| email         | String  | The user's email address        |
| password      | String  | Hashed password for authentication |

#### **Company**
This table stores company-related data.

| Field         | Type    | Description                            |
|---------------|---------|----------------------------------------|
| id            | Integer | Primary key                            |
| name          | String  | Name of the company                    |
| location      | String  | Location of the company                |
| careers_link  | URL     | Link to the company's careers page     |
| linkedin_link | URL     | Link to the company's LinkedIn profile |

#### **Employee**
This table stores information about employees that are contacts for the user.

| Field         | Type    | Description                                    |
|---------------|---------|------------------------------------------------|
| id            | Integer | Primary key                                    |
| name          | String  | Employee's name                                |
| linkedin_link | URL     | Link to the employee's LinkedIn profile        |
| email         | String  | Employee's email (optional)                   |
| job_title     | String  | Employee's job title                           |
| contacted     | Enum    | The contact status (e.g., Sent, Accepted, etc.)|
| user_id       | FK      | Foreign key to the `User` table (nullable)     |
| company_id    | FK      | Foreign key to the `Company` table (nullable)  |

#### **Application**
This table manages job application details for each user.

| Field             | Type    | Description                                         |
|-------------------|---------|-----------------------------------------------------|
| id                | Integer | Primary key                                         |
| job_title         | String  | The job title the user applied for                  |
| job_type          | String  | The job type (e.g., full-time, internship)          |
| description       | Text    | Detailed job description                            |
| link              | URL     | Link to the job posting                             |
| submitted_cv      | File    | The CV the user submitted for the job               |
| ats_score         | Integer | Applicant Tracking System (ATS) score               |
| stage             | Enum    | Current stage of the application process            |
| status            | Enum    | Current application status (e.g., Pending, Rejected)|
| submission_date   | Date    | Date of application submission                      |
| user_id           | FK      | Foreign key to the `User` table (nullable)          |
| company_id        | FK      | Foreign key to the `Company` table (nullable)       |
| contacted_employees | M2M   | Many-to-many relationship with the `Employee` table |

#### **Question**
This table stores interview questions and answers related to job applications.

| Field         | Type    | Description                                    |
|---------------|---------|------------------------------------------------|
| id            | Integer | Primary key                                    |
| question      | Text    | Interview question asked during the application|
| answer        | Text    | The user's answer to the question              |
| user_id       | FK      | Foreign key to the `User` table (nullable)     |
| application_id| FK      | Foreign key to the `Application` table (nullable)|

#### **TodoList**
This table stores a to-do list for job applications the user intends to apply for later.

| Field             | Type    | Description                                  |
|-------------------|---------|----------------------------------------------|
| id                | Integer | Primary key                                  |
| application_title | Text    | Title of the job application the user plans to apply for|
| application_link  | URL     | Link to the job application (optional)       |
| completed         | Boolean | Whether the to-do item has been completed    |
| user_id           | FK      | Foreign key to the `User` table (nullable)   |

#### **ApplicationEmployee**
This join table manages the many-to-many relationship between applications and employees contacted.

| Field         | Type    | Description                                    |
|---------------|---------|------------------------------------------------|
| id            | Integer | Primary key                                    |
| application_id| FK      | Foreign key to the `Application` table         |
| employee_id   | FK      | Foreign key to the `Employee` table            |

### Relationships Overview
- **User**: Each user can have multiple job applications, questions, employees, and todo items.
- **Company**: A company can have multiple employees and job applications.
- **Application**: Each job application can have many associated questions and employees contacted.
- **TodoList**: A user can store job applications to apply for later.
- **Employee**: Employees can be linked to multiple job applications, and a job application can have multiple employees contacted.

For a visual representation, check the **ERD diagram** generated in the [Mermaid editor](https://www.mermaidchart.com/raw/7f1bbc01-92d3-4aaa-a40b-18240f476078?theme=dark&version=v0.1&format=svg).

  
### Database Migration
We use Django's ORM to manage database migrations. You can apply any database changes with:
```bash
python manage.py migrate
```

Got it! Let's adjust the documentation to reflect that you're using **generic views** instead of **ViewSets** and I'll provide the code in Markdown code blocks for better readability. Here's the corrected version:

### Views & Serializers
The project uses Django Rest Framework's **generic views** to handle the main API functionality, which offer built-in methods for common patterns (such as `list`, `retrieve`, `create`, `update`, and `delete`). **Serializers** are responsible for transforming complex data types like Django QuerySets into native Python datatypes for the API responses, and for validating incoming data.

#### Key Views:
- **JobApplicationListCreateView**: Handles listing and creating job applications.
- **JobApplicationDetailView**: Manages retrieving, updating, and deleting a specific job application.
- **CompanyListCreateView**: Responsible for listing and creating company records.
- **CompanyDetailView**: Handles retrieving, updating, and deleting company records.
- **EmployeeListCreateView**: Manages listing and creating employee contacts.
- **EmployeeDetailView**: Handles retrieving, updating, and deleting a specific employee record.
- **InterviewQuestionListCreateView**: Responsible for listing and creating interview questions.
- **InterviewQuestionDetailView**: Handles retrieving, updating, and deleting specific interview questions.

#### Key Serializers:
- **JobApplicationSerializer**: Converts job application data to and from native Python data types, ensuring validation of input data and structuring the API response.
- **CompanySerializer**: Handles serialization and deserialization of company records.
- **EmployeeSerializer**: Manages serialization for employee contact information tied to job applications.
- **InterviewQuestionSerializer**: Validates and converts interview question data.

### API Features:
- **User Authentication**: Powered by **Djoser**, enabling token-based authentication and user management (registration, login, password reset).
- **Filtering, Searching, Ordering**: The API supports advanced filtering, searching, and ordering on job applications, enabling users to narrow down search results based on various parameters.
- **Pagination**: Built-in pagination ensures that large data sets are split across multiple pages for better performance.

### Example of Common Endpoints:
- **`/api/token/login/`**: Login using Djoser.
- **`/api/applications/`**: Create, view, update, or delete job applications.
- **`/api/applications?search=Software`**: Search applications based on title.
- **`/api/applications?ordering=submission_date`**: Order applications by submission_date (asc/desc).
- **`/api/applications?filter=status=open`**: Filter applications by status.

For more details about the backend API, check out the [API Documentation](https://app.swaggerhub.com/apis-docs/ZEYADMOUSSA_1/JobLanderAPIs/1.0.3).

## Contributors
- **Zeyad Salah** (Backend Developer) - [Email](zeyad.moussa@ejust.edu.eg) - [Linkedin](https://www.linkedin.com/in/zeyad02/)
- **Aliaa Abobakr** (Frontend Developer) - [Email](zeyad.moussa@ejust.edu.eg) - [Linkedin](#)

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
