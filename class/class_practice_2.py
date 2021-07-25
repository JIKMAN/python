from abc import ABC, abstractmethod

class IWeapon(ABC):
    """무기 클래스"""
    @abstractmethod
    def use_on(self, other_character):
        pass

class Sword(IWeapon):
    """검 클래스"""
    def __init__(self, damage):
        self.damage = damage

    def use_on(self, other_character):
        """검 사용 메소드"""
        other_character.get_damage(self.damage)
        print(f'{self.owner}가 칼을 휘둘렀습니다.')
        
    def owner(self):
        return GameCharacter().name
        
class Gun(IWeapon):
    """총 클래스"""
    def __init__(self, damage, bullets):
        self.damage = damage
        self.bullets = bullets
    
    def use_on(self, other_character):
        """총 사용 메소드"""
        if self.bullets > 0:
            if other_character.hp > 0:
                other_character.get_damage(self.damage)
                self.bullets -= 1
                print(f"총을 쐈습니다. 총알이 {self.bullets}개 남았습니다.")
            else:
                print('상대가 이미 죽었습니다.')
        else:
            print("총알이 없어 공격할 수 없습니다.")



class GameCharacter:
    """게임 캐릭터 클래스"""
    def __init__(self, name, hp, weapon: IWeapon):
        self.name = name
        self.hp = hp
        self.weapon = weapon

    def attack(self, other_character):
        """다른 유저를 공격하는 메소드"""
        if self.hp > 0:
            self.weapon.use_on(other_character)
            print(f'{other_character.name}은 {self.weapon.damage}의 피해를 입었습니다.\n{other_character.name}의 잔여체력{other_character.hp}\n')            
        else:
            print(self.name + "님은 사망해서 공격할 수 없습니다.")

    def change_weapon(self, new_weapon):
        """무기를 바꾸는 메소드"""
        self.weapon = new_weapon
        print(f"{self.weapon}으로 무기를 변경하였습니다.")

    def get_damage(self, damage):
        """캐릭터가 공격받았을 때 자신의 체력을 깎는 메소드"""
        if self.hp <= damage:
            self.hp = 0
            print(self.name + "님은 이미 사망했습니다.")
        else:
            self.hp -= damage         

    def __str__(self):
        """남은 체력을 문자열로 리턴하는 메소드"""
        return f'{self.name}님의 남은 hp는 {self.hp}입니다.'

worn_sword = Sword(5)
sharp_sword = Sword(20)
riple = Gun(50, 10)

player1 = GameCharacter("Tom", 110, worn_sword)
player2 = GameCharacter("Jack", 200, riple)

player1.attack(player2)
player2.attack(player1)
player1.change_weapon(sharp_sword)
player1.attack(player2)
player2.attack(player1)
player1.attack(player2)
player2.attack(player1)
player1.attack(player2)
player2.attack(player1)

print(player1)
print(player2)