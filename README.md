# Percurso das ações

## Quando aplicada a edição do Canvas:
BackBuffer -> FrontBuffer -> GLFW_BackBuffer -> GLFW_FrontBuffer
BackBuffer commita para FrontBuffer, o qual é usado como matriz de pixels base para as operaçãoes do GLFW/display gráfico.
## Quando cancelada a edição do Canvas:
BackBuffer -> clear()
