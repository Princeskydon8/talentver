# Talent Verify

Talent Verify is an online talent verification service that allows employers to provide information
about themselves and their employees.This project uses Django as the backend and React as the frontend
to develop a cloud-based solution.

## Features

- Manage company information including name, date of registration, registration number, address, contact details, departments, and more.
- Keep track of employee details like name, employee ID, department, role, dates of employment, and duties.
- Perform single entry or bulk upload of company and employee data.
- Search employee data based on various attributes.
- Ensure data security with encryption for sensitive fields.
- Create and manage user roles for Company Admin and Talent Verify Admin.
- Stress testing to evaluate system performance under high loads.
- Cloud deployment for scalability.

## Project Structure

- `backend/`: Django backend code
- `frontend/`: React frontend code
- `docs/`: Documentation and other project-related files

## Getting Started

### Backend Setup

1. Navigate to the `backend` directory.
2. Install project dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the Django development server: `python manage.py runserver`

### Frontend Setup

1. Navigate to the `frontend` directory.
2. Install project dependencies: `npm install`
3. Start the React development server: `npm start`

## Usage

- Access the Django admin panel to manage companies, employees, and users: `http://localhost:8000/admin`
- Use the React frontend to interact with the Talent Verify system: `http://localhost:3000`

## API Endpoints

- Companies: `/api/companies/`
- Employees: `/api/employees/`

## Contributions

Contributions are welcome! If you find a bug or have a suggestion, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or inquiries, contact [Prince Sithole] at (mailto:princeskydon8@gmail.com)

