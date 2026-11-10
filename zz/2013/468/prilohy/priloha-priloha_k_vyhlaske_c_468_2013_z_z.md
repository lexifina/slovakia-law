Príloha k vyhláške č. 468/2013 Z. z.

- 1. ![vzorec 01](../assets/2b073394a79329cbf58f82d3b43b35df1dad481fc4fe5372050e570231cf5abe.png)

- 2. ![vzorec 02](../assets/12f8a2d632fd098ef801790610cd3c6fd9c951d92b5bb11040535b8ca2a7020f.png)

- 3. ![vzorec 03](../assets/89c959c4f79d83cfb524898580dd3ce3e117af18a37072fede93594160220594.png)

- Index „i“ označuje názov zvukového kanálu (R - pravý, L - ľavý, C - stredný, Ls - ľavý zadný, Rs - pravý zadný).

- Koeficienty Gi nadobúdajú hodnoty: G<sub>L</sub> = G<sub>R</sub>= G<sub>C</sub> = 1 a G<sub>Ls</sub> = G<sub>Rs</sub> = 1,41.

- Veličina zij je energia zvukového signálu definovaná ako:

- ![vzorec 04](../assets/f3fcadde39c221677b8cd8cfbfcdfb1f6a3f27be98f0f40fe97899485739885f.png) .

- Index „j“ čísluje jednotlivé časové úseky zvukových signálov yi(t), z ktorých sa počítajú príslušné hodnoty z<sub>ij</sub>. Každý časový úsek má dĺžku Tg = 400 ms. Index „j“ nadobúda postupne celočíselné hodnoty od 0 až do hodnoty indexu posledného časového úseku Tg, ktorý ešte celý obsahuje zvukové signály yi(t).

- Hodnoty energií z<sub>ij</sub> sa počítajú zo signálov y<sub>j</sub>(t) od času t = Tg.j.krok do času t = Tg.(j.krok+1). Hodnota konštanty krok je: krok = 0,25. V čase po sebe nasledujúce hodnoty z<sub>ij</sub> sa teda určujú z navzájom prekrývajúcich sa časových intervalov dĺžky Tg postupne časovo posunutých o 100 ms.

- Zvukové signály yi(t) sa získavajú zo vstupných zvukových signálov x<sub>i</sub>(t) ich filtráciou cez tzv. K-filtre. Modulová frekvenčná charakteristika K-filtra má takýto priebeh:

- ![obrázok](../assets/393845333a1ddc671a118b61c370747313a4d942622c90b47150f8fe79c5c5df.png)

- Modulová frekvenčná charakteristika K-filtra

- Množina indexov J<sub>gr</sub> obsahuje len tie indexy „j“, pri ktorých hodnota hladiny hlasitosti l<sub>j</sub> presiahla hodnotu prahovacej hladiny hlasitosti Γ<sub>r</sub>. Hodnota lj je definovaná ako:

- ![vzorec 05](../assets/d71bc9a2bb83e91592a79ff0055cd677ce50c7a1e22d467291021c6c5397b371.png) [LUFS].

- Prahovacia hodnota hlasitosti Γr je definovaná ako:

- ![vzorec 06](../assets/26cf45daaf9f0deb4c8366d032363056f287bd61b0e67e08022473f328a4308d.png) [LUFS].

- Množina indexov J<sub>ga</sub> obsahuje len tie indexy „j“, pri ktorých hodnota hladiny hlasitosti l<sub>j</sub> presiahla hodnotu prahovacej hladiny hlasitosti Γ<sub>a</sub>. Hodnota Γ<sub>a</sub> je: Γ<sub>a</sub> = –70 LUFS.
