def add_note(notes_dict, note_title, note_content): #add_note додає нову нотатку (назва та сама нотатка в нас мають тип string і не потребують перевірки). нотатка додається у кінець словника
    notes_dict[note_title] = note_content

def remove_note(notes_dict): #видаляє першу додану нотатку (якщо нотанок у записнику немає, видає повідомлення про це)
    if not notes_dict:
        raise ValueError("Список нотаток порожній. Немає що видаляти.")

    first_note_title = list(notes_dict.keys())[0]
    first_note_content = notes_dict.pop(first_note_title)
    print(f"Нотатка '{first_note_title}' видалена.")
    return first_note_title, first_note_content

def display_notes(notes_dict): #виводить дані всього записника
    output = "Список нотаток:\n"
    for title, content in notes_dict.items():
        output += f"{title}: {content}\n"
    return output

def get_amount(notes_dict): #повертає кількість нотаток в записнику
    return len(notes_dict)




