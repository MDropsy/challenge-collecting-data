import csv


class House:
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
        """Constructor our class"""
        self.locality = "rty"
        self.type_of_property = "z"
        self.subtype_of_property = "e"
        self.price = "r"
        self.type_of_sale = "t"
        self.number_of_rooms = "y"
        self.area = "u"
        self.fully_equipped_kitchen = "i"
        self.furnished = "o"
        self.open_fire = "p"
        self.terrace = "q"
        self.terrace_area = "s"
        self.garden = "d"
        self.garden_area = "f"
        self.surface_of_the_land = "g"
        self.surface_of_the_plot_of_land = "h"
        self.number_of_facades = "j"
        self.swimming_pool = "k"
        self.state_of_the_building = "l"

    # permet de rajouter des données au fichier CSV

    def save_to_csv(self):
        fields = ['first', 'second', 'third']
        with open('innovators.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.locality, self.type_of_property, self.subtype_of_property, self.price,
                             self.type_of_sale, self.number_of_rooms, self.area, self.fully_equipped_kitchen,
                             self.furnished, self.open_fire, self.terrace, self.terrace_area, self.garden,
                             self.garden_area, self.surface_of_the_land, self.surface_of_the_plot_of_land,
                             self.number_of_facades, self.swimming_pool, self.state_of_the_building])

    # permet de creer le fichier CSV (avec les en-tête)

    def create_csv(self):
        with open('innovators.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["locality", "type_of_property", "subtype_of_property", "price", "type_of_sale",
                             "number_of_rooms", "area", "fully_equipped_kitchen", "furnished", "open_fire", "terrace",
                             "terrace_area", "garden", "garden_area", "surface_of_the_land",
                             "surface_of_the_plot_of_land", "number_of_facades", "swimming_pool",
                             "state_of_the_building"])
            writer.writerow([self.locality, self.type_of_property, self.subtype_of_property, self.price,
                             self.type_of_sale, self.number_of_rooms, self.area, self.fully_equipped_kitchen,
                             self.furnished, self.open_fire, self.terrace, self.terrace_area, self.garden,
                             self.garden_area, self.surface_of_the_land, self.surface_of_the_plot_of_land,
                             self.number_of_facades, self.swimming_pool, self.state_of_the_building])
