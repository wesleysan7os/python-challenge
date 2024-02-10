from ..errors.error_types import EmptyInputError

def salve_contact(phone_book, contact):
    try:
        __check_has_empty_inputs(contact)
    except EmptyInputError as e:
        print(e.message)
    else:
        phone_book.append(contact)
        print("Contato salvo com sucesso!")

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
            phone_book[indice] = contact
            print("Contato atualizado com sucesso!")

def remove_contact(phone_book, indice):
    try:
        indice = int(indice)
    except Exception as e:
        print(e)
    else:
        del phone_book[indice]
        print("Contato removido com sucesso!")

def check_as_favorite(phone_book, indice):
    try:
        indice = int(indice)
    except Exception as e:
        print(e)
    else:
        phone_book[indice] = phone_book[indice]["isFavorite"] = True

def uncheck_as_favorite(phone_book, indice):
    try:
        indice = int(indice)
    except Exception as e:
        print(e)
    else:
        phone_book[indice] = phone_book[indice]["isFavorite"] = False

def show_contacts(phone_book):
    for index, contact in enumerate(phone_book):
        check_if_its_favorite = "✓" if contact.isFavorite else " "
        print(f"{index}. [{check_if_its_favorite}] "
            f"Nome: {contact.name} "
            f"Telefone: {contact.telefone}")


def ask_for_contact_info():
    name = input("Digite o nome do contato: ")
    celphone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    contact = {
        "name": name,
        "celphone": celphone,
        "email": email
    }
    return contact

def __check_has_empty_inputs(contact):
    if not contact.name or not contact.celphone or contact.email:
        raise EmptyInputError("Empty inputs are not valid.")
