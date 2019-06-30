# Where are our grades?

Lecturers usually publish the results of exams on their websites - very often in designated sections of the page.

This simple program is a tool that automatizes arduous task that is checking if the grades were already published.
Program checks, once every given time period, if there is any difference in content of the website.
Once the results arrive, an adequate email notification is sent to all the addresses from the mailing list.

## Requirements

- requests
- beautifulsoup4

## Usage

1. Specify your data in config.json file - program requires the following data

- website address
- (optional) website's DOM element that will be compared
- wait time
- email address and password (used for sending notification)
- content of the mail
- list of recipients
- mailing server's information

2. Run Python script (python main.py).

### Available modes:

Program has two available modes, that check if ther is any change :

- on the website as a whole,
- in a designated section pointed using HTML tag and its class / id.
