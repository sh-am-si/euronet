1. Załączony zbiór danych zawiera szeregi czasowe wypłat 9 bankomatów. Szeregi podziel na cześć treningową i testową. Długość części testowej to 30 dni. Wykorzystując znane Ci metody stwórz model/-e, które zaprognozują wypłaty dla każdego urządzenia na następne 60 dni. Krótko opisz jakich modeli użyłeś(-aś) i przedstaw błąd dopasowania do danych rzeczywistych oraz błąd prognozy na części testowej. Przygotuj wykres danych historycznych i prognozy. (kod R)

Mainly I conducted the analysis of the provided data. Main results:

- Missing dates are, seemingly, the ones with zero withdrawal. (if they are filled with zeros the data may be transformed to a dataframe with columns as the ATM name and the common date index)
- There are two kinds of ATMs one seasonal (placed likely in mountain and sea resorts)
- The week seasonality is quite strong for both types


2. Opisz w jaki sposób stworzył(a)byś prognozę dla zupełnie nowych maszyn, które nie posiadają historii?

Certainly it is a very general question depending on amount of available data etc. Nevertheless, I would consider the following factors

* Some measure of people 'flow' nearby this location (transport hubs, housing etc)

* Presence of other ATMs nearby

* Presence of public places where the cash may be used (restaurants etc)

3. Tabela o nazwie Atm_History zawiera następujące kolumny: Atm (nazwa bankomatu), ProcessDate (Data), Currency (Waluta), Withdrawal (Wypłata), Deposit (Wpłata). Napisz zapytanie SQL które wyświetli transakcje z ostatniego dnia dla każdego bankomatu.

```sql
CREATE TABLE "Atm_History" (Atm TEXT, ProcessDate TEXT, CURRENCY TEXT, Withdrawal INTEGER, Deposit INTEGER);

INSERT INTO Atm_History VALUES ('ATM1', '2017-02-01', 'PLN', 140, 50);
INSERT INTO Atm_History VALUES ('ATM1', '2017-02-02', 'PLN', 1140, 150);
INSERT INTO Atm_History VALUES ('ATM2', '2017-02-01', 'PLN', 1240, 250);
INSERT INTO Atm_History VALUES ('ATM2', '2017-02-02', 'PLN', 1340, 450);
INSERT INTO Atm_History VALUES ('ATM3', '2017-02-01', 'PLN', 1440, 350);

SELECT * FROM Atm_History WHERe ProcessDate = (SELECT MAX(AH.ProcessDate) FROM Atm_History AS AH);
```