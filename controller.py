import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtI, language, modality):
        txt = replaceChars(txtI)
        words = txt.split()
        paroleErrate = ""

        match modality:
            case "default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None
    def handleButton(self, e):
        temp = self.risolvi()
        self._view._output_area.controls.append(ft.Text(f"Frase: {str(self._view.textIn())}"))
        if temp[0] != "":
            self._view._output_area.controls.append(ft.Text(f"Parole Errate: {temp[0]}"))
        else:
            self._view._output_area.controls.append(ft.Text(f"La frase è stata scritta correttamente"))
        self._view._output_area.controls.append(ft.Text(f"Tempo Impiegato: {temp[1]} sec"))
        self._view.__textIn = ""
        self._view.update()

    def risolvi(self):
        testo = self._view.textIn()
        lingua = self._view.tendina()
        modality = self._view.type()
        temp = self.handleSentence(testo, lingua, modality)
        return temp

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = str(text).replace(c, "")
    return text