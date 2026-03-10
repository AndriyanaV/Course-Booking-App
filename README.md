### Admin Account for Testing

- **Username:** `jovan.jovanovic@example.com`
- **Password:** `jovanjovanovic11`

### User Account for Testing

- **Username:** `mila.milic@example.com`
- **Password:** `milamilic11`

### Professor Account for Testing

- **Username:** `jovana.donova@example.com`
- **Password:** `jovanadonova11`


### Running Backend (Flask):
- pip install -r requirements.txt
- python app.py

### Running  Vue.js app (Frontend):
- npm run dev

### Course Reservation Application 
- This is a full-stack application built using Flask (backend) and Vue.js (frontend). It allows users to browse available courses and reserve a spot. Admins can manage courses and users, while professors can view the list of students enrolled in their courses. Each course contains basic and additional information, including images.

### Tech Stack
Backend:
- Python
- Flask
- JWT Authentication
- Marshmallow (validation)

Frontend:
- Vue.js
- TailwindCSS
- VeeValidate (Form validation for Vue.js)
- Yup (schema validation library)
- Pinia

Database:
- MariaDB

## Project Structure
## API
- **blueprints/** – Organizes API routes using Flask Blueprints.
- **schemas/** – Contains Marshmallow schemas used for request validation.
- **decorators/** – Custom decorators for authentication and role checking.
- **database/** – Database connection and query logic.
- **utils/** – Helper functions used across the application.
- **uploads/** – Storage for uploaded files (e.g. user profile images).
- **constants/** – Central place for roles and constant values.

- **app.py** – Main Flask application where the server starts.
- **config.py** – Application configuration (environment variables, settings).
- **requirements.txt** – Python dependencies required to run the project.
- **course_management_test.sql** – SQL file for creating and populating the database.

## Frontend (web)
- **components/** – Reusable UI components used across the application.  
- **views/** – Main pages of the application (homepage, login, course list, etc.).  
- **stores/** – Global state management using Pinia.  
- **router/** – Defines application routes using Vue Router.  
- **composables/** – Reusable logic.  
- **validation/** – Form validation using VeeValidate and Yup.  
- **utils/** – Helper functions used across the frontend.  
- **assets/** – Static resources such as images and icons.

- **App.vue** – Root component of the Vue application.  
- **main.js** – Entry point where the Vue app is initialized.

## Roles
## Admin 
- Manage users
- Manage courses
- Modify language courses that are currently ongoing (current courses)
- Cancel reservation
- Cannot reserve a course for themselves.

## User 
- Browse courses
- Reserve courses
- Check information about the course

Professor
- View assigned courses
- See enrolled students
  
### Learned through project work
### Frontend (Vue.js):

Understanding of Vue project structure and environment

Reusable and modular components

Creating full page views (/login, /users, /courses) composed of multiple components

Route navigation using Vue Router

Axios for sending requests to the backend

Toastify for user-friendly notifications (success/error)

Token presence and validation for access control to pages and features

Using v-model for two-way data binding in forms

### Tailwind CSS – useful applications

Applied utility classes like grid, flex, gap, space-x, space-y for layout control

Quick UI development using shadow, rounded, hover, transition classes

Clean  UI built 

Used @apply directive to compose styles within component <style> blocks

Incorporated pre-built Tailwind components, including file upload forms for images

### Backend functionality and technology

Implemented JWT authentication using Flask-JWT-Extended

Routes protected by decorators that check:

 - If the user is authenticated

 - If the user has the correct role (e.g., only admins can access admin routes)

Custom guard functions used to:

 - Check if a course has expired → hide it from users

 - Check if course seats are full → prevent further reservations

Prevent a user from reserving the same course more than once (with appropriate HTTP status codes). The database has a unique constraint on user ID and course ID pairs to prevent duplicates.

Routes organized via Blueprints (e.g., users, courses, reservations)

Role-based route grouping (admin, professor, student)

Use of URL and query parameters for flexible filtering and access

### Database – MariaDB

The database schema includes all necessary relations between users, courses, and reservations

Constraints such as foreign key, unique, and not null ensure data integrity

###  Design
I personally created the UI/UX design for this project using Figma. You can explore the design prototypes and layouts here:
- https://www.figma.com/design/lj9NpxwlBdyBu8ZFl2oA3m/Untitled?node-id=0-1&p=f&t=AOxtfI94z72n4Gzc-0

