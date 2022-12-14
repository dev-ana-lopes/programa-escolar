from time import sleep

lista = []
    
def inicializacao():
    solicitante = input('Informe seu nome: ')
    print('Olá, ' + solicitante + '. Você está no sistema Jullies Education!!')

def chamaMenu(): 
    sleep(2)
    print('\nPara o menu: \n(1) Cadastrar Aluno \n(2) Editar Aluno \n(3) Visualizar Aluno \n(4) Excluir Aluno \n(5) Sair \n')
    sleep(2)
    comando = input('Informe o digito de acesso: ')
    return int(comando)

def executaComando():
    solicitacao = chamaMenu()

    if solicitacao == 1:
        
        cadastraAluno()
        
        return print('Aluno cadastrado')
        
    elif solicitacao == 2:
        
        alteraAluno()
        
        return print('Aluno alterado')

    elif solicitacao == 3:
        
        visualizaAluno()

    elif solicitacao == 4:
        
        deletaAluno()
        
        return print('Aluno apagado')

    elif solicitacao == 5:
        
        sair() 
        
    else:
        digitoNaoEncontrado()
      
def cadastraAluno():
    crm = (input('Informe o crm: '))
    nome = input('Informe o nome: ')
    curso = input('Informe o curso: ')
    aluno = {'crm': crm, 'nome': nome, 'curso': curso}
    lista.append(aluno)

def alteraAluno():
    crm = input('Informe o crm do aluno que deseja altera: ')
    find = next(x for x in lista if x["crm"] == crm)
    index = lista.index(find)
    nome = input('Informe o nome: ')
    curso = input('Informe o curso: ')
    lista[index] = {"nome": nome, "curso": curso}
    
def visualizaAluno():
    crm = input('Informe o crm do aluno que deseja visualizar: ')
    find = next(x for x in lista if x["crm"] == crm)
    print('Aluno encontrado\n')
    sleep(1)
    print(find)
    sleep(1)
    
def deletaAluno():
    crm = input('Informe o crm do aluno que deseja deletar: ')
    find = next(x for x in lista if x["crm"] == crm)
    index = lista.index(find)
    lista.pop(index)
    
def sair():
    print('Até logo...')
    return exit
 
def digitoNaoEncontrado():
    sleep(1)
    print('\nO número inserido não está de acordo com o menu. Tente Novamente!!\n')
    sleep(1)

      
if __name__ == '__main__': 
    
    inicializacao()
    
    while True:
        
        if executaComando() == exit:
            
            break
        
        else:
            executaComando()
        
        
    
    


        