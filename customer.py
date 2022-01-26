class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if 20 <= self.age < 65:
            return "1500"
        elif 65 <= self.age < 75:
            return "1200"
        elif 3 < self.age < 20:
            return "1000"
        elif 75 <= self.age:
            return "500"  # C6
        else:
            return "0"  # C5

    def info_csv(self):  # C-4
        return f"{self.full_name()}, {self.age}, {self.entry_fee()}"

    def info_tab(self):  # C-7
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"  # \t タブ区切り

    def info_pipe(self):  # C-8
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"

    # Customerクラスのインスタンス化


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
nobunaga = Customer(first_name="Nobunaga", family_name="Oda", age=3)
hideyoshi = Customer(first_name="Hideyoshi", family_name="Toyotomi", age=75)

# C-1 - C-3, C-5 - C-6
print(ken.full_name(), ken.age, ken.entry_fee())
print(tom.full_name(), tom.age, tom.entry_fee())
print(ieyasu.full_name(), ieyasu.age, ieyasu.entry_fee())
print(nobunaga.full_name(), nobunaga.age, nobunaga.entry_fee())
print(hideyoshi.full_name(), hideyoshi.age, hideyoshi.entry_fee())

print()  # 改行

# C-4, C-7 - C-8
print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())
print()
print(ken.info_tab())
print(tom.info_tab())
print(ieyasu.info_tab())
print()
print(ken.info_pipe())
print(tom.info_pipe())
print(ieyasu.info_pipe())
