choice = input("A or B or C?\n")
input_text= open('D:\\Projects\\Ddum\\HomeWork\\Dictionary\\test.txt', 'r')
alpha = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
alpha1 = 'abcdefghijklmnopqrstuvwxyz'
class Dictionary():

    def choice(self, text):
        if choice == 'A' or choice == 'a':
            self.choice_A(text)
        elif choice == 'B' or choice == 'b':
            self.choice_B(text)
        elif choice == 'C' or choice == 'c':
            self.choice_C(text)
        else:
            print('dibloid')
        
    def colculate_total_count(self, text):
        count_letters = 0
        for i in alpha:
            count = text.count(i)
            count_letters = count_letters + count
        return count_letters

    def choice_A(self, text):
        list_txt_A = text.split(' ')
        list_txt_A.sort()
        list_txt_A = set(list_txt_A)
        list_txt_A = ', '.join(list_txt_A)
        print(list_txt_A)
        
    
    def choice_B(self, text):
        for i in alpha1:
            count = text.count(i) + text.count(i.upper())
            if count == 0:
                continue
            print(("{} - {}".format(i.upper(), count)))
        


    def choice_C(self, text):
        totalLen = self.colculate_total_count(text)
        for j in alpha1:
            count = text.count(j) + text.count(j.upper())
            percent = "{:.2f}".format(round((count/totalLen*100),2))
            print(("{0} - {1}%".format(j.upper(), percent)))


object1 = Dictionary()
object1.choice(input_text.read())