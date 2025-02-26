import random

class Personaje:
    def __init__(self, region, weapon, element, model_Type, quality):
        self.region = region
        self.weapon = weapon
        self.element = element
        self.model_Type = model_Type
        self.quality = quality


Albedo = Personaje('Mondstadt', 'Sword', 'Geo', 'Male', '5' )
Alhaitham = Personaje('Sumeru', 'Sword', 'Dendro', 'Male', '5')
Aloy = Personaje('None', 'Bow', 'Cryo', 'Female', '5')
Amber = Personaje('Mondstadt', 'Bow', 'Pyro', 'Female', '4')
Arattaki_Itto = Personaje('Inazuma', 'Claymore', 'Geo', 'Male', '5')
Arlecchino = Personaje('Fontaine', 'Polearm', 'Pyro', 'Female', '5')
Baizhu = Personaje('Liyue', 'Catalyst', 'Dendro', 'Male', '5')
Barbara = Personaje('Mondstadt', 'Catalyst', 'Hydro', 'Female', '4')
Beidou = Personaje('Liyue', 'Claymore', 'Electro', 'Female', '4')
Bennett = Personaje('Mondstadt', 'Swords', 'Pyro', 'Male', '4')
Candace = Personaje('Sumeru', 'Polearm', 'Hydro', 'Female', '4')
Charlote = Personaje('Fontaine', 'Catalyst', 'Cryo', 'Female', '4')
Chevereuse =  Personaje('Fontaine', 'Polearm', 'Pyro','Female', '4')
Chiori = Personaje('Inazuma', 'Sword', 'Geo', 'Female', '5')
Chongyun = Personaje('Liyue', 'Claymore', 'Cryo', 'Male', '4')
Clorinde = Personaje('Fontaine', 'Sword', 'Electro', 'Female', '5')
Collei = Personaje('Sumeru', 'Bow', 'Dendro', 'Female', '4')
Cyno = Personaje('Sumeru', 'Polearm', 'Electro', 'Male', '5')
Dehya = Personaje('Sumeru', 'Claymore', 'Pyro', 'Female', '5')
Diluc = Personaje('Mondstadt', 'Claymore', 'Pyro', 'Male', '5')
Diona = Personaje('Mondstadt', 'Bow', 'Cryo', 'Female', '4')
Diori = Personaje('Sumeru', 'Claymore', 'Electro', 'Female', '4')
Eula = Personaje('Mondstadt', 'Claymore', 'Cryo', 'Female', '5')
Faruzan = Personaje('Sumeru', 'Bow', 'Anemo', 'Female', '4')
Fischl = Personaje('Mondstadt', 'Bow', 'Electro', 'Female', '4')
Freminet = Personaje('Fontaine', 'Claymore', 'Cryo', 'Male', '4')
Furina = Personaje('Fontaine', 'Sword', 'Hydro', 'Female', '5')
Gaming = Personaje('Liyue', 'Claymore', 'Pyro', 'Male', '4')
Ganyu = Personaje('Liyue', 'Bow', 'Cryo', 'Female', '5')
Gorou = Personaje('Inazuma', 'Bow', 'Geo', 'Male', '4')
Hu_Tao = Personaje('Liyue', 'Polearm', 'Pyro', 'Female', '5')
Jean = Personaje('Mondstadt', 'Sword', 'Anemo', 'Female', '5')
Kaedehara_Kazuha = Personaje('Inazuma', 'Sword', 'Anemo','Male', '5')
Kaeya = Personaje('Mondstadt', 'Sword', 'Cryo', 'Male', '4')
Kamisato_Ayaka = Personaje("Inazuma", 'Sword', 'Cryo', 'Female', '5')
Kamisato_Ayato = Personaje('Inazuma', 'Sword', 'Hydro', 'Male', '5')
Kaveh = Personaje('Sumeru', 'Claymore', 'Dendro', 'Male', '4')
Keqing = Personaje('Liyue', 'Sword', 'Electro', 'Female', '5')
Kirara = Personaje('Inazuma', 'Sword', 'Dendro', 'Female', '4')
Klee = Personaje('Mondstadt', 'Catalyst', 'Pyro', 'Female', '5')
Kujou_Sara = Personaje('Inazuma', 'Bow', 'Electro', 'Female', '4')
Kuki_Shinobu = Personaje('Inazuma', 'Sword', 'Electro', 'Female', '4')
Laila = Personaje('Sumeru', 'Sword', 'Cryo', 'Female', '4')
Lisa = Personaje('Mondstadt', 'Catalyst', 'Electro', 'Female', '4')
Lynette = Personaje('Fontaine', 'Sword', 'Anemo', 'Female', '4')
Lyney = Personaje('Fontaine', 'Bow', 'Pyro', 'Male', '5')
Mika = Personaje('Mondstadt', 'Polearm', 'Cryo', 'Male', '4')
Mona = Personaje('Mondstadt', 'Catalyst', 'Hydro', 'Female', '5')
Nahida = Personaje('Sumeru', 'Catalyst', 'Dendro', 'Female', '5')
Navia = Personaje('Fontaine', 'Claymore', 'Geo', 'Female', '5')
Neuvillette = Personaje('Fontaine', 'Catalyst', 'Hydro', 'Male', '5')
Nilou = Personaje('Sumeru', 'Sword', 'Hydro', 'Female', '5')
Ningguang = Personaje('Liyue', 'Catalyst', 'Geo', 'Female', '4')
Noelle = Personaje('Mondstadt', 'Claymore', 'Geo', 'Female', '4')
Qiqi = Personaje('Liyue', 'Sword', 'Cryo', 'Female', '5')
Raiden_Shogun = Personaje('Inazuma', 'Polearm', 'Electro', 'Female', '5')
Razor = Personaje('Mondstadt', 'Claymore', 'Electro', 'Male', '4')
Rosaria = Personaje('Mondstadt', 'Polearm', "Cryo", 'Female', '4')
Sangonomiya_Kokomi = Personaje('Inazuma', 'Catalyst', 'Hydro', 'Female', '5')
Sayu = Personaje('Inazuma', 'Claymore', 'Anemo', 'Female', '4')
Sethos = Personaje('Sumeru', 'Bow', 'Electro', 'Male', '4')
Shenhe = Personaje('Liyue', 'Polearm', 'Cryo', 'Female', '5')
Shikanoin_Heizou = Personaje('Inazuma', 'Catalyst', 'Anemo', 'Male', '4')
Sigewinne = Personaje('Fontaine', 'Bow', 'Hydro', 'Female', '5')
Sucrose = Personaje('Mondstadt', 'Catalyst', 'Anemo', 'Female', '4')
Tartaglia = Personaje('Snezhnaya', 'Bow', 'Hydro', 'Male', '5')
Thoma = Personaje('Inazuma', 'Polearm', 'Pyro', 'Male', '4')
Tighnari = Personaje('Sumeru', 'Bow', 'Dendro', 'Male', '5')
Traveler = Personaje('None', 'Sword', 'All', 'Both', '5')
Venti = Personaje('Mondstadt', 'Bow', 'Anemo', 'Male', '5')
Wanderer = Personaje('Inazuma', 'Catalyst', 'Anemo', 'Male', '5')
Wriothesley = Personaje('Fontaine', 'Catalyst', 'Cryo', 'Male', '5')
Xiangling = Personaje('Liyue', 'Polearm', 'Pyro', 'Female', '4')
Xianyun = Personaje('Liyue', 'Catalyst', 'Anemo', 'Female', '5')
Xiao = Personaje('Liyue', 'Polearm', 'Anemo', 'Male', '5')
Xingqiu = Personaje('Liyue', 'Sword', 'Hydro', 'Male', '4')
Xinyan = Personaje('Liyue', 'Claymore', 'Pyro', 'Female', '4')
Yae_Miko = Personaje('Inazuma', 'Catalyst', 'Electro', 'Female', '5')
Yanfei = Personaje('Liyue', 'Catalyst', 'Pyro', 'Female', '4')
Yaoyao = Personaje('Liyue', 'Polearm', 'Dendro', 'Female', '4')
Yelan = Personaje('Liyue', 'Bow', 'Hydro','Female', '5')
Yoimiya = Personaje('Inazuma', 'Bow', 'Pyro', 'Female', '5')
Yun_Jin = Personaje('Liyue', 'Polearm', 'Geo', 'Female', '4')
Zhongli = Personaje('Liyue', 'Polearm', 'Geo', 'Male', '5')

