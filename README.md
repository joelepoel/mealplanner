# Meal Planner

This is a Django-based meal planner application that allows users to save recipes and generate weekly meal plans. Users can create, edit, and delete recipes, including title, description, and optional image. The application can generate a 7-day meal plan based on the saved recipes, with placeholders for empty days and the ability to reroll individual meals.

---

## Features

- Add, edit, and delete recipes
- Each recipe includes:
  - Title
  - Description
  - Image (optional)
- Generate a weekly meal plan (7 days)
  - Placeholders for empty days
  - Reroll individual days to get a new random recipe
- Custom user model (overrides Django's default)
- Profile model automatically created after user registration via Django signals

---

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/joelepoel/mealplanner.git
   cd mealplanner
   ```

2. **Install dependencies using Pipenv**

   ```bash
   pipenv install
   pipenv shell
   ```

   To exit the virtual environment, run:

   ```bash
   exit
   ```

3. **Create and configure your MySQL database**

   - Manually create a MySQL database.
   - Open `settings.py` and update the `DATABASES` section with your MySQL credentials.

4. **Make migrations and apply them**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **(Optional) Create a superuser for admin access**

   ```bash
   python manage.py createsuperuser
   ```

6. **Ensure media folder is set up**

   By default, the app uses a media folder for uploaded images.  

   - Create a `media/` directory in your project root, or update `MEDIA_ROOT` and `MEDIA_URL` in `settings.py` as needed.  
   - Recipes and user profiles will use default images if none are provided.

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   Access the application at:

   ```
   http://127.0.0.1:8000/
   ```

   Press `Ctrl + C` to stop the server.

---

## Notes

- This project uses Pipenv for dependency management. Python, Django versions, and all required libraries are handled automatically through the `Pipfile`.
- Uploaded images are saved in the `media/` folder unless configured otherwise in `settings.py`.
- Weekly meal plans are stored in the session, so they persist while the user is logged in but are not permanently saved in the database.  
- If no recipes are available when generating or rerolling, a warning is shown to prompt users to add recipes first.

