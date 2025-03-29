import random
from characters_class import Personaje
from characters_data import Personajes_List
winstreak = 0

while True:

    print("""
          
        Write 1 to play
        Write anything else to stop playing """)

    jugar = int(input())

    if jugar == 1:
        print('--------------------------------------------------------------------------------------------')
        print(f"You have a streak of {winstreak} wins\n")
    
        personaje = random.randrange(0,len(Personajes_List))
        
        
        vidas = 5
        win = False

        # bucle que se repite 5 veces 
        while vidas !=0:

            i=100000
            while i>len(Personajes_List):
                Personaje_Elegido = input("Write a character: ")
                print(" ")
                i=0
                for elem in Personajes_List:
                    if elem.name == Personaje_Elegido:
                        break
                    else:
                        i = i + 1


            Region_El = Personajes_List[i].region
            Weapon_El = Personajes_List[i].weapon
            Element_El = Personajes_List[i].element
            ModelType_El = Personajes_List[i].model_Type
            Quality_El = Personajes_List[i].quality

            if Personajes_List[personaje].name == Personaje_Elegido:
                win = True
                print(Personajes_List[personaje].region + " " + Personajes_List[personaje].weapon + " " 
                      + Personajes_List[personaje].element + " " + Personajes_List[personaje].model_Type + " " 
                      + Personajes_List[personaje].quality + "\n")
                
                winstreak = winstreak + 1
                print('You won!')
                break

            else:
                print("your character features: ")
                print(Region_El + " " + Weapon_El + " " + Element_El + " " +
                       ModelType_El + " " + Quality_El + "\n")
                print("matching fetures: ")
                if Region_El == Personajes_List[personaje].region:
                    print(Personajes_List[personaje].region) 

                if Weapon_El == Personajes_List[personaje].weapon:
                    print(Personajes_List[personaje].weapon) 

                if Element_El == Personajes_List[personaje].element:
                    print(Personajes_List[personaje].element)  

                if ModelType_El == Personajes_List[personaje].model_Type:
                    print(Personajes_List[personaje].model_Type) 

                if Quality_El == Personajes_List[personaje].quality:
                    print(Personajes_List[personaje].quality) 
                print(" ")
                vidas = vidas - 1

        if vidas == 0:
            print('You lose :(')
            winstreak=0

    else:
        break
