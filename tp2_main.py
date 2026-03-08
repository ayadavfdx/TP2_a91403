from gestor_stock import GestorStock
from graph import show_graph
from colorama import Fore,init
init()

def main():
    
    stock= GestorStock("AAPL","Apple",130,8)
    print(stock)

    stock.comprar(10,100)
    print(f"{Fore.RED}\nAfter buying: ")
    print(stock)

    stock.vender(3,220)
    print(f"{Fore.RED}\nAfter selling: ")
    print(stock)

    stock.receber_dividendo(2.9)
    print(f"{Fore.RED}\nAfter dividend: ")
    print(stock)

    show_graph(stock.simbolo)
if __name__ == "__main__":
    main()