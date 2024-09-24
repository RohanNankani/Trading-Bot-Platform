# Trading Platform

## Overview

This project is a trading simulator platform. It has been developed with the following functionalities:

- Config-driven trading bots that can send buy and sell orders according to a particular strategy
- Matching engine to match buy and sell orders according to multiple matching algorithms
- Order Book to store all the orders 

## Installation

1. Navigate to the project directory:

    ```bash
    cd trading-bot-platform
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Install the CLI

    ```bash
    pip install -e .
    ```

## Usage

```sh
trade -f <path-to-config-file>
```

See [sample config](./tests/config.yaml)
