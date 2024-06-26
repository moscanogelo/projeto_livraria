from service.menu_service import MenuService
from dao.editora_dao import EditoraDAO
from model.editora import Editora


class EditoraService(MenuService):
    def __init__(self):
        self.__editora_dao: EditoraDAO = EditoraDAO()

    @property
    def editora_dao(self) -> EditoraDAO:
        return self.__editora_dao

    def listar(self):
        print('\nListando editoras...')

        try:
            editoras = self.__editora_dao.listar()
            if len(editoras) == 0:
                print('Nenhuma editora encontrada!')

            for editora in editoras:
                print(editora)
        except Exception as e:
            print(f'Erro ao exibir as editoras! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('\nAdicionando editora...')

        try:
            id = self.__editora_dao.ultimo_id() + 1
            nome = input('Digite o nome da editora: ')
            endereco = input('Digite o endereço da editora: ')
            telefone = input('Digite o telefone da editora: ')
            nova_editora = Editora(id, nome, endereco, telefone)

            self.__editora_dao.adicionar(nova_editora)
            print('Editora adicionada com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir editora! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def remover(self):
        print('\nRemovendo editora...')

        try:
            editora_id = int(input('Digite o ID da excluir para excluir: '))
            if (self.__editora_dao.remover(editora_id)):
                print('Editora excluída com sucesso!')
            else:
                print('Editora não encontrada!')
        except Exception as e:
            print(f'Erro ao excluir editora! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def mostrar_por_id(self):
        print('\Editora por Id...')

        try:
            id = int(input('Digite o Id da editora para buscar: '))
            edt = self.__editora_dao.buscar_por_id(id)

            if (edt == None):
                print('Editora não encontrada!')
            else:
                print(f'{edt.id} | {edt.nome} | {edt.endereco} | {edt.telefone}')
        except Exception as e:
            print(f'Erro ao exibir editora! - {e}')
            return

        input('Pressione uma tecla para continuar...')
