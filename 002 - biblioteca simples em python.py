class Livro:
  def __init__(self, titulo, autor, disponivel):
    self.titulo = titulo
    self.autor = autor
    self.disponivel = disponivel

  def exibir_detalhes(self):
      print(self.titulo, ",", self.autor, ", Disponível: ", self.disponivel)

class Usuario:
  def __init__(self, nome):
    self.nome = nome
    self.livros_emprestados = []

  def emprestar_livro(self, livro):
      if livro.disponivel:
        self.livros_emprestados.append(livro)
        livro.disponivel = False
        print("livro emprestado com sucesso.")
      else:
        print("o livro não está disponível.")

  def devolver_livro(self, livro):
      self.livros_emprestados.remove(livro)
      livro.disponivel = True
      print("livro devolvido com sucesso.")

class Biblioteca:
  def __init__(self, nome):
    self.nome = nome
    self.todos_livros = []

  def adicionar_livro(self, livro):
    self.todos_livros.append(livro)
    print("livro adicionado à biblioteca com sucesso")

  def exibir_livros_disponiveis(self):
    print("catálogo de livros na biblioteca:")
    for livro in self.todos_livros:
      livro.exibir_detalhes()

livro1 = Livro("Orgulho e Preconceito", "Jane Austen", True)
livro2 = Livro("Harry Potter 1", "JK Rowling", True)
livro3 = Livro("Harry Potter 2", "JK Rowling", False)
livro4 = Livro("Harry Potter 3", "JK Rowling", False)

biblioteca = Biblioteca("Biblioteca SATC")
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)

biblioteca.exibir_livros_disponiveis()

usuario1 = Usuario("Ana")

usuario1.emprestar_livro(livro3)
usuario1.emprestar_livro(livro1)
usuario1.emprestar_livro(livro2)
usuario1.devolver_livro(livro2)

biblioteca.exibir_livros_disponiveis()
