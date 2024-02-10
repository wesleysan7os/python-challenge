from .hooks.utils import (salve_contact, show_contacts, update_contact, 
                          ask_for_contact_info, remove_contact, check_as_favorite,
                          uncheck_as_favorite)

print("Bem vindo ao seu gerenciador de Agenda!")

phone_book = []

while True:
    userInput = input("Digite uma das opções a seguir:")
    print("0. Salvar novo contato")
    print("1. Editar contato")
    print("2. Remover contato")
    print("3. Marcar contato como favorito")
    print("4. Desmarcar contato como favorito")
    print("5. Visualizar lista de contatos")
    print("6. Encerrar")

    match userInput:
        case "0":
            contact = ask_for_contact_info()
            salve_contact(phone_book, contact)

        case "1":
            contact_index = input("Digite o indice do contato que voce deseja atualizar:")
            show_contacts(phone_book)
            if contact_index:
                contact = ask_for_contact_info()
                update_contact(phone_book, contact, contact_index)

        case "2":
            contact_index = input("Digite o indice do contato que voce deseja remover:")
            show_contacts(phone_book)
            remove_contact(phone_book, contact_index)

        case "3":
            contact_index = input("Digite o indice do contato que voce deseja favoritar:")
            show_contacts(phone_book)
            check_as_favorite(phone_book, contact_index)

        case "4":
            contact_index = input("Digite o indice do contato que voce deseja desfavoritar:")
            show_contacts(phone_book)
            uncheck_as_favorite(phone_book, contact_index)

        case "5":
            show_contacts(phone_book)

        case "6":
            break
        case _:
            print("Entrada inválida, tente novamente.\n")
