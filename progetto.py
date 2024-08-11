import json

class Contact:
    def __init__(self, first_name, last_name, phone, email):
        """
        Inizializza un nuovo contatto.

        :param first_name: Nome del contatto
        :param last_name: Cognome del contatto
        :param phone: Numero di telefono del contatto
        :param email: Indirizzo email del contatto
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __str__(self):
        """
        Restituisce una rappresentazione in stringa del contatto.

        :return: Stringa rappresentativa del contatto
        """
        return f"{self.first_name} {self.last_name}, Phone: {self.phone}, Email: {self.email}"

class ContactManager:
    def __init__(self):
        """
        Inizializza un nuovo gestore di contatti.
        """
        self.contacts = []

    def add_contact(self, contact):
        """
        Aggiunge un nuovo contatto alla lista dei contatti se non esiste già.

        :param contact: Istanza di Contact da aggiungere
        :raises ValueError: Se il contatto esiste già
        """
        if self.find_contact(contact.first_name, contact.last_name):
            raise ValueError("Contatto già presente")
        self.contacts.append(contact)

    def view_contacts(self):
        """
        Visualizza tutti i contatti presenti nella lista.
        """
        for contact in self.contacts:
            print(contact)

    def find_contact(self, first_name, last_name):
        """
        Trova un contatto per nome e cognome.

        :param first_name: Nome del contatto da trovare
        :param last_name: Cognome del contatto da trovare
        :return: Istanza di Contact se trovato, altrimenti None
        """
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        return None

    def edit_contact(self, first_name, last_name, new_contact):
        """
        Modifica i dettagli di un contatto esistente.

        :param first_name: Nome del contatto da modificare
        :param last_name: Cognome del contatto da modificare
        :param new_contact: Nuova istanza di Contact con i dettagli aggiornati
        :return: True se il contatto è stato modificato, altrimenti False
        """
        contact = self.find_contact(first_name, last_name)
        if contact:
            contact.first_name = new_contact.first_name
            contact.last_name = new_contact.last_name
            contact.phone = new_contact.phone
            contact.email = new_contact.email
            return True
        return False

    def delete_contact(self, first_name, last_name):
        """
        Elimina un contatto dalla lista.

        :param first_name: Nome del contatto da eliminare
        :param last_name: Cognome del contatto da eliminare
        :return: True se il contatto è stato eliminato, altrimenti False
        """
        contact = self.find_contact(first_name, last_name)
        if contact:
            self.contacts.remove(contact)
            return True
        return False

    def save_contacts(self, filename):
        """
        Salva tutti i contatti in un file JSON.

        :param filename: Nome del file in cui salvare i contatti
        """
        with open(filename, 'w') as file:
            json.dump([contact.__dict__ for contact in self.contacts], file)

    def load_contacts(self, filename):
        """
        Carica i contatti da un file JSON.

        :param filename: Nome del file da cui caricare i contatti
        """
        try:
            with open(filename, 'r') as file:
                contacts_data = json.load(file)
                self.contacts = [Contact(**data) for data in contacts_data]
        except FileNotFoundError:
            print("File not found. Starting with an empty contact list.")

def main():
    """
    Funzione principale che gestisce l'interfaccia utente della console.
    """
    manager = ContactManager()
    manager.load_contacts('contacts.json')

    while True:
        print("\nContactEase Solutions")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            try:
                manager.add_contact(Contact(first_name, last_name, phone, email))
                print("Contact added successfully.")
            except ValueError as e:
                print(e)
                print("Please try again.")
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            first_name = input("First Name of the contact to edit: ")
            last_name = input("Last Name of the contact to edit: ")
            new_first_name = input("New First Name: ")
            new_last_name = input("New Last Name: ")
            new_phone = input("New Phone: ")
            new_email = input("New Email: ")
            if manager.edit_contact(first_name, last_name, Contact(new_first_name, new_last_name, new_phone, new_email)):
                print("Contact updated successfully.")
            else:
                print("Contact not found.")
        elif choice == '4':
            first_name = input("First Name of the contact to delete: ")
            last_name = input("Last Name of the contact to delete: ")
            if manager.delete_contact(first_name, last_name):
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")
        elif choice == '5':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            contact = manager.find_contact(first_name, last_name)
            if contact:
                print(contact)
            else:
                print("Contact not found.")
        elif choice == '6':
            manager.save_contacts('contacts.json')
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
