# Feladat

A feladat egyszerű és optimális keresők programozása
**választott programozási nyelvben**.
A teszteléshez a gráfok a [`graphs.txt`](./graphs.txt) fájlban találhatóak.
A feladatot **egyénileg kell elkészíteni**, a félév során
t-próba szerűen lesz akiknek be kell mutatniuk.
Akik az előző félévben ugyanazt a feladatot adták le, kötelezően be kell mutatniuk a megoldásukat!

Implementálja és tesztelje az alábbi algoritmusokat:

-   Hegymászó keresés (Hill-climbing)
-   Legjobbat először keresés (Best-first search)
-   Nyalábkeresés (Beam search)
    -   $w = 2$
-   Elágazás és korlátozás (B&B)
    -   Mindhárom verzió
-   A\*

A programnak képesnek kell lennie a graphs.txt beolvasására és a gráf automatikus felépítésére!

# Dokumentáció

Az algoritmusok működését és a kapott eredményeket dokumentálja a
[`README.md`](./README.md) fájlban!

-   Algoritmusok ismertetése
-   Futási eredmények (útvonal, hossz)
-   Futási idő
-   Kiterjesztett csomópontok száma
