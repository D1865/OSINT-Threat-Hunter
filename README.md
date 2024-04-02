# OSINT Collector for Threat Hunting

## Introduction
The OSINT Collector for Threat Hunting is a command-line tool designed for Linux systems. It automates the collection of Open Source Intelligence (OSINT) from publicly available sources, aiding cybersecurity professionals and enthusiasts in proactive threat hunting. By aggregating data from various sources, it provides valuable insights for identifying potential security threats.

## Features
- Automated collection of OSINT data from specified public sources.
- Simple, Linux command-line interface.
- JSON formatted output for easy parsing and integration with other tools.

## Installation
Before deploying this tool, ensure you have Python 3.x and pip installed on your Linux machine.

Install the required dependencies:

```pip install requests beautifulsoup4```

## Basic Usage

Navigate to the directory containing osint_collector.py and run:

```python osint_collector.py --output collected_data.json```

This command collects OSINT data and saves it in collected_data.json. You can specify any filename for the output.

## Advanced Usage:

Creating a Bash Wrapper Script. For ease of use, you can create a bash script to run the OSINT Collector with predefined parameters. Save the following content in a file named run_osint.sh:


```shell
#!/bin/bash
# Directory where you want to save the output
OUTPUT_DIR="/path/to/your/output/directory"
# Filename for the output data
FILENAME="osint_data.json"
# Full path to the Python script
SCRIPT_PATH="/path/to/osint_collector.py"
python $SCRIPT_PATH --output $OUTPUT_DIR/$FILENAME
```

Make your script executable

``` bash chmod +x run_osint.sh```

Now, you can run your OSINT Collector simply by executing ./run_osint.sh.

## Automating with Cron
To collect OSINT data at regular intervals, such as daily or hourly, you can set up a cron job.

### Edit your crontab file by running:

```crontab -e```

Add a line to schedule your script. For example, to run it every hour:

cron

```0 * * * * /path/to/run_osint.sh```

This cron job executes ```run_osint.sh``` at the start of every hour, collecting and saving the latest OSINT data.

### Extending the Collector

Contributions to the OSINT Collector project are welcome. Whether it's adding new sources, improving the data processing logic, or providing feedback, your input is valuable.

## License

This project is licensed under the MIT License. 

