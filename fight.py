import random
from time import sleep

f1_lvl, f2_lvl = random.randint(0, 5), random.randint(0, 5) 

f1_data = {
    "member": {
        "id": 657567767786868,
        "name": "SubZero",  
    },

    "specs": {
        "lvl": f1_lvl,
        "hp": 100 + f1_lvl*10,
        "exp": 0,
        "crt": 10 + f1_lvl*5,
        "dmg": int(20 + f1_lvl*1.2),
    },  
}


f2_data = {
    "member": {
        "id": 579898759595,
        "name": "Scorpion",  
    },

    "specs": {
        "lvl": f2_lvl,
        "hp": 100 + f2_lvl*10,
        "exp": 0,
        "crt": 10 + f2_lvl*5,
        "dmg": int(20 + f2_lvl*1.2),
    },  
}

class Fighter:


    def __init__(self, member:dict, specs:dict):
        self.__member = member
        self.__specs = specs
        self._new_specs = specs
        self.can_fight = True


    def attack(self, target:'Fighter'=None):
        attack_chance = random.randint(0, self.__specs["dmg"])
        crit_chance = random.randint(1, 100)

        print(1)
        if attack_chance > 0:
            if crit_chance > 20:
                target._specs["hp"] -= self._specs["dmg"]
                print(target._member['name'], 'имеет ', target._specs["hp"], ' hp!')
            else:
                target._specs["hp"] -= self._specs["dmg"] + self._specs["crt"]
                print(target._member['name'], 'имеет ', target._specs["hp"], ' hp!')
            
        else:
            target._specs["hp"] -= 0
            print(target._member['name'], 'имеет ', target._specs["hp"], ' hp!')

        if target._specs["hp"] <= 0:
            target.can_fight = False
            print(target._member['name'], 'умер...')
        

    def __str__(self):
            return f"Боец {self.__member['name']} имеет параметры {self._specs}"

    def win(self, target:"Fighter"=None):
        diff = abs(self._specs["lvl"] - target._specs["lvl"])

        # Разница от 0 до 4
        if diff < 4:
            self._specs["exp"] += 10
        # Разница от 4 до 9
        elif diff < 9:
            # Если наш лвл больше противника
            if self._specs["lvl"] > target._specs["lvl"]:
                self._specs["exp"] -= 5
            # Противник выше лвл-ом
            else:
                self._specs["exp"] += 20
        # разница больше 9
        elif diff >= 9:
            # Если наш лвл больше противника
            if self._specs["lvl"] > target._specs["lvl"]:
                self._specs["exp"] -= 40
            # Противник выше лвл-ом
            else:
                self._specs["exp"] += 80
                self.__lvl_up()

        if self._specs["exp"] >=100:
            self.__lvl_up()

    def __lvl_up(self):
        # Реализовать lvlUp параметров new_specs
        self._specs["lvl"] += 1
        self._specs["exp"] -= 100
        self._specs["hp"] += 10
        self._specs["crt"] += 5
        self._specs["dmg"] *= 1.2


    def __str__(self):
        return f"Боец {self.__member['name']} имеет параметры {self.__specs}"


# Создаём два объекта класса Fighter (f1, f2) на основе инфы из f2_data f1_data
# 1
f1 = Fighter(f1_data["member"], f1_data["specs"])
# 2
f2 = Fighter(f2_data["member"], f2_data["specs"])

print(f1)
print(f2)


def fight(f1:Fighter=None, f2:Fighter=None):
    # true f1 => false f2
    turn = True 

    while f1.can_fight and f2.can_fight:
        sleep(2)
        # Первый претендент
        if turn:
            turn = False
            f1.attack(f2)

        # Второй претендент
        else:
            turn = True
            f2.attack(f1)

    # Выбор победителя

    if f1.can_fight:
        f1.win(f2)
        print(f"{f1.__member['name']} победил {f2.name} и выжил при {f1.hp}")
    else:
        f2.win(f1)
        print(f"{f2.__member['name']} победил {f1.name} и выжил при {f2.hp}")
fight(f1, f2)