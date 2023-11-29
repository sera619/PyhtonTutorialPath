class CharClass:
    def __init__(self, name, health, mana):
        self.classnames = ["Krieger", "Magier"]
        self.name = name
        self.health = health
        self.max_health = health
        self.mana = mana
        self.atk = None
        self.is_alive = True
        self.classname = ""

    def display_info(self):
        print(f"[!] Name: {self.name}")
        print(f"[!] Class: {self.classname}")
        print(f"[!] Health: {self.health} / {self.max_health}")
        print(f"[!] Mana: {self.mana}")
        print(f"[!] Attack: {self.atk}")
        
    def take_damage(self, damage):
        if self.is_alive:
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                self.is_alive = False
            print(f"[!] {self.name} took {damage} damage. Remaining health: {self.health}")
        else:
            print(f"[X] {self.name} is already defeated. Cannot take more damage.")

    def attack(self, target):
        if self.is_alive:
            print(f"[!] {self.name} attacks {target.name}.")
        else:
            print(f"[X] {self.name} is defeated and cannot attack.")

class Mage(CharClass):
    def __init__(self, name, health, mana, spell_power):
        super().__init__(name, health, mana)
        self.classname = self.classnames[1]
        self.spell_power = spell_power
        self.atk = spell_power
    

        
class Warrior(CharClass):
    def __init__(self, name, health, mana, attack_power):
        super().__init__(name, health, mana)
        self.classname = self.classnames[0]
        self.attack_power = attack_power
        self.atk = attack_power
    

