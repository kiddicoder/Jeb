# Job Hunters

## Table of contents
- [Project Description](#project-description)
- [Core Requirements](#core-requirements)
- [Extra Requirements](#extra-requirements)
- [Installation and Setup](#installation-and-setup)
- [Usage Instructions](#usage-instructions)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Description
Job Hunters is a web platform designed to connect job seekers with employers. The platform allows job seekers to search for job opportunities and apply for jobs. Employers can post job listings and create company profiles. The application is built using Django, PostgreSQL, and CSS for styling.

## Core Requirements

### Layout Site
- Navigation bar
- Footer

### Edit Profile
- Add or update name
- Upload or change profile image

### Job Offer Site
- List available job offerings
- Filter by category (e.g., Software Engineering, Data Science)
- Filter by company
- Filter by already applied job offerings
- Search job offerings based on name
- Sort job offerings by date, due date

### Job Offering Detail Site
- View detail site for a job offering
- View the title of a job offering
- See if a job is full-time or part-time
- See the location of the job offering
- See the job category
- See the due date
- See the starting date
- Read the job offering description in HTML format
- View the company's name
- View the company's address
- Access a link to the company's page
- Click a button to apply for a job offering if not already applied
- See the status of an application, including when it was applied

### Company Detail Site
- Navigate to a company's detail site
- View the title of the company
- View the address of the company
- See the company's logo
- See the cover image of the company
- Read the company's description in HTML format
- View a list of all non-due job offerings with links
- Click on a job offering from the list to navigate to its detail site

### Job Applications Page
- Navigate to the job applications page
- View a list of all job applications
- View job title, date of application, and status
- View the company associated with each application
- See whether a job is full-time or part-time

### Applying for a Job
- Apply for a job offering
- Proceed to the next step of the application phase
- Navigate to the previous step of the application phase
- Enter full name, street number, house number, city, country, and postal code in contact information step
- Write a cover letter in a text section
- Add job experiences: place of work, role, start date, end date
- Add recommendation contacts: name, email address, phone number, permission to contact, role
- Review all entered information in a read-only format before final submission
- Receive a confirmation that the application was successful, with further navigation back disabled

### User Authentication
- Create an account using a username and password
- Log in to account using email and password
- Log out of account


## Extra Requirements

### Job Offer Site
- Create a job offer
- View favorited job offerings

### Profile Enhancements
- Add a bio to profile
- Add and update contact information in profile
- Add and remove job experiences in profile
- Add and remove references contacts in profile
- Autofill contact information, job experiences, and recommendation contacts during the job application phase

### Employer Features
- Create company
- Update company profile information: logo, cover image, address, description in HTML format
- Post new job offerings
- View list of all active postings
- Delete job postings
- View detail site for each job posting
- Delete Company

## Installation and Setup

### Prerequisites
- Python 3.12.2
- PostgreSQL
- Git

## Installation Steps

### Create a virtual environment
- To create a virtual environment and install dependencies from a requirements.txt file, follow these steps for both macOS and Windows.

### macOS

1. Open Terminal: You can find it in Applications > Utilities > Terminal.

2. Navigate to your project directory:
    
    cd /path/to/your/project

3. Ensure Python is installed: macOS typically comes with Python pre-installed. You can check your Python version:
   
    python3 --version

    If you need to install Python, download it from [python.org](https://www.python.org/downloads/).

5. Install virtualenv (if not already installed):
   
    pip3 install virtualenv
   
6. Create a virtual environment inside jeb_project:
    
    python3 -m venv venv
   
7. Activate the virtual environment inside jeb_project:
    
    source venv/bin/activate
    
8. Install the dependencies from requirements.txt inside jeb_project:
    
    pip install -r requirements.txt
    
9. Deactivate the virtual environment (when you're done):
    
    deactivate

### Windows

1. Open Command Prompt or PowerShell: You can do this by searching for `cmd` or `powershell` in the Start menu.

2. Navigate to your project directory:
   
    cd \path\to\your\project

3. Ensure Python is installed: You can check your Python version:
    
    python --version
    
    If you need to install Python, download it from [python.org](https://www.python.org/downloads/). Ensure you check the option to add Python to your PATH during installation.

4. Install virtualenv (if not already installed):
    
    pip install virtualenv

5. Create a virtual environment inside jeb_project:
    
    python -m venv venv

6. Activate the virtual environment inside jeb_project:
   
    .\venv\Scripts\activate
   
7. Install the dependencies from requirements.txt inside jeb_project:
   
    pip install -r requirements.txt

8. Deactivate the virtual environment (when you're done):
    
    deactivate


Following these steps will help you set up a virtual environment and install your project's dependencies on both macOS and Windows.

## Usage Instructions

### Register an Account: 

- Visit the registration page and create a new account.

### Log In:

- Log in with your new account credentials.

### Edit Profile:

- Update your profile information and upload a profile image.

### Browse Jobs:

- Search for jobs using the search bar and filters.

### Apply for Jobs:

- Apply for jobs by filling out the application form.

### Manage Applications:

- View and manage your job applications from the applications page.

### Employer Functions:

- If you are an employer, post new job offerings and manage applications.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- Django for the web framework
- PostgreSQL for the database
- All contributors and open-source libraries used in this project
