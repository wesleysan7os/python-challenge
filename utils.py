from error_types import EmptyInputError

def salve_contact(phone_book, contact):
    try:
        __check_has_empty_inputs(contact)
    except EmptyInputError as e:
        print(e.message)
    else:
        contact["isFavorite"] = False
        phone_book.append(contact)
        print("\nContato salvo com sucesso!")

def update_contact(phone_book, contact, indice):
    try:
        __check_has_empty_inputs(contact)
    except EmptyInputError as e:
        print(e.message)
    else:
        try:
            indice = int(indice)
        except Exception as e:
            print(e)
        else:
            contact["isFavorite"] = phone_book[indice]["isFavorite"]
            phone_book[indice] = contact
            print("\nContato atualizado com sucesso!")

def remove_contact(phone_book, indice):
    try:
        indice = int(indice)
    except Exception as e:
        print(e)
    else:
        del phone_book[indice]
        print("\nContato removido com sucesso!")

def check_as_favorite(phone_book, indice):
    try:
        indice = int(indice)
    except Exception as e:
        print(e)
    else:
        phone_book[indice]["isFavorite"] = True
        print("\nContato favoritado com sucesso!")

def uncheck_as_favorite(phone_book, indice):
    try:
        indice = int(indice)
    except Exception as e:
        print(e)
    else:
        phone_book[indice]["isFavorite"] = False
        print("\nContato desfavoritado com sucesso!")

def show_contacts(phone_book):
    for index, contact in enumerate(phone_book):
        check_if_its_favorite = "✓" if contact["isFavorite"] else " "
        print(f"\n{index}. [{check_if_its_favorite}] "
            f"Nome: {contact['name']} | "
            f"Telefone: {contact['celphone']} | "
            f"Email: {contact['email']}")


def ask_for_contact_info():
    name = input("\nDigite o nome do contato: ")
    celphone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    contact = {
        "name": name,
        "celphone": celphone,
        "email": email
    }
    return contact

def __check_has_empty_inputs(contact):
    if not contact["name"] or not contact["celphone"] or not contact["email"]:
        raise EmptyInputError("\nEmpty inputs are not valid.")
