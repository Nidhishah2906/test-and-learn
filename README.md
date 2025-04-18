# Test N Learn Platform

A comprehensive online learning and assessment platform built with Django that enables users to test their programming skills, learn through video courses, and earn certifications.

## Features

### Learning Management
- Video-based courses with structured chapters
- Support for multiple programming languages and topics (Python, Java, Data Science)
- Interactive learning content with practical examples
- Organized course structure with 10 chapters per course

### Assessment System
- MCQ-based examinations for skill verification
- Timed assessments (15 minutes for 15 questions)
- Real-time exam progress tracking
- Instant result generation
- Auto-submission on timer expiry
- Required 50% score to pass examinations

### User Management
- User registration and authentication
- Profile management with avatar and bio
- Password reset functionality
- "Remember me" login option
- Social login support (GitHub, Google)

### Certification System
- Industry-recognized certifications
- Unique certification IDs for verification
- Downloadable certificates upon passing
- Course-specific certifications

### Payment Integration
- Secure payment processing
- Multiple payment method support
- Transaction verification

### Additional Features
- Responsive design for all devices
- User-friendly navigation
- Course search functionality
- Contact form for support
- Admin panel for content management

## Tech Stack

- **Backend**: Django 5.2
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite3
- **Authentication**: Django Auth, Social Auth
- **Media Storage**: Local file system
- **UI Framework**: Custom CSS with responsive design

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd test-and-learn
```

2. Create and activate a virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Start development server:
```bash
python manage.py runserver
```

Visit http://localhost:8000 to access the application.

## Project Structure

- `users/` - Core application directory
  - `templates/` - HTML templates
  - `static/` - CSS and static assets
  - `models.py` - Database models
  - `views.py` - View logic
  - `urls.py` - URL routing
- `media/` - Uploaded files and images
- `static/` - Global static files
- `requirements.txt` - Project dependencies

## Usage

1. Register an account or login
2. Browse available courses
3. Watch course videos and learn
4. Make payment for certification
5. Take the assessment
6. Get certified upon passing

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.