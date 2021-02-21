from check import main
from fileOrganizer import Dictionary


class Execute:
    def __init__(self, path, y):
        self.Dir_PATH = path
        self.Src_PATH = path
        self.B = y
        if y >= 5:
            print("Enter the Valid Choice")
            return
        main(self.Src_PATH, self.Dir_PATH)

    def Run(self):
        if self.B >= 4:
            return
        Dictionary(self.Dir_PATH, self.B)


if __name__ == "__main__":
    while True:
        print("Welcome to JFO : Junk File Organizer\n")
        print("Select 1 for Organizing Files with Extension")
        print("Select 2 For Organizing files with Dates")
        print("Select 3 for Organizing Files with Size")
        print("Select 4 for to Convert Organized Files into Junk Files\n")
        print("After Selecting Press Enter Key!\n")
        A = input("PLEASE ENTER PATH\n")
        A = r''+A+'\\'
        if len(A) == 1:
            break
        B = int(input("Enter Your Choice\n"))
        print("Thank You for using JFO !!\n")
        
        obj = Execute(A, B)
        obj.Run()
