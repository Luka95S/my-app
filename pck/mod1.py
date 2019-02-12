class Covjek:
    def __init__(self, oz, name, surname, sex, dob):
        self.id = oz
        self.name = name
        self.surname = surname
        self.sex = sex
        self.dob = dob

    def full_name(self):
        return str(self.id) + ". " + str(self.name) + " " + str(self.surname)

class Glosbe:
    def __init__(self, name, ro_nb):
        self.name = name
        self.rooms_nb = ro_nb


class Room:  # creating room for
        def __init__(self, nb_ro):
            self.id = nb_ro
            self.beds = []

        def add_beds(self, bed_nb):
            self.beds.append(bed_nb)


class Bed:  # creating bed in room for patient
    def __init__(self, id):
        self.bed = {}
        self.bed_id = id
        self.id_pac = 0
        self.bed[self.bed_id] = self.id_pac

    @classmethod
    def add_pac_in(cls, bed, id_paca):  # fulling bed, new patient
        bed["bed_id"] = id_paca
        return bed

    @classmethod 
    def empty_bed(cls, bed):  # emptying bed because patient is released
        bed["bed_id"] = 0
        return bed

class Search:
    def __init__(self):
        self.pret = {}
    
    @classmethod
    def init_pret(self):  # initializing searches for patient
        self.pret = {}
        self.pret["temperatura"] = 0.0
        self.pret["tlak"] = 0.0
        self.pret["krv"] = 0
        self.pret["urin"] = False
        self.pret["iskasljaj"] = False
        self.pret["stolica"] = False
        self.pret["boja koze"] = ""
        self.pret["promjena koze"] = False
        self.pret["ekg"] = False
        self.pret["visina"] = 0.0
        self.pret["tezina"] = 0.0
        self.pret["psi.stanje"] = 0
        self.pret["osip"] = 0
        return self.pret

    @classmethod
    def init_new_search(self, dict_sr, new_sr, sr_type):  # adding new search
        dict_sr[new_sr] = sr_type
        return dict_sr

    @classmethod
    def ch_search(self, search, idx):  # changing search value
        keys = self.pret.keys()
        self.pret[keys[idx-1]] = search
        return self.pret