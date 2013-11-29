# Heroku Commands for Rails projects

### Add remote heroku repo
    git remote add heroku git@heroku.com:your-project-name.git

### Push to heroku
    git push heroku master

### Open Heroku Console
    heroku run rails c

### Migrate heroku db
    heroku run rake db:migrate
