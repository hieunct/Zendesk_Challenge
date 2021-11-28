# Introduction

This is a simple ticket viewer for viewing Zendesk tickets.

## Installation
Make sure you are using Python 3.7.+
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the dependency.

```bash
pip install -r requirements.txt
```

## Usage
First you need to create a ```.env``` file in the same directory with the ```main.py``` and initialize all of the environment variables:
```bash
API_TOKEN={Your Zendesk API Token}
SUB_DOMAIN={Your Zendesk subdomain}
EMAIL={Your Zendesk email}
```
After that, you can start using the application by running this command:
```bash
C:\Users\hieun\Zendesk_Challenge>python main.py
```
At this point, you can enter "ticket 1" to view the description of ticket #1 or "page 1" to view the content of page 1 of the ticket viewer:
```bash
Enter "menu" to view the options or "quit" to end
menu

            There are 100 tickets in total
            There are 4 pages in total

            * Enter "all" to view all the tickets.
            * Enter "ticket {number}" to view the ticket description.
            * Enter "page {number}" to view the page content at that page number.
            * Enter "quit" to end.
```

Here is the result after you enter "ticket 1":
```bash
ticket 1
   Ticket #1: Hi there,

I’m sending an email because I’m having a problem setting up your new product. Can you help me troubleshoot?

Thanks,
 The Customer



            There are 100 tickets in total
            There are 4 pages in total

            * Enter "all" to view all the tickets.
            * Enter "ticket {number}" to view the ticket description.
            * Enter "page {number}" to view the page content at that page number.
            * Enter "quit" to end.
```

Here is the result after you enter "page 1":
```bash
page 1
   1. Ticket with subject "Sample ticket: Meet the ticket" opened by "1267145063410" at "2021-11-27T20:36:25Z"
   2. Ticket with subject "Ticket#1" opened by "1267145063410" at "2021-11-27T21:07:00Z"
   3. Ticket with subject "velit eiusmod reprehenderit officia cupidatat" opened by "1267145063410" at "2021-11-28T01:22:05Z"
   4. Ticket with subject "excepteur laborum ex occaecat Lorem" opened by "1267145063410" at "2021-11-28T01:22:05Z"
   5. Ticket with subject "ad sunt qui aute ullamco" opened by "1267145063410" at "2021-11-28T01:22:06Z"
   6. Ticket with subject "aliquip mollit quis laborum incididunt" opened by "1267145063410" at "2021-11-28T01:22:07Z"
   7. Ticket with subject "nisi aliquip ipsum nostrud amet" opened by "1267145063410" at "2021-11-28T01:22:07Z"
   8. Ticket with subject "cillum quis nostrud labore amet" opened by "1267145063410" at "2021-11-28T01:22:08Z"
   9. Ticket with subject "proident est nisi non irure" opened by "1267145063410" at "2021-11-28T01:22:08Z"
   10. Ticket with subject "veniam ea eu minim aute" opened by "1267145063410" at "2021-11-28T01:22:09Z"
   11. Ticket with subject "magna reprehenderit nisi est cillum" opened by "1267145063410" at "2021-11-28T01:22:10Z"
   12. Ticket with subject "quis veniam ad sunt non" opened by "1267145063410" at "2021-11-28T01:22:10Z"
   13. Ticket with subject "tempor aliquip sint dolore incididunt" opened by "1267145063410" at "2021-11-28T01:22:11Z"
   14. Ticket with subject "labore pariatur ut laboris laboris" opened by "1267145063410" at "2021-11-28T01:22:11Z"
   15. Ticket with subject "officia mollit aliqua eu nostrud" opened by "1267145063410" at "2021-11-28T01:22:12Z"
   16. Ticket with subject "do incididunt incididunt quis anim" opened by "1267145063410" at "2021-11-28T01:22:13Z"
   17. Ticket with subject "tempor magna anim ea id" opened by "1267145063410" at "2021-11-28T01:22:13Z"
   18. Ticket with subject "exercitation sit incididunt magna laboris" opened by "1267145063410" at "2021-11-28T01:22:14Z"
   19. Ticket with subject "laborum ea ut in cupidatat" opened by "1267145063410" at "2021-11-28T01:22:15Z"
   20. Ticket with subject "est fugiat labore pariatur esse" opened by "1267145063410" at "2021-11-28T01:22:15Z"
   21. Ticket with subject "commodo sint laboris est et" opened by "1267145063410" at "2021-11-28T01:22:16Z"
   22. Ticket with subject "laboris sint Lorem ex Lorem" opened by "1267145063410" at "2021-11-28T01:22:17Z"
   23. Ticket with subject "esse adipisicing consectetur sunt tempor" opened by "1267145063410" at "2021-11-28T01:22:17Z"
   24. Ticket with subject "sunt enim pariatur id id" opened by "1267145063410" at "2021-11-28T01:22:18Z"
   25. Ticket with subject "et ad ut enim labore" opened by "1267145063410" at "2021-11-28T01:22:19Z"

   You're on page 1/4
```

## Testing
You can run this command to run all the unit tests:
```bash
C:\Users\hieun\Zendesk_Challenge>python test.py -v
```
It should appear like this:
```bash
C:\Users\hieun\Zendesk_Challenge>python test.py -v
test_authorized_200 (__main__.TestTicketViewer) ... ok
test_authorized_401 (__main__.TestTicketViewer) ... ok
test_generate_page_content (__main__.TestTicketViewer) ... ok
test_generate_ticket_description (__main__.TestTicketViewer) ... ok
test_generate_ticket_view_list (__main__.TestTicketViewer) ... ok
test_get_page_display_string (__main__.TestTicketViewer) ... ok
test_get_ticket_display_string (__main__.TestTicketViewer) ... ok
test_get_total_page_number (__main__.TestTicketViewer) ... ok
test_valid_page_str (__main__.TestTicketViewer) ... ok
test_valid_ticket_str (__main__.TestTicketViewer) ... ok

----------------------------------------------------------------------
Ran 10 tests in 1.173s

OK
```