Personajes_List = [Albedo, Alhaitham, Aloy, Amber, Arattaki_Itto, Arlecchino, Baizhu, Barbara, Beidou, Bennett, Candace, Charlote, Chevereuse, Chiori, Chongyun, Clorinde,
Collei, Cyno, Dehya, Diluc, Diona, Diori, Eula, Faruzan, Fischl, Freminet, Furina, Gaming, Ganyu, Gorou, Hu_Tao, Jean, Kaedehara_Kazuha, Kaeya, Kamisato_Ayaka, Kamisato_Ayato,
Kaveh, Keqing, Kirara, Klee, Kujou_Sara, Kuki_Shinobu, Laila, Lisa, Lynette, Lyney, Mika, Mona, Nahida, Navia, Neuvillette, Nilou, Ningguang, Noelle, Qiqi, Raiden_Shogun, Razor,
Rosaria, Sangonomiya_Kokomi, Sayu, Sethos, Shenhe, Shikanoin_Heizou, Sigewinne, Sucrose, Tartaglia, Thoma, Tighnari, Traveler, Venti, Wanderer, Wriothesley, Xiangling, Xianyun, Xiao, Xingqiu,
Xinyan, Yae_Miko, Yanfei, Yaoyao, Yelan, Yoimiya, Yun_Jin, Zhongli]

