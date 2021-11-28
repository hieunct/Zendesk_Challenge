from main import *
import requests
import json
import os
from dotenv import load_dotenv
import unittest
load_dotenv()
subdomain = os.environ.get("SUB_DOMAIN")
email = os.environ.get("EMAIL")
api_token = os.environ.get("API_TOKEN")
params = (
    ('include', 'comment_count'),
)
ticket_list = get_ticket_list(get_response(email, api_token, subdomain))[:30]

class TestTicketViewer(unittest.TestCase):
    def test_authorized_200(self):
        # self.assertEqual('foo'.upper(), 'FOO')
        authorized_200 = type(get_response(email, api_token, subdomain)) is dict
        self.assertEqual(authorized_200, True) 

    def test_authorized_401(self):
        # self.assertTrue('FOO'.isupper())
        # self.assertFalse('Foo'.isupper())
        authorized_401 = get_response("hieu", api_token, subdomain) == "Authorization 401. Couldn't authenticate you"
        self.assertEqual(authorized_401, True)
        
    def test_generate_ticket_view_list(self):
        no_ticket = ""
        one_ticket = '   1. Ticket with subject "Sample ticket: Meet the ticket" opened by "1267145063410" at "2021-11-27T20:36:25Z"\n'
        many_tickets = '   1. Ticket with subject "Sample ticket: Meet the ticket" opened by "1267145063410" at "2021-11-27T20:36:25Z"\n   2. Ticket with subject "Ticket#1" opened by "1267145063410" at "2021-11-27T21:07:00Z"\n   3. Ticket with subject "velit eiusmod reprehenderit officia cupidatat" opened by "1267145063410" at "2021-11-28T01:22:05Z"\n   4. Ticket with subject "excepteur laborum ex occaecat Lorem" opened by "1267145063410" at "2021-11-28T01:22:05Z"\n   5. Ticket with subject "ad sunt qui aute ullamco" opened by "1267145063410" at "2021-11-28T01:22:06Z"\n'
        self.assertEqual(generate_ticket_view_list(0, []), no_ticket)
        self.assertEqual(generate_ticket_view_list(0, ticket_list[:1]), one_ticket)
        self.assertEqual(generate_ticket_view_list(0, ticket_list[:5]), many_tickets)
    
    def test_generate_ticket_description(self):
        inbound_ticket_num = '   Ticket #1: Hi there,\n\nI’m sending an email because I’m having a problem setting up your new product. Can you help me troubleshoot?\n\nThanks,\n The Customer\n\n'
        outbound_ticket_num = "The ticket# exceeds the total number of tickets"
        invalid_ticket_str = "Invalid ticket string"
        self.assertEqual(generate_ticket_description("ticket 1", ticket_list), inbound_ticket_num)
        self.assertEqual(generate_ticket_description("ticket 31", ticket_list), outbound_ticket_num)
        self.assertEqual(generate_ticket_description("haha haha", ticket_list), invalid_ticket_str)

    def test_generate_page_content(self):
        inbound_page_num = '   1. Ticket with subject "Sample ticket: Meet the ticket" opened by "1267145063410" at "2021-11-27T20:36:25Z"\n   2. Ticket with subject "Ticket#1" opened by "1267145063410" at "2021-11-27T21:07:00Z"\n   3. Ticket with subject "velit eiusmod reprehenderit officia cupidatat" opened by "1267145063410" at "2021-11-28T01:22:05Z"\n   4. Ticket with subject "excepteur laborum ex occaecat Lorem" opened by "1267145063410" at "2021-11-28T01:22:05Z"\n   5. Ticket with subject "ad sunt qui aute ullamco" opened by "1267145063410" at "2021-11-28T01:22:06Z"\n   6. Ticket with subject "aliquip mollit quis laborum incididunt" opened by "1267145063410" at "2021-11-28T01:22:07Z"\n   7. Ticket with subject "nisi aliquip ipsum nostrud amet" opened by "1267145063410" at "2021-11-28T01:22:07Z"\n   8. Ticket with subject "cillum quis nostrud labore amet" opened by "1267145063410" at "2021-11-28T01:22:08Z"\n   9. Ticket with subject "proident est nisi non irure" opened by "1267145063410" at "2021-11-28T01:22:08Z"\n   10. Ticket with subject "veniam ea eu minim aute" opened by "1267145063410" at "2021-11-28T01:22:09Z"\n   11. Ticket with subject "magna reprehenderit nisi est cillum" opened by "1267145063410" at "2021-11-28T01:22:10Z"\n   12. Ticket with subject "quis veniam ad sunt non" opened by "1267145063410" at "2021-11-28T01:22:10Z"\n   13. Ticket with subject "tempor aliquip sint dolore incididunt" opened by "1267145063410" at "2021-11-28T01:22:11Z"\n   14. Ticket with subject "labore pariatur ut laboris laboris" opened by "1267145063410" at "2021-11-28T01:22:11Z"\n   15. Ticket with subject "officia mollit aliqua eu nostrud" opened by "1267145063410" at "2021-11-28T01:22:12Z"\n   16. Ticket with subject "do incididunt incididunt quis anim" opened by "1267145063410" at "2021-11-28T01:22:13Z"\n   17. Ticket with subject "tempor magna anim ea id" opened by "1267145063410" at "2021-11-28T01:22:13Z"\n   18. Ticket with subject "exercitation sit incididunt magna laboris" opened by "1267145063410" at "2021-11-28T01:22:14Z"\n   19. Ticket with subject "laborum ea ut in cupidatat" opened by "1267145063410" at "2021-11-28T01:22:15Z"\n   20. Ticket with subject "est fugiat labore pariatur esse" opened by "1267145063410" at "2021-11-28T01:22:15Z"\n   21. Ticket with subject "commodo sint laboris est et" opened by "1267145063410" at "2021-11-28T01:22:16Z"\n   22. Ticket with subject "laboris sint Lorem ex Lorem" opened by "1267145063410" at "2021-11-28T01:22:17Z"\n   23. Ticket with subject "esse adipisicing consectetur sunt tempor" opened by "1267145063410" at "2021-11-28T01:22:17Z"\n   24. Ticket with subject "sunt enim pariatur id id" opened by "1267145063410" at "2021-11-28T01:22:18Z"\n   25. Ticket with subject "et ad ut enim labore" opened by "1267145063410" at "2021-11-28T01:22:19Z"\n\n   You\'re on page 1/2'
        outbound_page_num = "The page# exceeds the total number of pages"
        invalid_page_str = "Invalid page string"
        self.assertEqual(generate_page_content("page 1", 2, ticket_list), inbound_page_num)
        self.assertEqual(generate_page_content("page 31", 2, ticket_list), outbound_page_num)
        self.assertEqual(generate_page_content("haha haha", 2, ticket_list), invalid_page_str)

    def test_get_ticket_display_string(self):
        no_ticket = "There is no ticket available"
        one_ticket = "There is 1 ticket in total"
        many_tickets = "There are 30 tickets in total"
        self.assertEqual(get_ticket_display_string(0), no_ticket)
        self.assertEqual(get_ticket_display_string(1), one_ticket)
        self.assertEqual(get_ticket_display_string(30), many_tickets)

    def test_get_page_display_string(self):
        no_page = "There is no page available"
        one_page = "There is 1 page in total"
        many_pages = "There are 2 pages in total"
        self.assertEqual(get_page_display_string(0), no_page)
        self.assertEqual(get_page_display_string(1), one_page)
        self.assertEqual(get_page_display_string(2), many_pages)
    
    def test_valid_ticket_str(self):
        valid_str = "ticket 1"
        invalid_str1 = "ticket haha"
        invalid_str2 = "haha haha"
        self.assertEqual(valid_ticket_str(valid_str), True)
        self.assertEqual(valid_ticket_str(invalid_str1), False)
        self.assertEqual(valid_ticket_str(invalid_str2), False)

    def test_valid_page_str(self):
        valid_str = "page 1"
        invalid_str1 = "page haha"
        invalid_str2 = "haha haha"
        self.assertEqual(valid_page_str(valid_str), True)
        self.assertEqual(valid_page_str(invalid_str1), False)
        self.assertEqual(valid_page_str(invalid_str2), False)
    
    def test_get_total_page_number(self):
        no_ticket = 0
        one_ticket = 1
        less_than_25 = 10
        more_than_25 = 27
        self.assertEqual(get_total_page_number(no_ticket), 0)
        self.assertEqual(get_total_page_number(one_ticket), 1)
        self.assertEqual(get_total_page_number(less_than_25), 1)
        self.assertEqual(get_total_page_number(more_than_25), 2)

if __name__ == '__main__':
    unittest.main()