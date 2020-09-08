from bs4 import BeautifulSoup
import requests
import json
import csv
from threading import Thread
import time


class House(Thread):
    """ Class defining a house characterized by :
    - his Locality
    - his type of property (House/apartment)
    - his Subtype of property (Bungalow, Chalet, Mansion, ...)
    - his Price
    - his Type of sale (Exclusion of life sales)
    - his Number of rooms
    - his Area
    - his Fully equipped kitchen (Yes/No)
    - his Furnished (Yes/No)
    - his Open fire (Yes/No)
    - his Terrace (Yes/No)
    - his Terrace Area (If terrace yes)
    - his Garden (Yes/No)
    - his Garden Area (If garden yes)
    - his Surface of the land
    - his Surface area of the plot of land
    - his Number of facades
    - his Swimming pool (Yes/No)
    - his State of the building (New, to be renovated, ...)
    """

    def __init__(self):
        Thread.__init__(self)
        """Constructor our class"""
        self.locality = "No Value found"
        self.type_of_property = "No Value found"
        self.subtype_of_property = "No Value found"
        self.price = "No Value found"
        self.type_of_sale = "No Value found"
        self.number_of_rooms = "No Value found"
        self.house_area = "No Value found"  # taille du terrain
        self.fully_equipped_kitchen = "No Value found"
        self.furnished = str(None)
        self.open_fire = "No Value found"
        self.terrace = "No Value found"
        self.terrace_area = "No Value found"
        self.garden = "No Value found"
        self.garden_area = "No Value found"
        self.surface_of_the_land = "No Value found"
        self.surface_of_the_plot_of_land = str(None)
        self.number_of_facades = "No Value found"
        self.swimming_pool = "No Value found"
        self.state_of_the_building = "No Value found"

        # optionnel

        self.construction_year = "m"

    # permet de rajouter des données au fichier CSV

    def save_to_csv(self):
        with open('house_detail.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.locality, self.type_of_property, self.subtype_of_property, self.price,
                             self.type_of_sale, self.number_of_rooms, self.house_area, self.fully_equipped_kitchen,
                             self.furnished, self.open_fire, self.terrace, self.terrace_area, self.garden,
                             self.garden_area, self.surface_of_the_land, self.surface_of_the_plot_of_land,
                             self.number_of_facades, self.swimming_pool, self.state_of_the_building,
                             self.construction_year])

    # permet de creer le fichier CSV (avec les en-tête)

    def create_csv(self):
        with open('house_detail.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["locality", "type_of_property", "subtype_of_property", "price", "type_of_sale",
                             "number_of_rooms", "house_area", "fully_equipped_kitchen", "furnished", "open_fire",
                             "terrace", "terrace_area", "garden", "garden_area", "surface_of_the_land",
                             "surface_of_the_plot_of_land", "number_of_facades", "swimming_pool",
                             "state_of_the_building", "construction_year"])
            writer.writerow([self.locality, self.type_of_property, self.subtype_of_property, self.price,
                             self.type_of_sale, self.number_of_rooms, self.house_area, self.fully_equipped_kitchen,
                             self.furnished, self.open_fire, self.terrace, self.terrace_area, self.garden,
                             self.garden_area, self.surface_of_the_land, self.surface_of_the_plot_of_land,
                             self.number_of_facades, self.swimming_pool, self.state_of_the_building,
                             self.construction_year])

    def print(self):
        print("locality : " + self.locality + "\n",
              "type_of_property : " + self.type_of_property + "\n",
              "subtype_of_property : " + str(self.subtype_of_property) + "\n",
              "price : " + self.price + "\n",
              "type_of_sale : " + self.type_of_sale + "\n",
              "number_of_rooms : " + self.number_of_rooms + "\n",
              "house_area : " + self.house_area + "\n",
              "fully_equipped_kitchen : " + self.fully_equipped_kitchen + "\n",
              "furnished : " + self.furnished + "\n",
              "open_fire : " + self.open_fire + "\n",
              "terrace : " + self.terrace + "\n",
              "terrace_area : " + self.terrace_area + "\n",
              "garden : " + self.garden + "\n",
              "garden_area : " + self.garden_area + "\n",
              "surface_of_the_land : " + self.surface_of_the_land + "\n",
              "surface_of_the_plot_of_land : " + self.surface_of_the_plot_of_land + "\n",
              "number_of_facades : " + self.number_of_facades + "\n",
              "swimming_pool : " + self.swimming_pool + "\n",
              "state_of_the_building : " + self.state_of_the_building + "\n",
              "construction_year : " + str(self.construction_year) + "\n")


