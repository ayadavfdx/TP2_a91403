# gestor_stock.py

class GestorStock:
    """Classe que representa um gestor de carteira de uma ação específica."""

    def __init__(
            self, 
            simbolo: str, 
            nome: str, 
            preco_atual= 0.0, 
            quantidade= 0, 
            ):
        
        self.simbolo= simbolo
        self.nome= nome
        self.preco_atual= preco_atual
        self.quantidade= quantidade
        self.preco_medio_compra= preco_atual
        self.lucro_realizado= 0.0

    @property
    def simbolo(self) -> str:
        """Devolve o símbolo da ação (ex: AAPL).
        O símbolo deve ser guardado e devolvido sem espaços adicionais e em maiúsculas."""
        return self.__simbolo

    @simbolo.setter
    def simbolo(self, valor: str):
        """Define o símbolo da ação."""
        self.__simbolo= valor.upper().strip()

    @property
    def nome(self) -> str:
        """Devolve o nome da empresa.
        O nome deve ser guardado e devolvido sem espaços adicionais e com as iniciais em maiúsculas (Title Case)."""
        return self.__nome

    @nome.setter
    def nome(self, valor: str):
        """Define o nome da empresa."""
        self.__nome=valor.strip().title()

    @property
    def preco_atual(self) -> float:
        """Devolve o preço atual da ação."""
        return self.__preco_atual

    @preco_atual.setter
    def preco_atual(self, valor: float):
        """Define o preço atual da ação. Deve ser positivo.
        Se for fornecido um valor negativo ou zero, o preço é colocado a 0."""
        self.__preco_atual=valor
        if valor <=0:
            self.__preco_atual = 0
        else:
            self.__preco_atual = valor

    @property
    def quantidade(self) -> int:
        """Devolve a quantidade de ações em carteira."""
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, valor: int):
        """Define a quantidade de ações em carteira.
        Se for fornecido um valor negativo, a quantidade é colocada a 0."""
        self.__quantidade= valor
        if valor <0:
            self.__quantidade= 0
        else:
            self.__quantidade= valor

    @property
    def preco_medio_compra(self) -> float:
        """Devolve o preço médio de compra vigente de todo o stock."""
        return self.__preco_medio_compra

    @preco_medio_compra.setter
    def preco_medio_compra(self, valor: float):
        """Define o preço médio de compra."""
        self.__preco_medio_compra= valor

    @property
    def lucro_realizado(self) -> float:
        """Devolve o lucro (ou prejuízo) consolidado ao longo de todo o histórico de transações de venda e dividendos fechados."""
        return self.__lucro_realizado

    @lucro_realizado.setter
    def lucro_realizado(self, valor: float):
        """Define o lucro realizado."""
        self.__lucro_realizado=valor

    def comprar(self, quantidade: int, preco: float) -> bool:
        """Realiza uma compra de ações.
        Aumenta a quantidade em carteira, estipula o novo preço médio de compra através da média pesada, e atualiza o preço de mercado atual.
        Retorna True no sucesso e False no caso de inputs (quantidade ou preco) não serem > 0."""
        
        if preco <0 or quantidade <0:
            return False
        
        total= self.__quantidade + quantidade
        
        #media pesada ->(preco_medio_compra*self.quantidade + preco*quantidade)/total
        self.__preco_medio_compra = (self.__preco_medio_compra*self.quantidade + preco*quantidade)/total
        
        self.__quantidade= total
        self.__preco_atual= preco

        return True

    def vender(self, quantidade: int, preco: float) -> bool:
        """Realiza uma venda de ações.
        Diminui a quantidade em carteira, atualiza o preço atual, e soma a margem (lucro ou prejuízo) face ao preço_medio_compra ao histórico de lucro_realizado.
        Retorna True no sucesso e False no insucesso (seja por parâmetros errados <= 0 ou pela inexistência de posições suficientes)."""
        if preco <=0 or quantidade <=0:
            return False
        elif quantidade > self.__quantidade:
            return False

        #lucro -> (preco-self.__preco_medio_compra)*quantidade
        profit= (preco - self.__preco_medio_compra)* quantidade

        self.__lucro_realizado += profit
        self.__quantidade-= quantidade
        self.__preco_atual = preco

        return True

    def valor_total(self) -> float:
        """Calcula o valor total da posição na carteira (quantidade * preço_atual)."""
        return self.__quantidade*self.__preco_atual

    def lucro_potencial(self) -> float:
        """Apurar rentabilidade não realizada ao valor de cotação presente.
        Diferença entre a avaliação do ativo aos preços de hoje, e a avaliação ao preço que foi comprado."""
        
        #lucro_potencial -> (self.__preco_actual-self.__preco_medio_compra)*self.quantidade
        potential_profit= (self.__preco_atual-self.__preco_medio_compra)*self.quantidade
        return potential_profit
    
    def receber_dividendo(self, dividendo_por_acao: float) -> float:
        """Apurar dividendos totais com o número de ações em posse, adicionando diretamente ao lucro_realizado da posição.
        Retorna o fundo depositado (que será 0.0 se for passado um valor inválido <= 0)."""
        if dividendo_por_acao <=0:
            return 0.0

        #receber_dividendo -> self.__quantidade * dividendo_por_acao
        total_dividend= self.__quantidade * dividendo_por_acao
        self.lucro_realizado += total_dividend

        return total_dividend
    

