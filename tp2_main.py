from gestor_stock import GestorStock
from graph import show_graph
from colorama import Fore, Style,init
init()

def main():
    
    stock= GestorStock("AAPL","Apple",130,8)
    print(stock)

    stock.comprar(10,100)
    print(f"{Fore.RED}\nAfter buying: ")
    print(stock)

if __name__ == "__main__":
    main()