url = ""


def scrap_scrip(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    # We only retrieve the content of the script tag
    al = []
    for p in soup.html.find_all():
        for n in p:
            if n.name == "script":
                al.append(str(n))

    # Données JSON:
    x = al[0]

    x = x.replace("<script>", "")
    x = x.replace("window.dataLayer = [", "")
    x = x.replace("];", "")
    x = x.replace("</script>", "")
    x = ' '.join(x.split())

    # parse x:
    y = json.loads(x)

    # récupération des informations présentent dans le premier script :

    une_maison = House()

    une_maison.type_of_property = y["classified"]["type"]
    if y["classified"]["subtype"]:
        une_maison.subtype_of_property = y["classified"]["subtype"]
    else:
        une_maison.subtype_of_property = None
    une_maison.price = y["classified"]["price"]
    une_maison.type_of_sale = y["classified"]["transactionType"]
    une_maison.locality = y["classified"]["zip"]
    if y["classified"]["kitchen"]["type"]:
        une_maison.fully_equipped_kitchen = str(1)
    else:
        une_maison.fully_equipped_kitchen = str(0)
    if y["classified"]["building"]["constructionYear"]:
        une_maison.construction_year = y["classified"]["building"]["constructionYear"]
    else:
        une_maison.construction_year = str(None)
    if y["classified"]["building"]["condition"]:
        une_maison.state_of_the_building = y["classified"]["building"]["condition"]
    else:
        une_maison.state_of_the_building = str(None)
    une_maison.number_of_rooms = y["classified"]["bedroom"]["count"]
    une_maison.surface_of_the_land = y["classified"]["land"]["surface"]
    if y["classified"]["outdoor"]["garden"]["surface"]:
        une_maison.garden_area = y["classified"]["outdoor"]["garden"]["surface"]
    else:
        une_maison.garden_area = str(None)
    if y["classified"]["outdoor"]["terrace"]["exists"]:
        une_maison.terrace = str(1)
    else:
        une_maison.terrace = str(0)
    if y["classified"]["wellnessEquipment"]["hasSwimmingPool"]:
        une_maison.swimming_pool = str(1)
    else:
        une_maison.swimming_pool = str(0)

    # récupération des informations présentent dans le second script :
    x = al[len(al) - 1]

    x = x.replace("<script type=\"text/javascript\">", "")
    x = x.replace("window.classified = ", "")
    x = x.replace(";", "")
    x = x.replace("</script>", "")
    x = x.replace("True", "\"True\"")

    x = ' '.join(x.split())

    y = json.loads(x)

    une_maison.house_area = str(y["property"]["netHabitableSurface"])

    if y["property"]["hasTerrace"]:
        une_maison.terrace = str(1)
    else:
        une_maison.terrace = str(0)
    if une_maison.terrace == str(1):
        une_maison.terrace_area = str(y["property"]["terraceSurface"])
    else:
        une_maison.terrace_area = str(None)
    une_maison.number_of_facades = str(y["property"]["building"]["facadeCount"])
    if y["property"]["hasSwimmingPool"]:
        une_maison.swimming_pool = str(1)
    else:
        une_maison.swimming_pool = str(0)
    if y["property"]["fireplaceExists"]:
        une_maison.open_fire = str(1)
    else:
        une_maison.open_fire = str(0)
    if y["property"]["hasGarden"]:
        une_maison.garden = str(1)
    else:
        une_maison.garden = str(0)

    return une_maison


def scrap_all_page():

    nbr_run = 1
    with open('final_link_list.csv', "r") as f:
        liste_url_intermediare = f.read()
        liste_url = liste_url_intermediare.split("\n")

        for i in range(1, len(liste_url)):
            print(nbr_run)
            nbr_run += 1
            try:

                maison = scrap_scrip(liste_url[i])
                maison.save_to_csv().start()


            except:
                with open('link_error.csv', 'a',
                          newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([url])
                continue


def create_csv():
    with open('house_detail.csv', 'w',
              newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["locality", "type_of_property", "subtype_of_property", "price", "type_of_sale",
                         "number_of_rooms", "house_area", "fully_equipped_kitchen", "furnished", "open_fire",
                         "terrace", "terrace_area", "garden", "garden_area", "surface_of_the_land",
                         "surface_of_the_plot_of_land", "number_of_facades", "swimming_pool",
                         "state_of_the_building", "construction_year"])


create_csv()
scrap1 = Thread(target=scrap_all_page())
scrap1.start()
