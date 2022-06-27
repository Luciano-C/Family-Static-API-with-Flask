
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
       if "id" not in member.keys():
        member["id"] = self._generateId()
       self._members.append(member)

    def delete_member(self, id):
        lista_id = [x["id"] for x in self._members]
        if id in lista_id:
            self._members = [x for x in self._members if x["id"] != id]

    def update_member(self, id, member):
        lista_id = [x["id"] for x in self._members]
        if id in lista_id:
            current_member = [x for x in self._members if x["id"] == id][0]
        indice = self._members.index(current_member)
        member["id"] = current_member["id"]
        self._members[indice] = member
        


    def get_member(self, id):
        lista_id = [x["id"] for x in self._members]
        if id in lista_id:
            member = [x for x in self._members if x["id"] == id][0]
        return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members


if __name__ == "__main__":
    familia = FamilyStructure("Jackson")
    
    John_Jackson = {
        "first_name": "John",
        "last_name": "Jackson",
        "age": 33,
        "lucky_numbers": [7, 13, 22]
         }

    Jane_Jackson = {
        "first_name": "Jane",
        "last_name": "Jackson",
        "age": 35,
        "lucky_numbers": [10, 14, 3]
         }

    Jimmy_Jackson = {
        "first_name": "Jimmy",
        "last_name": "Jackson",
        "age": 5,
        "lucky_numbers": [1]
         }
    
    # Añade miembros
    familia.add_member(John_Jackson)
    familia.add_member(Jane_Jackson)
    familia.add_member(Jimmy_Jackson)

    # Prueba borrar (Debe borrar a John Jackson)
    id_a_borrar = familia.get_all_members()[0]["id"]
    familia.delete_member(id_a_borrar)
    print(familia.get_all_members())
    print("-" * 100 )

    # Prueba get
    id_a_obtener = familia.get_all_members()[1]["id"]
    print(familia.get_member(id_a_obtener))
    print("-" * 100 )

    # Prueba Editar
    id_a_editar = familia.get_all_members()[1]["id"]
    Jimmy_Jackson_Updated = {
        "first_name": "Jimmy",
        "last_name": "Jackson",
        "age": 10,
        "lucky_numbers": [1, 20, 30]
         }
    familia.update_member(id_a_editar, Jimmy_Jackson_Updated)
    print(familia.get_all_members())
