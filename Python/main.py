def introducao():
    # Função apenas para introducao do programa, organiza as falas iniciais
    print("------------------ Feed th Future ------------------")
    print("Temos o objetivo de combater a fome através de agricultura sustentável e melhor distribuição de alimentos")
    print()


def pf_ou_pj():
    # Função para perguntar se o usuário é Pessoa Física ou Jurídica, enquanto não digitar uma opção válida (1 ou 2) não sai da função
    # Retorna uma string "PF" ou "PJ" com base na resposta do usuário
    tipo_pessoa=0
    while tipo_pessoa not in range(1,3):
        tipo_pessoa = int(input("Agora nos diga, você é Pessoa Física ou Pessoa Jurídica? Digite:"
              "\n1- PF\n2- PJ\n"))

    return "PF"  if tipo_pessoa==1 else "PJ"

def cadastro(tipo_pessoa):
    # Função para realizar o cadastro do usuário, precisa de um parâmetro string que espera "PF" ou "PJ" retorno da função pf_ou_pj()
    # Retorna uma lista de variáveis com dados digitados pelo usuário (nome, documento_identificacao, cep, email, telefone)
    if tipo_pessoa == "PF":
        nome = input("Digite o seu nome: ")
        documento_identificacao = input("Digite seu CPF (apenas números): ")
    else:
        nome = input("Digite o nome da empresa: ")
        documento_identificacao = input("Digite o CNPJ (apenas números): ")

    cep = input("Digite o CEP (apenas números): ")
    email = input("Digite o email para contato: ")
    telefone = input("Digite um telefone para contato (apenas números): ")
    print(f"Perfeito {nome}, cadastro realizado!")
    return nome, documento_identificacao, cep, email, telefone

def doacao():
    # Função que faz o procedimento de doação do projeto, utiliza no seu escopo a função pf_ou_pj() e cadastro()
    print("Que ótima notícia, você quer ajudar no combate a fome!")
    tipo_pessoa = pf_ou_pj()
    dados_cadastro = cadastro(tipo_pessoa)
    print(f"{dados_cadastro[0]}, você irá receber um email em {dados_cadastro[3]} com a unidade mais próxima para doar. O mundo agradeçe!")
    print("E fique sabendo que todos os produtos doados para a Feed the Future são 100% doados ao próximo!!!")

def vender():
    # Função que faz o procedimento de venda do projeto, utiliza no seu escopo a função pf_ou_pj() e cadastro()
    print("Que bom saber que você entrou em contato com a gente.\nVendas na Feed the Future funcionam da seguinte maneira, produtos em boas condições que "
          "seriam jogados fora ou estão perto da data de validade podem ser vendidos para nós a um preço baixo (já que seriam jogados fora) e com isso nós "
          "podemos alcançar pessoas com necessidade através desses produtos. Todos saem ganhando!")
    tipo_pessoa = pf_ou_pj()
    dados_cadastro = cadastro(tipo_pessoa)
    print(f"{dados_cadastro[0]}, você irá receber um email em {dados_cadastro[3]} com mais informações de venda. O mundo agradeçe!")
    print("A Feed the Future não tem objetivo de fins lucrativos, os seus produtos seão revendidos a um preço acessível, apenas com uma taxa a mais para arcar com o frete")


def combater_fome():
    # Função que lista as opções disponíveis para ajudar no combate a fome, não sai da função até que o usuário digite uma opção válida (1 ou 2)
    acao = 0
    while acao not in range(1, 3):
        acao = int(input("Como você quer contribuir com o combate a fome? Digite:"
                         "\n1 - Doar"
                         "\n2 - Vender\n"))
    if acao == 1:
        doacao()
    else:
        vender()


def sobre_nos():
    # Função que apenas imprime as informações sobre o projeto Feed the Future
    print("A partir de doações ou vendas de produtos, nossa missão como o grupo Feed The Future é acabar com a fome nacional e internacionalmente. "
          "Nosso serviço servirá como uma junção de ONG \ninternacional (com voluntários, patrocínios, ações governamentais e claro, com tecnologia "
          "envolvida em todas as etapas) e inteligência artificial")
    print()
    print("Nosso sistema permite participar pessoas físicas ou jurídicas (que representam mercados, marcas, FastFood, Hortifrúti e afins)."
          "Caso represente uma pessoa jurídica, suas possibilidades \nserão vender alimentos intocados que foram feitos a mais do que foi necessário "
          "e seriam jogados fora e desperdiçados no final do dia por um preço abaixo do mercado. \nA Inteligência Artificial irá classificar "
          "localidades mais próximas da empresa ao pedir o CEP e \nfica a critério deles se querem contratar uma equipe própria para levar "
          "até o local ou se preferem que nossos voluntários façam isso.")
    print()
    print("Caso represente pessoa física e quiser doar alimentos dentro do prazo de validade, a inteligência artificial lhe mostrará a partir do seu "
          "CEP, uma de nossas unidades mais próxima de sua localização, \nassim, você pode escolher entre ir até o local ou se quiser, um de nossos "
          "voluntários, irá até sua casa pegar os alimentos e levar para a doação")
    print()
    print("Em ambos os casos, se os alimentos doados forem fora do prazo de validade, iremos converter eles em fertilizante que será doado para "
          "pequenos produtores para uso local, ajudando \nerradicar a fome garantindo alimentos a todos a partir das doações de comidas ou futuros "
          "fertilizantes promovendo a agricultura sustentável \npara pequenos produtores melhorarem seus resultados e sua distribuição e, "
          "principalmente a eliminação total do desperdício e redução da desigualdade.")
    print()
    print("Isso é só um pouco sobre a Feed the Future! Caso queira saber mais você pode visitar o nosso site:"
          "\nwww.google.com"
          "\nOu caso queira dar sugestões, críticas ou melhorias, entre em contato: gs.feedthefuture@gmail.com")


