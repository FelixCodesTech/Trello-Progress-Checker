import requests

# Read Own Trello API key and token
with open("info.txt") as f:
    lines = f.readlines()
    API_KEY = str(lines[0])[0:-1]   #first line
    API_TOKEN = str(lines[1])[0:-1] #second line
    BOARD_ID = str(lines[2])        #third line

# List we don't want to count
LIST_NAME = 'DONE'

# Make a request to the Trello API to get the lists in the board
response = requests.get(
    f'https://api.trello.com/1/boards/{BOARD_ID}/lists',
    params={
        'key': API_KEY,
        'token': API_TOKEN,
    },
)

# Check if the request was successful
if response.status_code != 200:
    print('Error:', response.text)
    exit()

# Find the ID of the list with the matching name
lists = response.json()
done_list_id = None
for trello_list in lists:
    if trello_list['name'] == LIST_NAME:
        done_list_id = trello_list['id']
        break

# Make a request to the Trello API to get the cards in the board
response = requests.get(
    f'https://api.trello.com/1/boards/{BOARD_ID}/cards',
    params={
        'key': API_KEY,
        'token': API_TOKEN,
    },
)

# Check if the request was successful
if response.status_code != 200:
    print('Error:', response.text)
    exit()

# Filter out the cards in the "DONE" list
cards = response.json()
if done_list_id:
    totalCards = [card for card in cards]
    cards = [card for card in cards if card['idList'] != done_list_id]

# Count the number of cards that are not in the "DONE" list
num_cards = len(cards)
print(f'Number of cards not in the "{LIST_NAME}" list: {num_cards}')

percent_done = round((len(totalCards) - len(cards)) / len(totalCards) * 100, 1)

# Print the percentage of cards that are not in the "DONE" list
print(f'{percent_done}% of the cards are not in the "{LIST_NAME}" list')