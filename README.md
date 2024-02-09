# Project Name
Create a REST API that takes in multiple paragraphs of text as input, stores each paragraph
and the words to paragraph mappings on a postgreSQL database.

## Usage

### Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set up PostgreSQL database and update configuration in `settings.py`.
4. Run migrations: `python manage.py migrate`.

### Running the Code
1. Start the Django server: `python manage.py runserver`.
2. Authenticate using `/api/login/`.
3. Use endpoints like `/api/paragraphs/` to interact with stored paragraphs.

## Documentation
- Detailed API documentation is provided in the project repository.
