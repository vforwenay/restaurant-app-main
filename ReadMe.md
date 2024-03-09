# Restuarent App

Restuarent App is an small application for voting the menu

## Features

- You can create menu for each day and then vote which one is best.

### Pre-requirements
These services must be installed, configured and running:

-- Sqllite
-- Python (>= 3.8)

## Installation

### Run Restuarent App locally using Docker

Clone the git repo and then switch to movies_wishlist folder
```
cd dev_task
docker build --tag <tagname> .
docker run --publish 8000:8000 <tagname>
```

This will start on http://localhost:8000 or http://127.0.0.1:8000