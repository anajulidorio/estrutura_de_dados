class Produto:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

class Carrinho:
  def __init__(self): #é vazio porque quando entramos no carrinho de uma loja, ele não tem nada dentro
    self.lista_produtos = []

  def adicionar_produto(self, produto):
    self.lista_produtos.append(produto)

  def remover_produto(self, produto):
    self.lista_produtos.remove(produto)

  def calcular_total(self):
    total = 0
    for p in self.lista_produtos:
      total += p.preco
    return total

p1 = Produto("Ar condicionado", 2499.00)
p2 = Produto("Lava e Seca (Samsung)", 3499.00)
p3 = Produto("Microondas", 450.00)
p4 = Produto("PS5", 3999.00)

carrinho_site = Carrinho()
carrinho_site.adicionar_produto(p1)
carrinho_site.adicionar_produto(p2)
carrinho_site.adicionar_produto(p3)
carrinho_site.adicionar_produto(p4)

print("Total da compra: ", carrinho_site.calcular_total())

carrinho_site.remover_produto(p4)

print("Agora a compra deu: ", carrinho_site.calcular_total())
