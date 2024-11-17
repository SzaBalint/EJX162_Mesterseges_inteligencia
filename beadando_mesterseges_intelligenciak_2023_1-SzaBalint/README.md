[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/B-yYWhOU)
# Mesterséges Intelligenciák I. beadandó feladat

Név: Szabó Bálint \
Neptun: EJX162 \
Használt programozási nyelv: Python

## Algoritmusok bemutatása

### DFS
Miután felépítettük a gráfot, inicializálunk egy várólistát. Ez egy útvonalakból álló sor. A startot a sorba tesszük. Amíg van valami a sorban, addig vesszük az első elemet, kivesszük a sorból, és ellenőrizzük, hogy eléri-e a célt. Ha elértük 
G, kilépünk. Ellenkező esetben fogjuk a szomszédait, és hozzáadjuk őket a listához. A Depth-first algoritmus esetében pedig e sor hátuljához adjuk hozzá. Ezt addig folytatjuk, amíg meg nem találjuk a célt, vagy ki nem merítjük a várólistát.
### BFS
A Breadth-first algoritmus esetében minden elemet előre helyezünk, amíg meg nem találjuk a célt, vagy ki nem merítjük a várólistát.
### HC
Mindegyik csomópontot megvizsgálja és a heurisztikai távolságokat figyelembevéve terjeszti ki a csomópontokat.
### Beam

### Best-first

### B&B

#### Lista
A csomópontokat egy listában tárolja és ha mégegyszer előfordul a csomópont azt már nem vizsgálja az algoritmus.
#### Heurisztika
Vizsgálj a csomópontokhoz rendelt heuriszikai távolságot és ezeket vizsgálva halad végig a csomópontokon.
### A\*
Az A* algoritmus az B&B w. extended list és a B&B w. heuristic algoritmus együtteséből épül fel. Így azokat felhasználva kapjuk meg az A* algoritmushoz tartozó útvonalat.
## Futási eredmények
Graph 3 futási eredmények

| Algoritmus   | Útvonal | Futási idő (mp) | Kiterjesztések száma |
|:-------------|:--------|:---------------:|:--------------------:|
| DFS          |  SZWG   |       0         |          3           |
| BFS          |  SXWG   |       0         |          7           |
| HC           |  SYWG   |       0         |          7           |
| Beam         |         |                 |                      |
| Best-first   |         |                 |                      |
| B&B          |  SXWG   |       0         |          8           |
| B&B w. List  |  SXWG   |       0         |          7           |
| B&B w. Heur. |  SZWG   |       0         |          7           |
| A*           |  SYWG   |       0         |          6           |

## Megoldás részletei

Megoldással töltött idő: kb. 20 óra \
Mi volt nehéz: Branch and Bound algoritmus. \
Mi volt érdekes: Pythonban való ismeretek bővítése. \
Mi volt unalmas: - \
Vélemény: Sokkat kellett vele foglalkozni, hogy a megfelelő útvonalakat adják vissza az algoritmusok és a megfelelő sorrendben vizsgálja gráfokat.
