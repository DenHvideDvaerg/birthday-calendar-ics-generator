# Birthday Calendar ICS Generator

This repository contains a Python script that reads birthdays from a CSV file and generates an iCalendar (ICS) file with birthday events for a specified number of years. The script imports the birthdays, creates events with age and notes, and exports the events to an ICS file that can be imported into calendar applications.

## Features

- Read birthdays from a CSV file with customizable delimiter and date format.
- Generate birthday events for a specified number of years.
- Include optional notes for each birthday event.
- Export birthday events to an ICS file that can be imported into calendar applications.

## Installation

To install and use the Birthday Calendar ICS Generator script, follow these steps:

1. Clone the repository:

```
git clone https://github.com/DenHvideDvaerg/birthday-calendar-ics-generator.git
```

2. Change directory to the cloned repository:

```
cd birthday-calendar-ics-generator
```

3. Make sure you have Python 3 installed on your machine. You can check the installed version with the following command:

```
python --version
```

4. Install the required dependencies:

```
pip install ics
```

## Usage

1. Prepare a CSV file with the following format:

```
name;birthdate;note
Mom;01/01/1978;
Dad;15/05/1975;
Son;12/02/2002;Birth weight 3350g.
```

- The delimiter can be customized in the script (default is `;`).
- The date format can be customized in the script (default is `%d/%m/%Y`).

2. Update the configuration variables in the script, if necessary:

- `csv_file`: Path to the CSV file with the birthdays.
- `ical_file`: Path to the output ICS file.
- `max_age`: Maximum age for the generated birthday events.
- `csv_deliiter`: Delimiter used in the CSV file.
- `date_format`: Date format used for the birthdates in the CSV file.

3. Run the `birthday_calendar_ics_generator.py` script using Python:

```
python birthday_calendar_ics_generator.py
```

4. Import the generated ICS file into your calendar application.