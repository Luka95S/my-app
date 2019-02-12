import pck.mod1
import json

if '__main__' == __name__:

    def writeToJSONFile(path, fileName, data):
        filePathNameWext = './' + path + '/' + fileName + '.json'
        with open(filePathNameWext, 'w') as fp:
            json.dump(data, fp)

    def unos_osobe():
        osobni_pod = []
        propo = ["id", "ime", "prezime", "spol", "dob"]
        json_file = open("C:/Users/Luka/PycharmProjects/moja_app/json/lista_osoblja.json", "r", encoding="utf-8")
        data1 = json.load(json_file)
        json_file.close()
        last_id = len(data1)+1
        osobni_pod.append(last_id)
        i = 1
        while i in range(len(propo)):
            print("Unesite " + propo[i] + ": ")
            osobni_pod.append(str(input()))
            i += 1
        i = 0
        print(data1)
        local_data = {}
        local_data1 = {}
        while i in range(len(propo)):
            local_data[propo[i]] = osobni_pod[i]
            i += 1
        local_data1[last_id] = local_data
        print(local_data1)
        data1.append(local_data1)
        fileName = 'lista_osoblja'
        path = './json/'
        writeToJSONFile(path, fileName, data1)


    def unos_pacijenta():
        osobni_pod = []
        propo = ["id", "ime", "prezime", "spol", "dob"]
        json_file = open("C:/Users/Luka/PycharmProjects/moja_app/json/lista_pacijenata.json", "r", encoding="utf-8")
        data1 = json.load(json_file)
        json_file.close()
        last_id = len(data1)+1
        osobni_pod.append(last_id)
        i = 1
        while i in range(len(propo)):
            print("Unesite " + propo[i] + ": ")
            osobni_pod.append(str(input()))
            i += 1
        print(data1)
        last_id -= 1
        new_per = pck.mod1.Covjek(osobni_pod[0], osobni_pod[1], osobni_pod[2], osobni_pod[3], osobni_pod[4])
        local_data1 = {last_id: new_per.__dict__}
        print(local_data1)
        #  unos odjela kojem pripada
        #  provjeriti raspoloživost kreveta - proci kroz sobe i dodjeliti mu prvi slobodan krevet, ako ih nema vratiti F
        #
        ls_naz_od = al_pr_a_glos()
        print("Odaberite odjel unosom broja: ")
        odabir = int(input()) - 1
        osobni_pod.append(odabir)
        soba = prip_ro(odabir)
        # lista s odabirom odjela i odabirom sobe
        pr_room(soba, odabir)
        print("Odaberite sobu unosom broja: ")
        od_s = int(input()) - 1
        nek_ls = [odabir,
                  od_s]
        pri_pac_krev(osobni_pod[0], nek_ls)
        data1.append(local_data1)
        fileName = 'lista_pacijenata'
        path = './json/'
        writeToJSONFile(path, fileName, data1)


    def pri_pac_krev(idx, podatak):
        json_file = open("C:/Users/Luka/PycharmProjects/moja_app/json/bed_list.json", "r", encoding="utf-8")
        glos_ro_bed = json.load(json_file)
        json_file.close()
        i, j = 0, 0
        for elem in glos_ro_bed:
            if i == podatak[0]:
                for un_elem in elem:
                    if j == podatak[1]:
                        for br_k in un_elem:
                            lista_kr_id = [list(br_k.values())]
                            lista_kr_ky = [list(br_k.keys())]
                            if lista_kr_id[0][0] == 0:
                                br_k[lista_kr_ky[0][0]] = idx
                            pass
                    else:
                        j += 1
            else:
                i += 1
        fileNameb = 'bed_list'
        path = './json/'
        writeToJSONFile(path, fileNameb, glos_ro_bed)

    def unos_pretraga(id, lista):
        print("Unesite naziv dodatne pretrage: ")
        naz_pret = input(str())
        print("\nUnesite naziv bolesti za koju dodajete pretragu: ")
        naz_bol = input(str())
        podaci = {"ime": naz_pret, "naziv_bol": naz_bol}
        dic = {"id": id, "podaci": podaci}
        lista.append(dic)


    def make_list_of_per(lista):
        list_per = []
        full_lst_per = []
        for one in lista:
            list_per[one][0] = pck.mod1.Covjek(lista[0], lista[1], lista[2], lista[3])
            obj_for_lst = [one, list_per[one][0]]
            full_lst_per.append(obj_for_lst)
        return full_lst_per


    def ispisi_pretrage_pac(pac, lista):
        j = 1
        for i in lista:
            ind = i[j].id
            if ind == pac:
                for key, value in i[2].items():
                    print(key + " " + str(value))


    def print_list(lista):
        for ele in lista:
            print(ele)

    def pr_osob():
        json_file = open("C:/Users/Luka/PycharmProjects/moja_app/json/lista_osoblja.json", "r",
                         encoding="utf-8")  # učitavanje liste - metoda
        lista = json.load(json_file)
        json_file.close()
        dic_val = []
        lis_val = []
        dic_key = []
        lis_key = []
        li_osoblja = []
        for i in range(len(lista)):
            dic_val.append(list(lista[i].values()))
            dic_key.append(list(lista[i].values()))
        for i in range(len(dic_val)):
            lis_val.append(list(dic_val[i][0].values()))
        lis_key.append(list(dic_val[0][0].keys()))
        for i in range(len(dic_val)):
            stri_osoba = ''
            for j in range(0, 3):
                stri_osoba += " " + str((lis_val[i][j]))
            li_osoblja.append(stri_osoba)
        for elem in li_osoblja:
            print(elem)
        
    def ch_in(var):
        if var == 'da':
            return True
        elif var == 'ne':
            return False
        elif var == 'Ne':
            return False
        elif var == 'NE':
            return False
        elif var == 'DA':
            return True
        elif var == 'Da':
            return True
        else:
            print("Pogrešan unos! Ponovite! ")
            var = input()
            ch_in(var)

    def unos_odjela():
        # odjel - id, naziv, broj soba, broj kreveta u svakoj sobi
        odjel = {"id": int, "naziv": str, "br_soba": int}
        json_file = open("C:/Users/Luka/PycharmProjects/moja_app/json/glosbe_list.json", "r", encoding="utf-8")
        data = json.load(json_file)
        json_file.close()
        ls_ind = len(data)
        odjel["id"] = ls_ind
        lst_key = list(odjel.keys())
        for idx in range(len(odjel) - 1):
            print("Unesite " + lst_key[idx + 1] + " odjela: ")
            lokalna = input()
            odjel[lst_key[idx + 1]] = lokalna
        lst_val = list(odjel.values())
        new_glos = pck.mod1.Glosbe(lst_val[1], lst_val[2])
        loc_data = {ls_ind: new_glos.__dict__}
        data.append(loc_data)
        fileName = 'glosbe_list'
        path = './json/'
        writeToJSONFile(path, fileName, data)
        en_room(ls_ind, lst_val[2])

    def en_room(id_od, nb_ro):
        json_file = open("C:/Users/Luka/PycharmProjects/moja_app/json/room_list.json", "r", encoding="utf-8")
        data2 = json.load(json_file)
        json_file.close()
        loc_roms = []
        json_file = open("C:/Users/Luka/PycharmProjects/moja_app/json/bed_list.json", "r", encoding="utf-8")
        glos_ro_bed = json.load(json_file)
        json_file.close()
        ro_bed = []
        for i in range(int(nb_ro)):
            loc = en_bed(i, ro_bed)
            loc_roms.append(loc[0])
        loc_data2 = {id_od: loc_roms}
        data2.append(loc_data2)
        glos_ro_bed.append(loc[1])
        fileNameb = 'bed_list'
        path = './json/'
        writeToJSONFile(path, fileNameb, glos_ro_bed)
        fileName = 'room_list'
        path = './json/'
        writeToJSONFile(path, fileName, data2)

    def en_bed(id, ro_bed):
        print("Unesite broj kreveta " + str(id + 1) + " sobe: ")
        br_bed = int(input())
        new_room = pck.mod1.Room(id + 1)
        loc_krev = []
        for i in range(br_bed):
            new_room.add_beds(i + 1)
        for krev in new_room.beds:
            loc_krev.append(put_bed_in_ls(krev))
        ro_bed.append(loc_krev)
        lista_sob_krev = []
        loc_ro = {id: new_room.__dict__}
        lista_sob_krev.append(loc_ro)
        lista_sob_krev.append(ro_bed)
        return lista_sob_krev

    def put_bed_in_ls(idx):
        new_bed = pck.mod1.Bed(idx)
        return new_bed.bed

    def conv(lista):
        co_el = []
        for elem in lista:
            for unu_elem in elem:
                unu_elem = int(unu_elem)
                co_el.append(unu_elem)
        return co_el

    def pr_a_glos():
        json_file = open("C:/Users/Luka/PycharmProjects/moja_app/json/glosbe_list.json", "r",
                         encoding="utf-8")
        data = json.load(json_file)
        json_file.close()
        n_dic = []
        l_val = []
        n_key = []
        ls_glosbe = []
        i = 0
        for ele in data:
            n_dic.append(list(ele.values()))
            n_key.append(list(ele.keys()))
            l_val.append((list(n_dic[i][0].values())))
            i += 1
        for i in range(len(n_key)):
            strin = str(int(n_key[i][0]) + 1) + " " + str(l_val[i][0])
            ls_glosbe.append(strin)
        for i in ls_glosbe:
            print(i)
        return n_key

    def al_pr_a_glos():
        json_file = open("C:/Users/Luka/PycharmProjects/moja_app/json/glosbe_list.json", "r",
                         encoding="utf-8")
        data = json.load(json_file)
        json_file.close()
        n_dic = []
        l_val = []
        n_key = []
        ls_glosbe = []
        naz_odj = []
        i = 0
        for ele in data:
            n_dic.append(list(ele.values()))
            n_key.append(list(ele.keys()))
            l_val.append((list(n_dic[i][0].values())))
            i += 1
        for i in range(len(n_key)):
            strin = str(int(n_key[i][0]) + 1) + " " + str(l_val[i][0])
            ls_glosbe.append(strin)
            naz_odj.append(l_val[i][0])
        for i in ls_glosbe:
            print(i)
        return naz_odj

    def pr_glos(idx_glos):
        json_file = open("C:/Users/Luka/PycharmProjects/moja_app/json/glosbe_list.json", "r",
                         encoding="utf-8")
        data = json.load(json_file)
        json_file.close()
        idx_glos -= 1
        n_dic = []
        l_val = []
        i = 0
        for ele in data:
            n_dic.append(list(ele.values()))
            l_val.append((list(n_dic[i][0].values())))
            i += 1
        print("Odabrali ste " + l_val[idx_glos][0])
        return l_val[idx_glos][0]
        #  može se i napraviti u prošloj fun. da vraća listu naziva
        #  odjela i onda se samo preda ta lista i ispise naziv pod idx

    def al_pr_glos(idx_glos, ls_naz_gl):
        print("Odabrali ste " + ls_naz_gl[idx_glos-1])

    def prip_ro(select_gl):  # takes argument and gives back rooms for that glosbe
        json_file = open("C:/Users/Luka/PycharmProjects/moja_app/json/room_list.json", "r",
                         encoding="utf-8")
        data = json.load(json_file)
        json_file.close()
        select_gl -= 1
        l_b_i = []
        l_k_a = []
        for elem in data:
            ls_key = []
            var = list(elem.keys())
            if int(var[0]) == select_gl:
                for un_elem in elem.values():
                    ls_bed_nb = []
                    for i in range(len(un_elem)):
                        ls_key.append(list(un_elem[i].keys()))  # dodavanje broja sobe
                        for nes_elem in un_elem[i].values():
                            ls_bed_nb.append(nes_elem["beds"])# dodavanje liste kreveta za tu sobu
                    l_b_i.append(ls_bed_nb)  # dodavanje liste kreveta unutar liste, za zadani odjel
                konv = conv(ls_key)  # pretvaranje stringa u int
                l_k_a.append(konv)
                ls_brRm_i_nBe = [l_k_a,
                                 l_b_i]  # stvaranje liste koja sadrzi brojeve soba na odjela i brojeve kreveta od svake sobe
        return ls_brRm_i_nBe



    def pr_room(ls_ro, gl_nb):
        for elem in ls_ro[0][gl_nb]:
            print(elem + 1)

    def pri_sobe(lista):
        lok = lista[0]
        lok1 =[]
        for i in range(len(lok[0])):
            lok1.append(lok[0][i]+1)
        for br_sobe in lok1:
            print(br_sobe)

    def pri_krev(lista, odabir):
        lok = lista[1]
        for i in lok:
            if (i-1) == odabir:
                for j in lok[i]:
                    print(lok[i][j])


    def pr_krev(lista_lista):
        # učitati json od pacijenata
        # izvuči listu kreveta pod indexom sobe
        # provjeriti pacijente u toj sobi i ispisati ih zajedno s njihovim indexom


    print("Dobro došao u medicinski dnevnik\nOdaberite broj:")
    prv_izb = int
    select = int
    lista_oso = []
    lista_pac = []
    lista_pret = []
    lista_kreveta = []
    active = '1'
    while active == '1':
        while select != 1:
            prv_izb = int(input("1. Rad \n2. Unos \n3. Pregled\n"));
            if ((prv_izb <= 3) & (prv_izb >= 1)) | (prv_izb == 111):
                if prv_izb == 1:
                    print("Dobrodošli u rad! \n")
                    select = 1
                    print("Predstavite se odabirom rednog broja: \n")
                    pr_osob()
                    odg_osoba = int(input())
                    print("\nUnesite šifru: ")
                    odg_osoba_pass = int(input())
                    if odg_osoba == odg_osoba_pass:
                        #  pr_a_glos()
                        ls_naz_od = al_pr_a_glos()
                        print("Odaberite odjel unosom broja: ")
                        odabir = int(input())
                        al_pr_glos(odabir, ls_naz_od)
                        # glos_name = pr_glos(odabir)
                        soba = prip_ro(odabir)
                        print("Odaberite broj sobe na odjelu u kojoj se nalazi pacijent: ")
                        lista_brsob_i_krevetasob = prip_ro(odabir)
                        pri_sobe(lista_brsob_i_krevetasob)
                        #  print soba na odjelu
                        od_s = int(input()) - 1
                        print("Odaberite pacijenta unosom broja njegovog kreveta: ")
                        pr_krev(lista_brsob_i_krevetasob)
                        #  print kreveta
                        #ispis sobe
                            # ispisati sobe na odjelu, omogućiti odabir
                                #  ispisati pacijente koji se nalaze u toj sobi s rednim brojem kreveta
                                #  omogućiti odabir kreveta - zapravo tako se odabire pacijent te dolaze njegove
                                #  pretrage na ispis     negdje gore uvesti odabir dnevne pretrage (jutro, podne, vecer)
                        #  for i in lista_odjela:
                        #     print(naziv odjela)
                        #  select odjela
                    else:
                        print("Neispravna lozinka! Ponovite unos.")

                elif prv_izb == 2:
                    print("Dobrodošli u unos podataka")
                    select = 1
                    izb_unosa = "da"
                    while izb_unosa == "da":
                        print(
                            "Odaberite unos: \n1 - Unos osoblja\n2 - Unos pacijenata\n3 - Unos dodatnih pretraga\nZa povratak na prijašnji izbornik unesite 'nazad'\n")
                        izb_un_unosa = input()
                        if izb_un_unosa == '1':  # unos osoblja za rad
                            select = "da"
                            while select == "da":
                                unos_osobe()
                                print("Želite li dodati drugu osobu? ")
                                select = input()
                        elif izb_un_unosa == '2':  # unos pacijenata
                            select = 'da'
                            while select == "da":
                                unu_select = "da"
                                while unu_select == "da":
                                    unos_pacijenta()
                                    print("Želite li dodati drugu osobu? ")
                                    unu_select = input()
                                    if unu_select == "ne":
                                        select = "ne"
                        elif izb_un_unosa == '3':  # unos posebnih pretraga
                            select = "da"
                            while select == "da":
                                unos_pretraga(lista_pret)
                                # pozivanje metode za unos pretraga(korišteno u početku
                                #  za dodavanje pretraga u lokalnoj pohrani). Jedna od značajki koje treba dovršiti
                                print("Želite li dodati drugu pretragu? ")
                                select = input()
                        elif izb_un_unosa == "nazad":  # izlaz iz unosa
                            izb_unosa = 'ne'
                        else:
                            print("Pogrešan unos! Ponovite! ")  # neispravan unos, ponavljanje
                elif prv_izb == 3:
                    select = 1
                    while select == 1:
                        print("Dobrodošli u pregled podataka\n Unesite broj ispred načina na koji želite pretraziti "
                              "pacijente:\n1 Odjel\soba \n2 Id pacijenta")
                        unos_nacina = int(input())
                        if unos_nacina == 1:
                            active_pre = 1
                            while active_pre == 1:
                                # ispis odjela
                                print("Unesite broj odjela u kojom se nalazi pacijent")
                                od_odjela = int(input())
                                # ispis soba
                                print("Unesite broj sobe u kojoj se nalazi pacijent")
                                broj_pret_sob = int(input())
                                # ispis pacijenata unutar sobe
                                print("Unesite index pacijenta za kojeg zelite provjeriti pretrage: ")
                                broj_p_pac = int(input())
                                #
                                # ispisi_pretrage_pac(broj_p_pac)
                                print("Za izlazak - ne \nZa ponovnu pretragu - da\n")
                                ponovi = input()
                                if ponovi == "ne":
                                    select = 0
                                    active_pre = 0
                                # for broj,j in lista_pac:
                                #     if broj[j] == broj_pret_sob:
                                #         print(broj.puno_ime())
                        elif unos_nacina == 2:
                            active_pre = 1
                            while active_pre == 1:
                                # napraviti metodu koja učitava lista_pac.json te ispisati id i pacijenta
                                print(
                                    "\nUnesite id pacijenta čiju statistiku želite pregledati. ")  # 31predavanje za dic print
                                broj_pret_pac = int(input())
                                ispisi_pretrage_pac(broj_pret_pac, lista_pac)
                                print("Za izlazak - ne \nZa ponovnu pretragu - da\n")
                                ponovi = input()
                                if ponovi == "ne":
                                    select = 0
                                    active_pre = 0
                        else:
                            print("Pogrešan unos! Ponovite ")
                elif prv_izb == 111:
                    print("Dobrodošli u administratorsko sučelje!\nOdaberite redni broj:\n"
                          "1.Dodavanje odjela\n2.Dodavanje soba\n3.Dodavanje kreveta\n"
                          "4.Dodavanje bolesti\n5.Dodavanje osnovnih pretraga")
                    izb_adm = int(input())
                    if izb_adm == 1:
                        un_var = True
                        while un_var:
                            unos_odjela()
                            print("želite li nastaviti s unosom odjela? ")
                            x = input()
                            un_var = ch_in(x)
                    elif izb_adm == 2:
                        pass
                    elif izb_adm == 3:
                        pass
                    elif izb_adm == 4:
                        pass
                    elif izb_adm == 5:
                        pass
            else:
                print("Pogrešan unos, molim Vas ponovite")
