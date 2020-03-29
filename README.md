# korona web

## django web app for lazy people

- allows logged in users to post their homework on the site
  - has sorting by users and subjects
- all users can see posts and download homework files
- easy way to share homework
- made using the flexible Django framework, allowing for easy modifications

# instalation

- after cloning the repository, set up your `config.json` file in `/etc/config.json` like so

```
    {
      "SECRET_KEY": "DJANGO_SECRET_KEY",
      "EMAIL_USER": "YOUR_EMAIL_ADRESS",
      "EMAIL_PASS": "EMAIL_APP_PASSWORD"
    }
```
- if you plan on using this in production change `DEBUG=False` in `korona_web/korona_web/settings.py` and set your allowed hosts to your hostname

- run `python manage.py migrate` to migrate your database before running

