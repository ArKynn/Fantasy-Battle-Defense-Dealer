# ***Fantasy-Battle-Defense-Dealer***
## **Projeto Realizado por:**

### Daniel Fernandes (a22202501) e David Mendes (a22203255)

1. *Daniel Fernandes* (a22202501)
     - dthreshold
     - d10_and_end_game
     - Recipe
     - Participação no Items_and_Inventory
     - Markdown
2. *David Mendes* (a22203255)
     - Main_and_Pygame_ui
     - Items_and_Inventory
     - BuyCraftandSell
------------------------------    
## **Desenvolvimento**


## O projeto é constituído por vários ficheiros:
- O ficheiro principal é o “Main_and_Pygame_ui.py” onde se definem a mecânica e exibição gráfica do jogo usando o engine pygame. Inclui também o código da execução das fases jogo:
    - Execução (Days) 
        - Resource Buying
        - Crafting
        - Selling
            - Player Setting Prices
            - Client Buying
     
- O ficheiro “Items_and_Inventory” (importa de outro ficheiro (class): “recipe”) contém as classes dos itens (armas, armaduras e materiais) e define as respetivas caracteristicas, tipos, quantidades e outras propriedades. Também contém as caracteristicas das diferentes receitas necessárias para crafting das armas e armaduras. Contém ainda a classe do inventário do jogador;
- O ficheiro “Recipe” define a classe recipe;
- O ficheiro “BuyCraftandSell” é onde estão definidas as funções de compra, construção e venda de items;
- O ficheiro “d10_and_end_game” contém a definição de uma função que simula o lançamento de um dado de 10 faces, a função que define o fim do jogo;
- O ficheiro “dthreshold” contém a definição da função onde é determinado o threshold da decisão de compra de um item por um cliente baseado na função quadrática.



### **Referências**
https://www.desmos.com/
-Usado para desenvolver as funções usados no cálculo do threshold
https://stackoverflow.com/questions/32486754/i-want-to-make-an-inventory-system-for-my-game-in-python-v-3-4-3
-Consultado para a construção do código do inventário
https://stackoverflow.com/questions/31899465/python-how-to-correctly-set-up-hierarchy-of-classes
-Consultado para compreensão da herança de classes
https://stackoverflow.com/questions/44998943/how-to-check-if-the-mouse-is-clicked-in-a-certain-area-pygame
-Consultado apenas para verificar se a posição do rato coincide dentro de uma área