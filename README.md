# Percurso das ações

## Quando aplicada a edição do Canvas:
BackBuffer -> FrontBuffer -> GLFW_BackBuffer -> GLFW_FrontBuffer
BackBuffer commita para FrontBuffer, o qual é usado como matriz de pixels base para as operaçãoes do GLFW/display gráfico.
## Quando cancelada a edição do Canvas:
BackBuffer -> clear()

# Como rodar
A partir da pasta de maior hierarquia, rode pyhton src/main.py


# Observação
Ainda não me organizei quanto as dependências, o código não está nem perto de finalizado. Oque se tem até o momento, é o esqueleto da interface gráfica, mas os eventos aplicados sobre a mesma ainda não estão sendo gerenciados ou aplicados de forma ideal.
