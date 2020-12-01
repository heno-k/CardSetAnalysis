import scrython
from scrython import cards, sets, foundation
import json
import time

def get_set_code():
    all_sets = sets.Sets()
    for i, set_object in enumerate(all_sets.data()):
        print(i, all_sets.data(i, "name"))

    choice = int(input("Select your set by number: "))

    code = all_sets.data(choice, "code")

    return 

def get_all_cards(card_array):
    card_list = []
    for card in card_array:
        time.sleep(0.5)
        id_ = card['id']
        card = cards.Id(id=id_)
        card_list.append(card)

    return card_list

def get_all_pages(set_code):
    page_count = 1
    all_data = []
    while True:
        time.sleep(0.5)
        page = cards.Search(q='e:{}'.format(set_code), page=page_count)
        all_data = all_data + page.data()
        page_count += 1
        if not page.has_more():
            break

    return all_data

def CreateDraftSetJson(SetCode, FilePath):
    if(SetCode is None):
        SetCode = get_set_code()

    card_list = get_all_pages(SetCode)
    card_list_objects = get_all_cards(card_list)

    
    with open(FilePath, 'w') as outfile:
        outfile.write('[')
        for card in card_list_objects:
            if(card.scryfallJson["booster"] == True):
                json.dump(card.scryfallJson, outfile, indent=4)
                if(card != card_list_objects[-1]):
                    outfile.write(',\n')
        outfile.write('\n]')
    #for card in card_list_objects:
    #    print(card.scryfallJson["name"])
    