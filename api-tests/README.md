# API Tests

This folder contains automated tests for the API to validate both positive and common non-compliant scenarios.

## Requirements

- Python 3.4 or later
- `requests` library
- `pytest` library
- The **Water Customer App Backend App** set up and running on *http://localhost:3001*

## Setup

1. Clone the repository and navigate to the `api-tests` directory.
2. Install the required libraries using:
   ```sh
   pip install -r requirements.txt
   ```
   Or using:
   ```sh
   pip install requests
   pip install pytest
   ```

## Run

To run the tests:
1. Open a Terminal, navigate to the `api-tests` directory
2. Start pytest:
   ```sh
   pytest -v