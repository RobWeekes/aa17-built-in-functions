# Given a list of dictionaries representing credit cards, sort the list in
# descending order according to the `num_users` property. Do the sort out-of
# place without mutating the original list, using the `sorted` built in
# function, and then return only the company names in a list, in the correct
# sorted order.

cards = [
    {
        "company": "Wells Fargo",
        "card_name": "Active Cash",
        "annual_fee": 0,
        "intro_reward_type": "cash",
        "intro_reward_amount": 200,
        "num_users": 20
    },
    {
        "company": "Chase",
        "card_name": "Sapphire Preferred",
        "annual_fee": 95,
        "intro_reward_type": "points",
        "intro_reward_amount": 60000,
        "num_users": 54
    },
    {
        "company": "Citi",
        "card_name": "Diamond Preferred",
        "annual_fee": 0,
        "intro_reward_type": "cash",
        "intro_reward_amount": 150,
        "num_users": 13
    }
]

# Write your code here.

# start w helper function
def users(card):
    return card['num_users']

def sort_cards(card_list):
    # map method can key into specific values and return them, but no sorting?
    # cards = list(map(lambda card: card['num_users'], card_list))# [20, 54, 13]
    in_order = sorted(card_list, key=users, reverse=True)
    companies = map(lambda company: company['company'], in_order)
    print(f'companies map object: {companies}')
    # print(f'companies list: {list(companies)}')   # only use list() for test printing -> comment this print out and use list in the return statement
    return list(companies)
print(sort_cards(cards))       # ['Chase', 'Wells Fargo', 'Citi']
