# CardSetAnalysis
A program to give a rough distribution of the cards in a MTGA set

Each year several MTGA card sets are released. Within each set, there are hundreds of cards with various methods to categorize them.
It is beneficial to understand the makeup of a set to grasp the true value of a card. Like the name of the format I enjoy the most,
my time is "Limited." This program will provide a distribution of the set pertaining to several categories thus, removing the need to
manually evaluate a cardset for a particular field.

Using the python wrapper for Scryfall API, Scrython, this code uses get requests to retrieve the Json object of some 200+ cards. The Json objects
are then stored into a Json file and loaded into a Card Object which will then get added to a Color Set Object. The colors correspond to the subsets of 
the overall set in Magic: The Gathering Arena, including: Black, Blue, Red, Green, White, Neutral, and Multi-Color. The card object stores all the information
about the card including it's Power, Toughness, Mana Cost and more. Once each card is loaded into a color subset, data is collected about each color subset such 
as how many Green Cards have a Mana Cost of 2, etc is determined. There are a lot of fields that go into an MTGA card, so more information can be processed from
the data available when needed.

Once distributions are determined, data will be saved to excel. Results can be found in Analysis.
