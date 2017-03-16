# CFD_A_library
An automated library software to catalogue books and efficiently displays its details.

For more details [Documentation.pdf](https://github.com/R-Wolf/CFD_A_library/blob/master/Documentation.pdf)
### Features
- Implemented in Django Framework and MySql database.
- Goodreads Api is used for book description, review, rating and book cover. 
- Automatic fine calculation.
- A reminder mail is send when a book is due.
- User's image is displayed from IITK database.
- Admin and various staff accounts.
- Bing Search.
- Trending Section of every week.
### Install via pip
```
pip install A_library
```

### Install via Github

```
git clone https://github.com/R-Wolf/CFD_A_library
```

#### Requirements 
Python Packages
- Pytz
- Regex
- Requests

### Run

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

