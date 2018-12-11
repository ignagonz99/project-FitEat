class Operations:

    def __init__(self, height, weight, age, gender):
        self.height = height
        self.weight = weight
        self.age = age
        self.gender = gender
        self.bmi = 0
        self.bmi_state = ''
        self.body_fat = 0
        self.body_fat_state = ''
        self.muscle_mass = 0
        self.bmr = 0
        self.diet = 0
        self.protein = 0
        self.fat = 0
        self.carbohydrates = 0

    def get_bmi(self):
        self.bmi = self.weight / ((self.height / 100) ** 2)
        if self.bmi < 18.4:
            self.bmi_state = 'Insufficient'
        elif 18.5 <= self.bmi <= 24.9:
            self.bmi_state = 'Normal'
        elif 25 <= self.bmi <= 29.9:
            self.bmi_state = 'Overweight'
        elif 30 <= self.bmi <= 40:
            self.bmi_state = 'Obesity I'
        elif self.bmi > 40:
            self.bmi_state = 'Obesity II'
        return self.bmi, self.bmi_state

    def get_body_fat(self):
        self.body_fat = (1.2 * self.bmi) + (0.23 * self.age) - (10.8 * self.gender) - 5.4
        if self.gender == 1:
            if self.body_fat < 12:
                self.body_fat_state = 'Low'
            elif 12 <= self.body_fat <= 20:
                self.body_fat_state = 'Normal'
            elif 21 <= self.body_fat <= 25:
                self.body_fat_state = 'Limit'
            elif self.body_fat > 25:
                self.body_fat_state = 'Obesity'
        else:
            if self.body_fat < 24:
                self.body_fat_state = 'Low'
            elif 24 <= self.body_fat <= 30:
                self.body_fat_state = 'Normal'
            elif 31 <= self.body_fat <= 33:
                self.body_fat_state = 'Limit'
            elif self.body_fat > 33:
                self.body_fat_state = 'Obesity'
        return self.body_fat, self.body_fat_state

    def get_muscle_mass(self):
        self.muscle_mass = self.weight - (self.weight * (self.body_fat / 100))
        return self.muscle_mass

    def get_bmr(self):
        if self.gender == 1:
            self.bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        elif self.gender == 0:
            self.bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        return self.bmr

    def get_protein(self):
        self.protein = 1.5 * self.weight
        return self.protein

    def get_fat(self):
        self.fat = 60
        return self.fat

    def get_carbohydrates(self, diet):
        self.diet = diet
        if self.diet == 1:
            self.carbohydrates = ((self.bmr - 300) - ((self.protein * 4) + (self.fat * 4))) / 4
        elif self.diet == 2:
            self.carbohydrates = ((self.bmr + 300) - ((self.protein * 4) + (self.fat * 4))) / 4
        return self.carbohydrates
