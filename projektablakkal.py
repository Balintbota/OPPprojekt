from abc import ABC, abstractmethod
from datetime import datetime
import tkinter as tk

class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def leiras(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=15000, szobaszam=szobaszam)
        self.foglalasok= []


    def leiras(self):
        return f"Szoba: {self.szobaszam}: Egyágyas, ára: {self.ar}$"

    def hozzaad_foglalas(self, foglalas):
        self.foglalasok.append(foglalas)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=20000, szobaszam=szobaszam)
        self.foglalasok= []

    def leiras(self):
        return f"Szoba: {self.szobaszam}: Kétágyas, ára: {self.ar}$"

    def hozzaad_foglalas(self, foglalas):
        self.foglalasok.append(foglalas)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def uj_szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def osszes_szoba_leiras(self):
        leirasok = []
        for szoba in self.szobak:
            leirasok.append(szoba.leiras())
        return leirasok

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                for foglalas in szoba.foglalasok:
                    if foglalas.datum == datum:
                        return szoba.ar
                return None
            return None

    def foglalas_lemondasa(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                for foglalas in szoba.foglalasok:
                    if foglalas.datum == datum:
                        szoba.foglalasok.remove(foglalas)
                        return True
                return False
        return False

    def osszes_foglalas_listazasa(self):
        foglalasok = []
        for szoba in self.szobak:
            foglalasok.extend(szoba.foglalasok)
        return foglalasok

    def keres_szoba(self, szobaszam):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba
        return None


szalloda = Szalloda(" ")

print(f"Üdvözöljük a Bálint Luxusszállójában. Itt láthatja a szobafelhozatalunkat: ")
for leiras in szalloda.osszes_szoba_leiras():
    print(leiras)


egyagyas = EgyagyasSzoba("101")
egyagyas2 = EgyagyasSzoba("102")
ketagyas = KetagyasSzoba("201")
ketagyas2 = KetagyasSzoba("202")
ketagyas3 = KetagyasSzoba("203")


print(egyagyas.leiras())
print(egyagyas2.leiras())
print(ketagyas.leiras())
print(ketagyas2.leiras())
print(ketagyas3.leiras())


class Foglalás:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def __str__(self):
        return f"{self.szoba.szobaszam} szoba foglalva {self.datum.strftime('%Y-%m-%d')} napra"

def foglalas_szobara(szalloda):
    szobaszam = input("Adja meg a szobaszámot: ")
    datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")
    try:
        datum = datetime.strptime(datum_str, '%Y-%m-%d')
    except ValueError:
        print("Hibás dátumformátum. Kérjük adjon meg helyes formátumot (pl. YYYY-MM-DD).")
        return
    if datum < datetime.now():
        print("A foglalás dátuma nem lehet múltbeli.")
        return

    szoba = szalloda.keres_szoba(szobaszam)
    if szoba is None:
        print("Nincs ilyen számú szobánk.")
        return

    foglalva = False
    for foglalas in szoba.foglalasok:
        if foglalas.datum == datum:
            foglalva = True
            break

    if foglalva:
        print("A szoba már foglalt ezen a dátumon.")
    else:
        szoba.foglalasok.append(Foglalás(szoba, datum))
        print("A foglalás sikeresen létrehozva.")


def foglalas_lemondasa(szalloda):
    szobaszam = input("Adja meg a szobaszámot: ")
    datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")
    try:
        datum = datetime.strptime(datum_str, '%Y-%m-%d')
    except ValueError:
        print("Hibás dátumformátum. Kérjük adjon meg helyes formátumot (pl. YYYY-MM-DD).")
        return

    foglalas_letezik = szalloda.foglalas_lemondasa(szobaszam, datum)
    if foglalas_letezik:
        print("A foglalás sikeresen le lett mondva.")
    else:
        print("Nem található ilyen foglalás.")

def foglalasok_listazasa(szalloda):
    foglalasok_szama = 0
    for szoba in szalloda.szobak:
        foglalasok_szama += len(szoba.foglalasok)
    if foglalasok_szama == 0:
        print("Jelenleg nincsen foglalás.")
    else:
        print("Az összes foglalás:")
        for szoba in szalloda.szobak:
            for foglalas in szoba.foglalasok:
                print(foglalas)

def feltolt_szalloda():
    # Szálloda létrehozása
    szalloda = Szalloda("Bálint luxusszálloda")

    # Szobák hozzáadása
    egyagyas = EgyagyasSzoba("101")
    egyagyas2 = EgyagyasSzoba("102")
    ketagyas = KetagyasSzoba("201")
    ketagyas2 = KetagyasSzoba("202")
    ketagyas3 = KetagyasSzoba("203")


    szalloda.uj_szoba_hozzaadasa(egyagyas)
    szalloda.uj_szoba_hozzaadasa(egyagyas2)
    szalloda.uj_szoba_hozzaadasa(ketagyas)
    szalloda.uj_szoba_hozzaadasa(ketagyas2)
    szalloda.uj_szoba_hozzaadasa(ketagyas3)


    # Foglalások hozzáadása
    foglalasok = [
        Foglalás(egyagyas, datetime(2024, 5, 10)),
        Foglalás(ketagyas, datetime(2024, 5, 11)),
        Foglalás(egyagyas2, datetime(2024, 5, 14)),
        Foglalás(ketagyas3, datetime(2024, 5, 16)),
        Foglalás(ketagyas2, datetime(2024, 5, 20))
    ]

    for foglalas in foglalasok:
        foglalas.szoba.hozzaad_foglalas(foglalas)

    return szalloda

def main():
    # Szálloda feltöltése
    szalloda = feltolt_szalloda()

    while True:
        print("\nKérjük válassza ki hogy mit szeretne tenni:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Kérjük válasszon: ")

        if valasztas == "1":
            foglalas_szobara(szalloda)
        elif valasztas == "2":
            foglalas_lemondasa(szalloda)
        elif valasztas == "3":
            foglalasok_listazasa(szalloda)
        elif valasztas == "4":
            print("Köszönjük hogy minket választott :)")
            break
        else:
            print("Érvénytelen választás. Kérjük válasszon újra.")

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bálint Luxusszállodája")

        self.szalloda = feltolt_szalloda()

        # Felhasználói felület elemeinek létrehozása
        self.label_szobaszam = tk.Label(self, text="Szobaszám:")
        self.entry_szobaszam = tk.Entry(self)
        self.label_datum = tk.Label(self, text="Foglalás dátuma (YYYY-MM-DD):")
        self.entry_datum = tk.Entry(self)
        self.button_foglalas = tk.Button(self, text="Foglalás", command=self.foglalas_szobara)
        self.button_lemondas = tk.Button(self, text="Lemondás", command=self.foglalas_lemondasa)
        self.button_listazas = tk.Button(self, text="Foglalások listázása", command=self.foglalasok_listazasa)
        self.textarea = tk.Text(self, height=10, width=50)

        # Felhasználói felület elrendezése a grid elrendező segítségével
        self.label_szobaszam.grid(row=0, column=0, sticky="w")
        self.entry_szobaszam.grid(row=0, column=1)
        self.label_datum.grid(row=1, column=0, sticky="w")
        self.entry_datum.grid(row=1, column=1)
        self.button_foglalas.grid(row=2, column=0, columnspan=2)
        self.button_lemondas.grid(row=3, column=0, columnspan=2)
        self.button_listazas.grid(row=4, column=0, columnspan=2)
        self.textarea.grid(row=5, column=0, columnspan=2)

    def foglalas_szobara(self):
        szobaszam = self.entry_szobaszam.get()
        datum_str = self.entry_datum.get()
        try:
            datum = datetime.strptime(datum_str, '%Y-%m-%d')
        except ValueError:
            self.textarea.insert(tk.END, "Hibás dátumformátum. Kérjük adjon meg helyes formátumot (pl. YYYY-MM-DD).\n")
            return
        if datum < datetime.now():
            self.textarea.insert(tk.END, "A foglalás dátuma nem lehet múltbeli.\n")
            return

        szoba = self.szalloda.keres_szoba(szobaszam)
        if szoba is None:
            self.textarea.insert(tk.END, "Nincs ilyen számú szobánk.\n")
            return

        foglalva = False
        for foglalas in szoba.foglalasok:
            if foglalas.datum == datum:
                foglalva = True
                break

        if foglalva:
            self.textarea.insert(tk.END, "A szoba már foglalt ezen a dátumon.\n")
        else:
            szoba.foglalasok.append(Foglalás(szoba, datum))
            self.textarea.insert(tk.END, "A foglalás sikeresen létrehozva.\n")

    def foglalas_lemondasa(self):
        szobaszam = self.entry_szobaszam.get()
        datum_str = self.entry_datum.get()
        try:
            datum = datetime.strptime(datum_str, '%Y-%m-%d')
        except ValueError:
            self.textarea.insert(tk.END, "Hibás dátumformátum. Kérjük adjon meg helyes formátumot (pl. YYYY-MM-DD).\n")
            return

        foglalas_letezik = self.szalloda.foglalas_lemondasa(szobaszam, datum)
        if foglalas_letezik:
            self.textarea.insert(tk.END, "A foglalás sikeresen le lett mondva.\n")
        else:
            self.textarea.insert(tk.END, "Nem található ilyen foglalás.\n")

    def foglalasok_listazasa(self):
        foglalasok_szama = 0
        for szoba in self.szalloda.szobak:
            foglalasok_szama += len(szoba.foglalasok)
        if foglalasok_szama == 0:
            self.textarea.insert(tk.END, "Jelenleg nincsen foglalás.\n")
        else:
            self.textarea.insert(tk.END, "Az összes foglalás:\n")
            for szoba in self.szalloda.szobak:
                for foglalas in szoba.foglalasok:
                    self.textarea.insert(tk.END, str(foglalas) + "\n")

if __name__ == "__main__":
    app = Application()
    app.mainloop()