def sobre_agricultura():
    # Função que apenas imprime as informações sobre agricultura sustentável
    print("------ Agricultura Sustentável ------")
    print("O QUE É AGRICULTURA SUSTENTÁVEL?\n"
          "Agricultura sustentável é aquela que respeita o meio ambiente, é justa do ponto de vista social e consegue ser \neconomicamente viável. A agricultura para ser "
          "considerada sustentável deve garantir, às \ngerações futuras, a capacidade de suprir as necessidades de produção e qualidade de vida no planeta.")
    print()

    print("PRINCIPAIS CARACTERÍSTICAS:\n"
          "- Diminuição no uso de agrotóxicos\n"
          "- Uso de técnicas em que não ocorra a poluição do ar, do solo e da água\n"
          "- Prática de agricultura organica\n"
          "- Não desmatamento de florestas para o cultivo\n"
          "- Uso equilibrado ou eliminado do uso de pesticidas que podem prejudicar o solo e a saúde dos consumidores\n"
          "- Adoção do Sistema de lantio direto, que preserva a capacidade produtiva do solo. Este sistema se baseia em: não arar o solo antes do plantio, cobrir o solo com folhagens secas e fazer a rotação de cultivo\n"
          "- Valorização da agricultura familiar que gera trabalho e renda às famílias rurais, possibilitando suas permanências no campo\n")
    print()

    print("QUAL O OBJETIVO DA AGRICULTURA SUSTENTÁVEL?\n"
          "A agricultura sustentável tem a missao de cultivar alimentos sem danificar o solo, reduzir o uso de recursos \nnecessários nesse processo, como a água, além de "
          "estar inserida na luta no alcança da equidade social e econômica")
    print()

    print("COMO AGRICULTURA SUSTENTÁVEL PODE NOS AJUDAR NO COMBATE CONTRA A FOME?\n"
          "Utilizando o modelo de plantio sustentável, o adaptando a demanda de produção necessária e seguindo a maneira \ncorreta de distribuiçao com base na fome, é possível "
          "unir o cuidado com os solos ao combate contra a fome, resultando na oferta de \nalimentos saudáveis livres de agrotóxicos aos que mais necessitam")
    print()
    

def sobre_IAgenereativa():
    # Função que apenas imprime as informações sobre Inteligência Artificial generativa aplicada a agricultura
    print("------ Inteligência Artificial Generativa na Agricultura ------")
    print("''A união entre a Inteligência Artificial Generativa e a agricultura sustentável abre as portas para um \nfuturo onde as colheitas são otimizadas, os recursos "
          "são utilizados de forma eficiente e com a \njusta distribuição a fome se torna um problema do passado.''")
    print()

    print("==== Colheitas Eficientes e Sustentáveis ====")
    print("Através da Inteligência Artificial Generativa, é possível criar modelos preditivos que auxiliam os agricultores na tomada de decisões, como o momento ideal de "
          "plantio, colheita e manejo \nde pragas, resultando em uma produção agrícola mais eficiente e sustentável.")
    print()

    print("==== Simulação Avançada para Agricultura Sustentável ====")
    print("A inteligência artificial generativa na agricultura é uma ferramenta revolucionária que permite a criação de modelos de simulação avançados, capazes de prever "
          "cenários climáticos, otimizar a \ndistribuição de recursos e garantir a máxima produtividade, impulsionando assim a sustentabilidade e o combate à fome.")
    print()

    print("==== Cultivando o Futuro Verticalmente ====")
    print("A Inteligência Artificial Generativa está revolucionando a agricultura vertical ao oferecer soluções inovadoras para maximizar o potencial desse método "
          "sustentável de cultivo. Através da \nanálise de dados em tempo real e do aprendizado de máquina, a IA generativa possibilita a otimização precisa dos parâmetros "
          "ambientais, como luz, temperatura e nutrientes, \nresultando em colheitas abundantes e de alta qualidade, independentemente das limitações espaciais e climáticas.")
    print()

def menu():
    # Função que lista em forma de menu, as ações disponíveis que o usuário pode realizar. Não sai da função até que o usuário digite um valor válido (1 ou 2 ou 3 ou 4 ou 5)
    menu = 0
    while menu not in range(1,6):
        menu = int(input("Digite o número de qual seção você deseja acessar:"
                         "\n1 - Combater a fome"
                         "\n2 - Agricultura sustentável"
                         "\n3 - I.A Generativa na agriultura"
                         "\n4 - Sobre a Feed the Future"
                         "\n5 - Finalizar\n"))

    match menu:
        case 1: combater_fome()
        case 2: sobre_agricultura()
        case 3: sobre_IAgenereativa()
        case 4: sobre_nos()
        case 5: print()

# Inicialização do programa onde fica em looping até que o usuário selecione a opção de finalizar
parar = False
while parar == False:
    introducao()
    menu()
    print()
    finalizar = int(input("Digite:"
                  "\n1 - Para acessar o menu novamente"
                  "\n2 - Para finalizar\n"))

    if finalizar == 2:
        parar = True