winstreak = 0

while True:

    print("""
        Presione 1 para jugar
        Presione 2 para dejar de jugar """)

    jugar = int(input())

    if jugar == 1:
        print('--------------------------------------------------------------------------------------------')
        print(f"llevas una racha de {winstreak} victorias")
        print(" ")

        Pj_random = random.randrange(0,83)
        k=0
        vidas = 5
        win = False

        # bucle que se repite 5 veces 
        while vidas !=0:

            # bucle hasta que el jugador escoga un personaje existente
            while k==0:

                Personaje_Elegido = input("Escribe un personaje: ")
                print(" ")
                i = 100

                # todos los personajes estan en una lista, despues de que el juagador escriba el nombre de un personaje
                # se guarda en una variable 'i' el numero de la posicion en la que esta el personaje en la lista
                match Personaje_Elegido:


                    case "Albedo":
                        i = 0
                        k = 1
                    case "Alhaitham":
                        i = 1
                        k = 1
                    case "Aloy":
                        i = 2
                        k = 1
                    case "Amber":
                        i = 3
                        k = 1
                    case "Arattaki Itto":
                        i = 4
                        k = 1
                    case "Arlecchino":
                        i = 5
                        k = 1
                    case "Baizhu":
                        i = 6
                        k = 1
                    case "Barbara":
                        i = 7
                        k = 1
                    case "Beidou":
                        i = 8
                        k = 1
                    case "Bennett":
                        i = 9
                        k = 1
                    case "Candace":
                        i = 10
                        k = 1
                    case "Charlote":
                        i = 11
                        k = 1
                    case "Chevereuse":
                        i = 12
                        k = 1    
                    case 'Chiori':
                        i = 13
                        k =  1
                    case 'Chongyun':
                        i = 14
                        k =  1
                    case 'Clorinde':
                        i = 15
                        k =  1
                    case 'Collei':
                        i = 16
                        k =  1
                    case 'Cyno':
                        i = 17
                        k =  1
                    case 'Dehya':
                        i = 18
                        k =  1
                    case 'Diluc':
                        i = 19
                        k =  1
                    case 'Diona':
                        i = 20
                        k =  1
                    case 'Diori':
                        i = 21
                        k =  1
                    case 'Eula':
                        i = 22
                        k =  1
                    case 'Faruzan':
                        i = 23
                        k =  1
                    case 'Fischl':
                        i = 24
                        k =  1
                    case 'Freminet':
                        i = 25
                        k =  1
                    case 'Furina':
                        i = 26
                        k =  1
                    case 'Gaming':
                        i = 27
                        k =  1
                    case 'Ganyu':
                        i = 28
                        k =  1
                    case 'Gorou':
                        i = 29
                        k =  1
                    case 'Hu Tao':
                        i = 30
                        k =  1
                    case 'Jean':
                        i = 31
                        k =  1
                    case 'Kaedehara Kazuha':
                        i = 32
                        k =  1
                    case 'Kaeya':
                        i = 33
                        k =  1
                    case 'Kamisato Ayaka':
                        i = 34
                        k =  1
                    case 'Kamisato Ayato':
                        i = 35
                        k =  1
                    case 'Kaveh':
                        i = 36
                        k =  1
                    case 'Keqing':
                        i = 37
                        k =  1
                    case 'Kirara':
                        i = 38
                        k =  1
                    case 'Klee':
                        i = 39
                        k =  1    
                    case 'Kujou Sara':
                        i = 40
                        k =  1
                    case 'Kuki Shinobu':
                        i = 41
                        k =  1
                    case 'Laila':
                        i = 42
                        k =  1
                    case 'Lisa':
                        i = 43
                        k =  1
                    case 'Lynette':
                        i = 44
                        k =  1
                    case 'Lyney':
                        i = 45
                        k =  1
                    case 'Mika':
                        i = 46
                        k =  1
                    case 'Mona':
                        i = 47
                        k =  1
                    case 'Nahida':
                        i = 48
                        k =  1
                    case 'Navia':
                        i = 49
                        k =  1
                    case 'Neuvillette':
                        i = 50
                        k =  1
                    case 'Nilou':
                        i = 51
                        k =  1
                    case 'Ningguang':
                        i = 52
                        k =  1
                    case 'Noelle':
                        i = 53
                        k =  1
                    case 'Qiqi':
                        i = 54
                        k =  1
                    case 'Raiden Shogun':
                        i = 55
                        k =  1
                    case 'Razor':
                        i = 56
                        k =  1
                    case 'Rosaria':
                        i = 57
                        k =  1
                    case 'Sangonomiya Kokomi':
                        i = 58
                        k =  1
                    case 'Sayu':
                        i = 59
                        k =  1
                    case 'Sethos':
                        i = 60
                        k =  1
                    case 'Shenhe':
                        i = 61
                        k =  1
                    case 'Shikanoin Heizou':
                        i = 62
                        k =  1
                    case 'Sigewinne':
                        i = 63
                        k =  1
                    case 'Sucrose':
                        i = 64
                        k =  1
                    case 'Tartaglia':
                        i = 65
                        k =  1
                    case 'Thoma':
                        i = 66
                        k =  1
                    case 'Tighnari':
                        i = 67
                        k =  1
                    case 'Traveler':
                        i = 68
                        k =  1
                    case 'Venti':
                        i = 69
                        k =  1
                    case 'Wanderer':
                        i = 70
                        k =  1
                    case 'Wriothesley':
                        i = 71
                        k =  1
                    case 'Xiangling':
                        i = 72
                        k =  1
                    case 'Xianyun':
                        i = 73
                        k =  1
                    case 'Xiao':
                        i = 74
                        k =  1
                    case 'Xingqiu':
                        i = 75
                        k =  1
                    case 'Xinyan':
                        i = 76
                        k =  1
                    case 'Yae Miko':
                        i = 77
                        k =  1
                    case 'Yanfei':
                        i = 78
                        k =  1
                    case 'Yaoyao':
                        i = 79
                        k =  1
                    case 'Yelan':
                        i = 80
                        k =  1
                    case 'Yoimiya':
                        i = 81
                        k =  1
                    case 'Yun Jin':
                        i = 82
                        k =  1
                    case 'Zhongli':
                        i = 83
                        k =  1
                    case _:
                        k = 0

                if Pj_random == i:
                    win = True
                    break
            k=0
            print(Personajes_List[i].region + " " + Personajes_List[i].weapon + " " + Personajes_List[i].element + " " + Personajes_List[i].model_Type + " " + Personajes_List[i].quality)
            print("")

            if win == False:
                if Personajes_List[i].region == Personajes_List[Pj_random].region:
                    print(Personajes_List[Pj_random].region) 

                if Personajes_List[i].weapon == Personajes_List[Pj_random].weapon:
                    print(Personajes_List[Pj_random].weapon) 

                if Personajes_List[i].element == Personajes_List[Pj_random].element:
                    print(Personajes_List[Pj_random].element)  

                if Personajes_List[i].model_Type == Personajes_List[Pj_random].model_Type:
                    print(Personajes_List[Pj_random].model_Type) 

                if Personajes_List[i].quality == Personajes_List[Pj_random].quality:
                    print(Personajes_List[Pj_random].quality) 

            vidas = vidas -1

            if win == True:
                winstreak = winstreak + 1
                print('Has ganado')
                break

        if vidas == 0:
            print('Has perdido')

    if jugar == 2:
        break