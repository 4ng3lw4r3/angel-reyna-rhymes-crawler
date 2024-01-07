
# ✧ Find Rhymes ✧

✧ ✧ ✧ This is a Python script for crawling lyrics and context information from Genius to find rhymes in any language. ✧ ✧ ✧

## ✧ Features ✧

- Crawl lyrics from Genius using the Genius API.
- Retrieve context information around a specific word in a song.
- Save the context information to a CSV file.
- Get rhymes in any language.
- Change the number of words you need to get around a specific word.

## ✧ Prerequisites ✧

- Python 3.x
- Required Python packages: `requests`, `beautifulsoup4`

## ✧ Usage ✧

1. Install the required packages:

    ```bash
    poetry install
    ```

   This will read dependencies from your `pyproject.toml` file and create a virtual environment for your project.

2. Run the script:

    ```bash
    poetry run python angel-reyna-crawler/main.py
    ```


3. For an example code run

    ```bash
    poetry run python angel-reyna-crawler/example.py
    ```

## ✧ Configuration ✧

- Genius API access token: You need to obtain a Genius API access token and set it in the configuration. There is one provided at the moment, oops.

## ✧ License ✧

This project is licensed under the [MIT License](LICENSE).
