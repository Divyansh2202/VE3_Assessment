# CSV Data Analysis Web Application

This Django-based web application allows users to upload CSV files, perform data analysis using `pandas` and `numpy`, and view the results and visualizations on the web interface.

## Required Commands To Run The Project
- Step 1 : Clone the repository
- Step 2 : Run command "python manage.py runserver"
 

## Features

- **File Upload**: Upload CSV files through the web interface.
- **Data Analysis**: Analyze the uploaded data with `pandas` and `numpy`.
- **Visualizations**: Display data visualizations using `matplotlib` and `seaborn`.

## Requirements

- Python 3.x
- Django 4.x
- pandas 2.x
- numpy 1.x
- matplotlib 3.x
- seaborn 0.x
- scikit-learn 1.x
- python-dotenv (optional for environment variables)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Divyansh2202/VE3_Assessment.git
    cd your-repo
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    ```

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (for admin access, optional):

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000/` to use the application.

## Usage

- **Upload**: Use the homepage to upload a CSV file.
- **Analyze**: The application will process and analyze the file.
- **View Results**: Results and visualizations will be displayed on the web interface.

## Contributing

Feel free to fork the repository and submit pull requests for improvements. Please follow standard coding practices and ensure your code is well-documented.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

