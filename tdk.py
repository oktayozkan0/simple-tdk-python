import requests


class TDK:
    SEARCH_URL = "https://sozluk.gov.tr/gts?ara="
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "application/json, text/javascript, */*; q=0.01",
    }
    def __init__(self) -> None:
        self.response = None
        self.kelime = None
        pass

    def _raw_search(self, kelime: str) -> dict:
        if self.response is None or self.response[0].get("madde") != kelime:
            r = requests.get(f"{self.SEARCH_URL}{kelime}", headers=self.HEADERS)
            self.kelime = kelime
            self.response = r.json()

    def anlamlar(self, kelime: str) -> dict:
        if not isinstance(kelime, str): raise TypeError("kelime must be a string.")
        self._raw_search(kelime)
        return self.response[0].get("anlamlarListe")

    def atasozu(self, kelime: str):
        if not isinstance(kelime, str): raise TypeError("kelime must be a string.")
        self._raw_search(kelime)
        return self.response[0].get("atasozu")
