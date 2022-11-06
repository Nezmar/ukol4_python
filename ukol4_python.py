#ukol-04: Třídy
#Deadline: 25.10.2022

#Vyberte si kterou variantu chcete, pro odvážnější jsem sepsala jen obecne požadavky třídy, atributy a metody nechávám na vás, můžete použít něco co vam přijde praktické, co vás zajímá :) Kdo se nechce zdržovat s vymášlením a chce si procvičit látku na konkretním zadání, může použít druhou variantu.

#Na úkolu si vyzkuoušejte, že umíte třídu definovat a vyvořit konkrétní objekty, experimentujte. Svoje pokusy v kódu klidně nechte i při odevzdání. Pokud budete chtít něco vytvořit ale nevíte jak, jestli na to jdete dobře, nebo prostě chcete jen sdílet nápad, napiště na slack

#Obecné požadavky na úkol (vyžaduje více času a vlastní iniciativy)
#Existuji alespoň dvě různé třídy z toho každá má:
#alespoň 3 atributy (nemusí být všechny jako argumenty v __init__)
#alespoň 3 metody + init (nebo může být i dataclass)
#Na konci souboru je ukázka použití tříd a metod



#Vymyšlené zadání
#Uvažuj že vytváříš kuchařku a potřebuješ uložit několik receptů. Vytvoř dvě třídy Recept a Kucharka (idealne v tomto poradi).

#1. Recept
#Bude mít 3 atributy:

#nazev - string, jmeno kucharky
#narocnost - necham na vas jak ji budete reprezentovat (muze byt cislo, muze byt slovni vyjadreni)
#url_adresa - string, odkaz na recept
#vyzkouseno - bool, metoda __init__ ji vzdy nastavi na False
#nazev,narocnost, url_adresa budou atributy metody __init__, tedy uzivatel si je muze zvolit pri vytvareni objektu.

#A bude mít také 3 metody:

#__str___(self)
#vraci hezky vypis receptu (necham na vas ktere atributy chcete do vypisu dat)
#zmen_narocnost(self, nova_hodnota)
#zmeni narocnost, tedy zmeni atribut narocnost na nova_hodnota
#zkusit(self)
#zmeni atribut vyzkouseno na True
#2. Kucharka

#_______________________________________________________________________________________________



#Vymyšlené zadání
#Uvažuj že vytváříš kuchařku a potřebuješ uložit několik receptů. Vytvoř dvě třídy Recept a Kucharka (idealne v tomto poradi).

#1. Recept
#Bude mít 3 atributy:

#nazev - string, jmeno kucharky
#narocnost - necham na vas jak ji budete reprezentovat (muze byt cislo, muze byt slovni vyjadreni)
#url_adresa - string, odkaz na recept
#vyzkouseno - bool, metoda __init__ ji vzdy nastavi na False
#nazev,narocnost, url_adresa budou atributy metody __init__, tedy uzivatel si je muze zvolit pri vytvareni objektu.


class Recept:
    
    def __init__(self, nazev_receptu:str, narocnost_receptu: int, URL_adresa:str):
     self.nazev_receptu = nazev_receptu
     self.narocnost_receptu = narocnost_receptu
     self.URL_adresa = URL_adresa
     
    def __str__(self):
       return f'Recept {self.nazev_receptu} najdete na sdrese {self.URL_adresa} Náročnost receptu {self.narocnost_receptu}'
        
muj_recept = Recept('Bábovka', 5, 'www.recepty.cz')

print(muj_recept.nazev_receptu)
print(muj_recept.narocnost_receptu)
print(muj_recept.URL_adresa)

class Kucharka(Recept):
    def __init__(self, nazev_receptu, narocnost_receptu, URL_adresa, vyzkouseno):
        super().__init__(nazev_receptu,narocnost_receptu, URL_adresa)
        self.vyzkouseno = vyzkouseno
       
bábovka = Kucharka('Bábovka', 4,'www.recepty.cz', True)


def recepty(self,  vyzkouseno):
        if  vyzkouseno == self.vyzkouseno:
            
            return f'{self.vyzkouseno} jedná se o osvědčený recept.'
        
        else:
           
            return f'{self.vyzkouseno} nikdo neochutnal'
        
recept_z_kucharky = Kucharka('Bábovka', 4, 'www.recepty.cz', True)
        
        
print(f' Recept byl vyzkoušen = {recept_z_kucharky.vyzkouseno}')
        
        
        


