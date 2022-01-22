# Setup

## Getting API key

- You will need to get an API key from [etherscan](https://etherscan.io/apis) directly.
- Store this in a safe place.

## Environment Variables

It is not recommended that you store and pass your credentials in the python code directly. Especially if you use a version control system like git.

An alternative is to store your credentials as environment variables. You will need to set the `ETHERSCAN_API_KEY` variable.

1. You can do this on the terminal, running the following command before running your python script.

    ```bash
    # Replace XXX with your actual key
    export ETHERSCAN_API_KEY=XXX
    ```
2. Or, you could add the following contents to a `.env` file in your working directory (but make sure the `.env` file gets ignored by your version control)

    ```bash
    ETHERSCAN_API_KEY=XXX
    ```
