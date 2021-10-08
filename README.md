# Cryptomite
Cryptomite is a set of tools and trackers to get the most out of your staking yields.

First major feature will be a limit trigger to exit an LP farm and liquidate the native tokens.

## Stack

Originally this project started using the VueJs framework.
Go to https://github.com/preginald/cryptomite-frontend for the frontend project.

This repo tracks the backend API.

* Python
* Flask

## Roadmap

v1. Collection of static calculators

v2. Fetch prices from Polygon

v3. Send alert when limit triggered

v4. Exit farm when limit triggered

v5. Exit farm and liquidate tokens when limit triggered

## Dev environment

### Windows

1. virtualenv --python python venv
2. .\venv\Scripts\activate
3. pip install -r .\requirements.txt
4. python main.py