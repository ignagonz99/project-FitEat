
import tkinter as tk
import tkinter.ttk as ttk

import operations


height = ['50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67',
          '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85',
          '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102',
          '103', '104', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116',
          '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131',
          '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146',
          '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161',
          '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176',
          '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191',
          '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205',
          '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220',
          '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235']

weight = ['32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
          '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67',
          '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85',
          '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102',
          '103', '104', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116',
          '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131',
          '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146',
          '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161',
          '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176',
          '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191',
          '192', '193', '194', '195', '196', '197', '198', '199', '200']

age = ['14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31',
       '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
       '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67',
       '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85',
       '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102',
       '103', '104', '104', '105', '106', '107', '108', '109', '110']


class FitEat(tk.Frame):

    def __init__(self):

        super().__init__()


        self.lbl = None
        self.lbl2 = None
        self.lbl3 = None
        self.lbl4 = None
        self.lbl5 = None
        self.lbl6 = None
        self.lbl7 = None
        self.lbl8 = None
        self.lbl9 = None
        self.lbl10 = None
        self.lbl11 = None
        self.lbl12 = None
        self.lbl13 = None
        self.txt1 = None
        self.txt2 = None
        self.txt3 = None
        self.txt4 = None
        self.txt5 = None
        self.txt6 = None
        self.txt7 = None
        self.txt8 = None
        self.txt9 = None
        self.txt10 = None
        self.frame1 = None
        self.frame2 = None
        self.frame3 = None
        self.frame4 = None
        self.frame5 = None
        self.frame6 = None
        self.comb1 = None
        self.comb2 = None
        self.comb3 = None
        self.comb4 = None
        self.comb5 = None
        self.btn1 = None
        self.str1 = None
        self.str2 = None
        self.str3 = None
        self.str4 = None
        self.str5 = None
        self.str6 = None
        self.str7 = None

        self.height = 0
        self.weight = 0
        self.age = 0
        self.gender = 0
        self.diet = 0

        self.op = None


        self.gui()

    def get_bio_markers(self):
        # Get the data from the multiple combobox
        self.height = int(self.comb1.get())
        self.weight = int(self.comb2.get())
        self.age = int(self.comb3.get())
        if self.comb4.get() is 'Male':
            self.gender = 1
        elif self.comb4.get() is 'Female':
            self.gender = 0

        # Create an object corresponding to the Operations Class imported
        self.op = operations.Operations(self.height, self.weight, self.age, self.gender)

        # Call the methods to compute the results needed with the bio-markers as parameters
        bmi, bmi_state = self.op.get_bmi()
        bmi = round(bmi, 2)
        body_fat, body_fat_state = self.op.get_body_fat()
        body_fat = round(body_fat, 2)
        muscle_mass = round(self.op.get_muscle_mass(), 2)
        bmr = self.op.get_bmr()

        # Write values into the disabled inputs
        self.str1.set(str(bmi) + ' - ' + bmi_state)
        self.str2.set(str(body_fat) + '% - ' + body_fat_state)
        self.str3.set(str(bmr) + ' kcal')
        self.str4.set(str(muscle_mass) + ' kg')


        self.comb5.config(state='readonly')

        self.height = 0
        self.weight = 0
        self.age = 0
        self.gender = 0

    def get_macro_nutrients(self):
        # Call the methods to compute the macronutrients and display them.
        self.str5.set(str(self.op.get_protein()))
        self.str6.set(str(self.op.get_fat()))
        if self.comb5.get() == 'Hypertrophy / Gain muscle mass':
            self.str7.set(str(round(self.op.get_carbohydrates(2), 2)))
        elif self.comb5.get() == 'Definition / Lose body fat':
            self.str7.set(str(round(self.op.get_carbohydrates(1), 2)))

    def gui(self):
        # General window
        self.master.title("FitEat App v1.0")
        self.pack(fill=tk.BOTH, expand=True)
        self.lbl = tk.Label(self, text="Welcome to FitEat", font=("Helvetica", 25), bg="white")
        self.lbl.grid(columnspan=7, sticky=tk.N+tk.E+tk.S+tk.W, pady=(30, 30), padx=(45, 0), column=0, row=0)


        self.frame1 = tk.LabelFrame(self, text="Bio-markers", font=("Helvetica", 16), bg="white")
        self.frame1.grid(columnspan=3, sticky=tk.N, pady=10, padx=(25, 0), column=0, row=1)

        # first frame
        self.frame2 = tk.LabelFrame(self.frame1, text="Complete the empty fields", font=("Helvetica", 14), bg="white")
        self.frame2.grid(columnspan=3, sticky=tk.W, pady=20, padx=20, column=0, row=1)
        self.lbl2 = tk.Label(self.frame2, text="Height (cm)", font=("Helvetica", 16), bg="white")
        self.lbl2.grid(column=0, row=2, sticky=tk.W, padx=30, pady=(20, 10))
        self.comb1 = ttk.Combobox(self.frame2, state='readonly', values=height, width=8)
        self.comb1.current(100)
        self.comb1.grid(column=1, row=2, sticky=tk.W, padx=(0, 30), pady=(10, 10))
        self.lbl3 = tk.Label(self.frame2
                             , text="Weight (kg)", font=("Helvetica", 16), bg="white")
        self.lbl3.grid(column=0, row=3, sticky=tk.W, padx=30, pady=10)
        self.comb2 = ttk.Combobox(self.frame2, state='readonly', values=weight, width=8)
        self.comb2.current(50)
        self.comb2.grid(column=1, row=3, sticky=tk.W, padx=(0, 30), pady=(10, 10))
        self.lbl4 = tk.Label(self.frame2, text="Age (years)", font=("Helvetica", 16), bg="white")
        self.lbl4.grid(column=0, row=4, sticky=tk.W, padx=30, pady=10)
        self.comb3 = ttk.Combobox(self.frame2, state='readonly', values=age, width=8)
        self.comb3.current(30)
        self.comb3.grid(column=1, row=4, sticky=tk.W, padx=(0, 30), pady=(10, 10))
        self.lbl5 = tk.Label(self.frame2, text="Gender", font=("Helvetica", 16), bg="white")
        self.lbl5.grid(column=0, row=5, sticky=tk.W, padx=30, pady=10)
        self.comb4 = ttk.Combobox(self.frame2, state='readonly', values=('Male', 'Female'), width=8)
        self.comb4.current(0)
        self.comb4.grid(column=1, row=5, sticky=tk.W, padx=(0, 30), pady=(10, 10))
        self.btn1 = tk.Button(self.frame2, text="Compute Results", command=self.get_bio_markers)
        self.btn1.grid(columnspan=2, sticky=tk.W, row=6, column=0, padx=50, pady=15)

        # second frame
        self.frame3 = tk.LabelFrame(self.frame1, text="Results", font=("Helvetica", 14), bg="white")
        self.frame3.grid(columnspan=3, sticky=tk.W+tk.N, pady=20, padx=20, column=4, row=1)
        self.lbl6 = tk.Label(self.frame3, text="BMI (Body Mass Index)", font=("Helvetica", 16), bg="white")
        self.lbl6.grid(column=0, row=2, sticky=tk.W, padx=30, pady=(20, 10))
        self.str1 = tk.StringVar()
        self.txt4 = tk.Entry(self.frame3, width=15, state='disabled', textvariable=self.str1)
        self.txt4.grid(column=1, row=2, sticky=tk.W, padx=(0, 30), pady=(20, 10))
        self.lbl7 = tk.Label(self.frame3, text="Body fat", font=("Helvetica", 16), bg="white")
        self.lbl7.grid(column=0, row=3, sticky=tk.W, padx=30, pady=10)
        self.str2 = tk.StringVar()
        self.txt5 = tk.Entry(self.frame3, width=15, state='disabled', textvariable=self.str2)
        self.txt5.grid(column=1, row=3, sticky=tk.W, padx=(0, 30), pady=(0, 10))
        self.lbl8 = tk.Label(self.frame3, text="BMR (Basal Metabolic Rate)", font=("Helvetica", 16), bg="white")
        self.lbl8.grid(column=0, row=4, sticky=tk.W, padx=30, pady=10)
        self.str3 = tk.StringVar()
        self.txt6 = tk.Entry(self.frame3, width=15, state='disabled', textvariable=self.str3)
        self.txt6.grid(column=1, row=4, sticky=tk.W, padx=(0, 30), pady=(0, 10))
        self.lbl9 = tk.Label(self.frame3, text="Muscle mass", font=("Helvetica", 16), bg="white")
        self.lbl9.grid(column=0, row=5, sticky=tk.W, padx=30, pady=10)
        self.str4 = tk.StringVar()
        self.txt7 = tk.Entry(self.frame3, width=15, state='disabled', textvariable=self.str4)

        self.txt7.grid(column=1, row=5, sticky=tk.W, padx=(0, 30), pady=(0, 10))

        # thrid frame
        self.frame4 = tk.LabelFrame(self, text="Specific diet", font=("Helvetica", 16), bg="white")
        self.frame4.grid(columnspan=3, sticky=tk.N, pady=10, padx=(25, 0), column=0, row=2)

        # thrid frame
        self.frame5 = tk.LabelFrame(self.frame4, text="Choose a diet", font=("Helvetica", 14), bg="white")
        self.frame5.grid(columnspan=3, sticky=tk.N, pady=20, padx=20, column=0, row=1)
        self.lbl10 = tk.Label(self.frame5, text="Guidelines for", font=("Helvetica", 16), bg="white")
        self.lbl10.grid(columnspan=4, column=0, row=0, sticky=tk.N, padx=20, pady=(15, 15))
        self.comb5 = ttk.Combobox(self.frame5, state='disabled',
                                  values=('Hypertrophy / Gain muscle mass', 'Definition / Lose body fat'), width=40)
        self.comb5.current(0)
        self.comb5.grid(columnspan=4, column=4, row=0, sticky=tk.N, padx=(30, 30), pady=(15, 15))

        # fourth frame
        self.frame6 = tk.LabelFrame(self.frame4, text="Macronutrients", font=("Helvetica", 14), bg="white")
        self.frame6.grid(columnspan=3, sticky=tk.N, pady=(0, 20), padx=20, column=0, row=2)
        self.lbl11 = tk.Label(self.frame6, text="Protein (gr)", font=("Helvetica", 16), bg="white")
        self.lbl11.grid(columnspan=3, column=0, row=1, sticky=tk.N, padx=(30, 30), pady=(10, 10))
        self.str5 = tk.StringVar()
        self.txt8 = tk.Entry(self.frame6, width=8, state='disabled', textvariable=self.str5)
        self.txt8.grid(columnspan=3, column=0, row=2, sticky=tk.N, padx=(30, 30), pady=(0, 10))
        self.lbl12 = tk.Label(self.frame6, text="Fat (gr)", font=("Helvetica", 16), bg="white")
        self.lbl12.grid(columnspan=3, column=3, row=1, sticky=tk.N, padx=(30, 30), pady=(10, 10))
        self.str6 = tk.StringVar()
        self.txt9 = tk.Entry(self.frame6, width=8, state='disabled', textvariable=self.str6)
        self.txt9.grid(columnspan=3, column=3, row=2, sticky=tk.N, padx=(30, 30), pady=(0, 10))
        self.lbl13 = tk.Label(self.frame6, text="Carbohydrates (gr)", font=("Helvetica", 16), bg="white")
        self.lbl13.grid(columnspan=3, column=6, row=1, sticky=tk.N, padx=(30, 30), pady=(10, 10))
        self.str7 = tk.StringVar()
        self.txt10 = tk.Entry(self.frame6, width=8, state='disabled', textvariable=self.str7)
        self.txt10.grid(columnspan=3, column=6, row=2, sticky=tk.N, padx=(30, 30), pady=(0, 10))
        self.btn1 = tk.Button(self.frame6, text="Get Macronutrients", command=self.get_macro_nutrients)
        self.btn1.grid(columnspan=3, column=3, row=3, sticky=tk.N, padx=(30, 30), pady=(10, 10))


def main():

    root = tk.Tk()
    root.rowconfigure(9, {'minsize': 30})
    root.columnconfigure(9, {'minsize': 30})
    root.geometry("820x800")
    root.resizable(0, 0)
    app = FitEat()
    root.mainloop()


if __name__ == '__main__':
    main()
