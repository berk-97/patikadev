# Binary Search Tree Projesi

## Proje 3
 [7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.

 Örnek: root x'dir. root'un sağından y bulunur. Solunda z bulunur vb.

---
1) Ilk eleman (7) root kabul edilerek baslanir.

2) Root'tan buyuk ilk eleman (8) bulunarak dizi ikiye bolunur ve bu eleman saga yazilir:

    [5, 1] ve [8, 3, 6, 0, 9, 4, 2]
    
                    7
                5       8

3) Ayni surec her altdizi icin devam ettirilir.

---
    [5, 1] -> root = 5, child = 1

                    7
                5       8
              1

    [8, 3, 6, 0, 9, 4, 2] -> root = 8
    Root'tan buyuk ilk eleman -> 9
    Aldiziler -> [3, 6, 0] ve [9, 4, 2]

                    7
                5       8
              1       3   9
              
    [3, 6, 0] -> root = 3

                    7
            5               8
        1               3       9
                      0   6
    [9, 4, 2] -> root = 9

                    7
            5               8
        1              3         9
                     0   6     2   4

[Bu bir patikadev projesidir.](https://www.patika.dev)
