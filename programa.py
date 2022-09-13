from time import sleep

cadastroAlunos = []

def incializacao():
    nome = input('informe seu nome: ')
    return nome

def chamaMenu(): 
    solicitante = incializacao
    print('Olá, ' + solicitante + '. Você está no sistema Jullies Education!! \n\nPara o menu: \n(1) Cadastrar Aluno \n(2) Editar Aluno \n(3) Visualizar Aluno \n(4) Excluir Aluno \n(5) Sair \n')
    comando = input('Informe o digito de acesso: ')
    return comando

def executaComando():
    solicitacao = int(chamaMenu())
    
    if solicitacao == 1:

        crm = input('Informe o crm: ')
        nome = input('Informe o nome: ')
        curso = input('Informe o curso: ')
        aluno = {'crm': crm, 'nome': nome, 'curso': curso}
        #return lista.append(aluno,)
        
    elif solicitacao == 2:
        pass
    elif solicitacao == 3:
        pass
    elif solicitacao == 4:
        pass
    elif solicitacao == 5:
        print('Até logo...')
    else:
        sleep(1)
        print('\nO número inserido não está de acordo com o menu. Tente Novamente!!\n')
        sleep(1)
        chamaMenu()
    
if __name__ == '__main__': 
    
    pass
        