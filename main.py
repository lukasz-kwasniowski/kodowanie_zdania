class Szyfr:
    def __init__(self):
        self.kodowanie = []
        self.zmiana = []
        self.zdanie_zaszyfrowane = ""
        self.czy_wyjsc = True

    def podanie_szyfru(self):
        self.zdanie = input("Podaj zdanie do zakodowania: ")
        self.szyfr = int(input("Podaj wartość szyfru (int): "))
        self.zakodowanie()

    def zakodowanie(self):
        for i in self.zdanie:
            self.kodowanie.append(ord(i)+self.szyfr)
        self.zmiana_na_ascii()

    def zmiana_na_ascii(self):
        for i in range(len(self.kodowanie)):
            self.zmiana.append(chr(self.kodowanie[i]))
        for i in self.zmiana:
            self.zdanie_zaszyfrowane += i

    def wyswietlanie(self):
        print("Twoje zdanie po zaszyfrowaniu to: " + self.zdanie_zaszyfrowane)

    def wyjscie(self):
        self.czy_wyjsc = False

    def menu(self):
        print("Witaj w aplikacji kodowanie! :D")
        print("MENU:")
        while(self.czy_wyjsc != False):
            print("1. Podanie zdania i zakodowanie; 2. Wyswielenie szyfru; 3. Zakończ program")
            self.wybor = int(input(">>> "))
            if (self.wybor == 1):
                self.podanie_szyfru()

            if (self.wybor == 2 ):
                self.wyswietlanie()

            if (self.wybor == 3):
                self.wyjscie()
            if (self.wybor != 1 and self.wybor != 2 and self.wybor != 3):
                print("ZLE DANE")

z1 = Szyfr()

z1.menu()
