# Myanmar InnoHub (MiH)

Myanmar InnoHub is a Django web application for showcasing technology innovations from Myanmar innovators. The platform lets users register, publish projects, browse and filter projects, comment, rate projects, and contact administrators. Administrators can manage users, projects, announcements, contact messages, and project reference data.

## Project Overview

MiH is organized as a multi-app Django project:

- `authentication`: custom email-based users, login, registration, profile management, password changes, user homepage, and user management.
- `projects_app`: project models and workflows for Software, Hardware, and AI projects.
- `feedback_app`: project comments and ratings.
- `admin_app`: admin dashboard, project statistics, role management, announcements, contacts, and reference-data management.

The project uses Django templates for the frontend, SQLite for local development, and uploaded media for user profile pictures and project cover images.

## Detailed Specs

### Technology Stack

- Python
- Django 6.0
- SQLite
- Django templates
- Static CSS and image assets
- Pillow for image upload support

### Main Features

#### Authentication and User Accounts

- Users register with name, email, and password.
- Email is used as the login identifier instead of username.
- Users can log in and log out.
- Users can view and update their profile.
- Users can change their password.
- Profile fields include name, phone, address, and profile picture.

#### Roles and Permissions

The app supports role-based behavior:

- `user`: default role for registered users.
- `admin`: can access administrative project, announcement, contact, and reference-data pages.
- `rootadmin`: used by permission decorators for granting and revoking admin access.

Note: `rootadmin` is referenced in the view logic, but the current `User.role` choices only define `admin` and `user`. If root admin behavior is needed, the model choices should be updated.

#### Project Management

Users can create, view, update, and delete projects. Projects share common fields:

- Title
- Innovator
- Cover photo
- Description
- Duration
- Project type
- Created date/time

Supported project types:

##### Software Projects

Software projects include:

- Source link
- Programming language
- Framework
- Platform

Supported platforms:

- Web
- Mobile
- Desktop
- Cross Platform

##### Hardware Projects

Hardware projects include:

- Code/source link
- Components
- Skill level

Supported skill levels:

- Beginner
- Intermediate
- Advanced

##### AI Projects

AI projects include:

- Dataset link
- Notebook/source link
- Algorithms
- Focus area

#### Browsing, Search, and Filtering

Users can:

- Browse all projects.
- Search projects by title.
- Filter software projects by platform, language, or framework.
- Filter hardware projects by skill level.
- Filter AI projects by focus area or algorithm.
- View detailed pages for each project type.

#### Feedback

Authenticated users can:

- Add comments to projects.
- Delete their own comments.
- Rate projects from 1 to 5.
- Update their previous rating for a project.

Each user can have only one rating per project.

#### Admin Features

Admins can:

- View project statistics.
- List and search projects.
- Filter projects by type.
- View and manage users.
- Create, update, and delete announcements.
- View contact messages submitted by users.
- Manage reference data:
  - Languages
  - Frameworks
  - Components
  - Focus areas
  - Algorithms

Root admins can:

- Grant admin access to users.
- Revoke admin access from admins.

### Validation Rules

Project forms include validation for:

- Title must be at least 5 characters.
- Description must be at least 30 characters.
- Duration must be positive.
- Duration must not exceed 260 weeks.
- Cover photo is required.
- Software source link must start with `https://`.
- Hardware code link must start with `https://`.
- Hardware projects must include at least one component.
- AI projects must include at least one algorithm.
- AI dataset link and notebook link must be different.

Profile forms include validation for:

- Name cannot be empty.
- Phone number must contain only digits.
- Phone number must be between 7 and 20 digits if provided.

Password change validates:

- Old password must be correct.
- New password cannot match old password.
- New password and confirmation must match.

### Main Routes

#### Authentication

- `/` - Login page
- `/register/` - Register
- `/signin/` - Sign in
- `/signout/` - Sign out
- `/user-homepage/` - User homepage
- `/profile/` - Profile page
- `/update-profile/<id>/` - Update profile
- `/change-password/` - Change password
- `/announcements/` - Announcement list

#### Projects

- `/sw-create/` - Create software project
- `/hw-create/` - Create hardware project
- `/ai-create/` - Create AI project
- `/project-detail/<id>/` - Project detail
- `/sw-update/<id>` - Update software project
- `/hw-update/<id>` - Update hardware project
- `/ai-update/<id>` - Update AI project
- `/project-delete/<id>/` - Delete project

#### Admin

- `/user-list/` - User management
- `/project-list/` - Project list
- `/project-stats/` - Project statistics
- `/grant-admin/<id>/` - Grant admin role
- `/revoke-admin/<id>/` - Revoke admin role
- `/create-announcement/` - Create/list announcements
- `/delete-announcement/<id>/` - Delete announcement
- `/update-announcement/<id>/` - Update announcement
- `/create-contact/` - Submit contact message
- `/contact-list/` - Admin contact list

#### Reference Data

- `/language-create/`
- `/language-update/<id>/`
- `/language-delete/<id>/`
- `/framework-create/`
- `/framework-update/<id>/`
- `/framework-delete/<id>/`
- `/component-create/`
- `/component-update/<id>/`
- `/component-delete/<id>/`
- `/focus-create/`
- `/focus-update/<id>/`
- `/focus-delete/<id>/`
- `/algorithm-create/`
- `/algorithm-update/<id>/`
- `/algorithm-delete/<id>/`

#### Feedback

- `/add-comment/<project_id>/`
- `/comment/delete/<comment_id>/`
- `/add-rating/<project_id>/`

## Project Structure

```text
MiH_Project/
  manage.py
  requirements.txt
  MiH_Project/
    settings.py
    urls.py
    asgi.py
    wsgi.py
  authentication/
    models.py
    forms.py
    views.py
    templates/
    static/
  projects_app/
    models.py
    forms.py
    views.py
    templates/
    static/
  feedback_app/
    models.py
    forms.py
    views.py
  admin_app/
    models.py
    forms.py
    views.py
    templates/
    static/
```

## Prerequisites

For the normal local setup:

- Python 3.13 or compatible Python version
- `pip`
- PowerShell, Command Prompt, Git Bash, or another terminal

For the Docker setup:

- Docker Desktop
- Docker Compose

## Run Locally by Installing Dependencies

From the repository root:

```powershell
cd MiH_Project
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate the virtual environment again:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Apply migrations:

```powershell
python manage.py migrate
```

Create a superuser:

```powershell
python manage.py createsuperuser
```

Run the development server:

```powershell
python manage.py runserver
```

Open the app:

```text
http://127.0.0.1:8000/
```

Django admin:

```text
http://127.0.0.1:8000/admin/
```

## Run Locally with Docker

Build and start the container:

```powershell
cd MiH_Project
docker compose up --build
```

In another terminal, apply migrations:

```powershell
docker compose exec web python manage.py migrate
```

Create a superuser:

```powershell
docker compose exec web python manage.py createsuperuser
```

Open the app:

```text
http://127.0.0.1:8000/
```

Stop Docker:

```powershell
docker compose down
```

## Notes for First-Time Setup

After creating a superuser, you may need to set the user's `role` field to `admin` through Django admin if you want to access the custom admin dashboard pages.

The app stores uploaded media in:

```text
MiH_Project/media/
```

The default local database is:

```text
MiH_Project/db.sqlite3
```

---
