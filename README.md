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
- **User Management**: Users can sign up, log in, and manage their profiles.
- **Job Application Tracking**: Add, edit, delete, and track the status of job applications.
- **Company and Contact Management**: Keep records of companies and their employees for networking.
- **Interview Preparation**: Log questions asked during interviews to better prepare for future opportunities.
- **Analytics and Insights**: Track application success rates, rejections, and generate progress reports.

## API Documentation
For detailed API documentation and usage, please refer to our [API Documentation](#) hosted externally. The API supports the following operations:
- User registration, login, and profile management
- Job application creation, update, and deletion
- Company and employee contact management
- Interview question logging
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
- Generate reports and statistics for better insights

## Frontend Overview
The frontend of JobLander is built with modern technologies, offering a smooth and intuitive user experience. Key frontend technologies include:
- **React.js**: For building the user interface and handling the overall application flow.
- **Chart.js**: For rendering insightful data visualizations and statistics.

## Backend Overview
The backend API for JobLander is built using **Django**, ensuring scalability and flexibility. The key components of the backend include:
- **User Authentication**: Secure user management, including registration and login functionality.
- **Job Applications API**: Create, update, delete, and track job applications.
- **Company and Employee Management**: Manage the companies and contacts associated with job applications.
- **Analytics API**: Generate real-time reports on job application performance and statistics.

For more details about the backend API, check out the [API Documentation](https://app.swaggerhub.com/apis-docs/ZEYADMOUSSA_1/JobLanderAPIs/1.0.3).

## Contributors
- **Zeyad Salah** (Backend Developer) - [Email](zeyad.moussa@ejust.edu.eg) - [Linkedin](https://www.linkedin.com/in/zeyad02/)
- **Aliaa Abobakr** (Frontend Developer) - [Email](zeyad.moussa@ejust.edu.eg) - [Linkedin](#)

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
