# UI Tests

This folder contains automated tests for the UI to validate both positive and common non-compliant scenarios.

## Requirements

- Python 3.4 or later
- `selenium` library
- `pytest` library
- The **Water Customer App Frontend App** set up on *http://localhost:3000*

## Setup

1. Clone the repository and navigate to the `ui-tests` directory.
2. Install the required libraries:
   ```sh
   pip install -r requirements.txt

## Run

To run the tests:
1. Open a Terminal, navigate to the `api-tests` directory
2. Start pytest:
   ```sh
   pytest -v