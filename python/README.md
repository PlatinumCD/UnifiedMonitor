# UnifiedMonitor Python Version
This is the Python version of the UnifiedMonitor project which monitors system and application components and logs their data.

## Requirements
- Python 3.6+
- psutil
- openai
- docker

## Setup
1. Clone the repository.
2. Create a virtual environment and activate it:
    ```shell
    python3 -m venv env
    source env/bin/activate
    ```
3. Install the dependencies:
    ```shell
    pip install -r requirements.txt
    ```

## Usage
To run the monitoring platform, use the following command:
```shell
python main.py
```