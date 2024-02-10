from utils import (salve_contact, show_contacts, update_contact, 
                          ask_for_contact_info, remove_contact, check_as_favorite,
                          uncheck_as_favorite)

phone_book = []


while True:
    print("\nMenu do Gerenciador de Agenda:")
    print("1. Salvar novo contato")
    print("2. Editar contato")
    print("3. Remover contato")
    print("4. Marcar contato como favorito")
    print("5. Desmarcar contato como favorito")
    print("6. Visualizar lista de contatos")
    print("7. Encerrar")

    userInput = input("\nDigite a sua escolha: ")

    match userInput:
        case "1":
            contact = ask_for_contact_info()
            salve_contact(phone_book, contact)

        case "2":
            contact_index = input("Digite o indice do contato que voce deseja atualizar: ")
            show_contacts(phone_book)
            if contact_index:
                contact = ask_for_contact_info()
                update_contact(phone_book, contact, contact_index)

        case "3":
            contact_index = input("Digite o indice do contato que voce deseja remover: ")
            show_contacts(phone_book)
            remove_contact(phone_book, contact_index)

        case "4":
            contact_index = input("Digite o indice do contato que voce deseja favoritar: ")
            check_as_favorite(phone_book, contact_index)

        case "5":
            contact_index = input("Digite o indice do contato que voce deseja desfavoritar: ")
            uncheck_as_favorite(phone_book, contact_index)

        case "6":
            show_contacts(phone_book)

        case "7":
            break
        case _:
            print("\nEntrada inválida, tente novamente.\n")
