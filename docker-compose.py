version: "3.3"

services:
  talana:
    container_name: talana
    image: python:3.9-buster
    command: python /code/talana.py
    volumes:
      - .:/code
