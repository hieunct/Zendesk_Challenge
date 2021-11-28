import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
subdomain = os.environ.get("SUB_DOMAIN")
email = os.environ.get("EMAIL")
api_token = os.environ.get("API_TOKEN")
params = (
    ('include', 'comment_count'),
)

#Get the response data
def get_response(email, api_token, subdomain):
    try:
        #Get the response from the api
        response = requests.get(f"https://{subdomain}.zendesk.com/api/v2/tickets", params=params, auth=(f"{email}/token", api_token))
        #Convert the response to json format
        data = json.loads(response.text)
        status = response.status_code
        
        #Check if we successfully connect to the api
        if status != 200:
            return f"Authorization {status}. Couldn't authenticate you"
        else:
            return data
    except:
        return "Some errors with connecting to the API"

#Get all the tickets from the response
def get_ticket_list(response):
    ticket_list = response['tickets']
    return ticket_list

#List all the tickets view with a starting index
def generate_ticket_view_list(start, ticket_list):
    output = ""
    for (count, ticket) in enumerate(ticket_list, start):
        subject = '"' + ticket['subject'] + '"'
        submitter_id = '"' + str(ticket['submitter_id']) + '"'
        created_at = '"' + ticket['created_at'] + '"'
        ticket_str = f"   {count + 1}. Ticket with subject {subject} opened by {submitter_id} at {created_at}\n"
        output = output + ticket_str
    return output

#Display the string to describe about the number of tickets
def get_ticket_display_string(ticket_number):
    if ticket_number > 1:
        return f"There are {ticket_number} tickets in total"
    elif ticket_number == 1:
        return "There is 1 ticket in total"
    else:
        return "There is no ticket available"

#Display the string to describe about the number of pages
def get_page_display_string(page_number):
    if page_number > 1:
        return f"There are {page_number} pages in total"
    elif page_number == 1:
        return "There is 1 page in total"
    else:
        return "There is no page available"

#Check if the user input string for ticket is valid
def valid_ticket_str(ticket):
    ticket_arr = ticket.split(" ")
    is_valid = len(ticket_arr) == 2 and ticket_arr[0] == 'ticket' and ticket_arr[1].isnumeric()
    return is_valid

#Check if the user input string for page is valid
def valid_page_str(page):
    page = page.split(" ")
    is_valid = len(page) == 2 and page[0] == 'page' and page[1].isnumeric()
    return is_valid

#Generate the ticket description for a specific ticket
def generate_ticket_description(ticket, ticket_list):
    if valid_ticket_str(ticket) == False:
        return "Invalid ticket string"
    ticket_arr = ticket.split(" ")
    ticket_num = int(ticket_arr[1])
    if ticket_num > len(ticket_list):
        return "The ticket# exceeds the total number of tickets"
    else:
        description = ticket_list[ticket_num - 1]['description']
        return f"   Ticket #{ticket_num}: {description}"

#Generate all the tickets at a specific page
def generate_page_content(page, total_page, ticket_list):
    if valid_page_str(page) == False:
        return "Invalid page string"
    page_arr = page.split(" ")
    page_num = int(page_arr[1])
    if page_num > total_page:
        return "The page# exceeds the total number of pages"
    else:
        end_idx = min(len(ticket_list), page_num * 25)
        start_idx = (page_num - 1) * 25
        output = generate_ticket_view_list(start_idx, ticket_list[start_idx:end_idx])
        on_page = f"\n   You're on page {page_num}/{total_page}"
        output = output + on_page
        return output

#Calculate the total pages based on the number of tickets
def get_total_page_number(ticket_number):
    return int(ticket_number / 25) + int(((ticket_number % 25) + 24) / 25)

#Run the user CLI
def run_user_input():
    data = get_response(email, api_token, subdomain)
    if isinstance(data, str):
        print(data)
        return
    
    ticket_list = get_ticket_list(data)
    ticket_number = len(ticket_list)
    page_number = get_total_page_number(ticket_number)
    number_param_str = "{number}"
    
    ticket_str = get_ticket_display_string(ticket_number)
    page_str = get_page_display_string(page_number)
    
    welcome = "Welcome to the ticket viewer"
    menu = 'Enter "menu" to view the options or "quit" to end'
    ticket_option = f"""
            {ticket_str}
            {page_str}
            
            * Enter "all" to view all the tickets.
            * Enter "ticket {number_param_str}" to view the ticket description.
            * Enter "page {number_param_str}" to view the page content at that page number.
            * Enter "quit" to end.
    """
    invalid_str = "   Please enter valid input"

    print(welcome)
    print(menu)

    options = ''
    menu_entered = False
    while options != 'quit':
        options = input()
        if options == 'quit':
            return
        elif options == 'menu':
            menu_entered = True
            print(ticket_option)
        elif menu_entered and options == 'all':
            print(generate_page_content("page 1", page_number, ticket_list))
            print(ticket_option)
        elif menu_entered and valid_ticket_str(options):
            ticket_description = generate_ticket_description(options, ticket_list)
            print(ticket_description)
            print(ticket_option)
        elif menu_entered and valid_page_str(options):
            page_content = generate_page_content(options, page_number, ticket_list)
            print(page_content)
            print(ticket_option)
        else:
            print(invalid_str)

if __name__ == "__main__":
    run_user_input()
# run_user_input()