### Admin Account for Testing

- **Username:** `jovan.jovanovic@example.com`
- **Password:** `jovanjovanovic11`

### User Account for Testing

- **Username:** `mila.milic@example.com`
- **Password:** `milamilic11`

### Professor Account for Testing

- **Username:** `ivan.ivic@example.com`
- **Password:** `ivanivic11`


### Running Backend (Flask):
- python app.py

### Running  Vue.js app (Frontend):
- npm run dev

### Course Reservation Application 
- This is a full-stack application built using Flask (backend) and Vue.js (frontend). It allows users to browse available courses and reserve a spot. Admins can manage courses and users, while professors can view the list of students enrolled in their courses. Each course contains basic and additional information, including images.
  
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

Clean and responsive UI built without writing custom CSS files

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



