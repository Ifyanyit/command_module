import cmd


class Person:
     age = 17

     def print_age(self):
         print(f"Age is {self.age}")



class AirBnBCMD(cmd.Cmd):
    """Simple command processor"""
    intro = "welcome to my console"

    def do_quit(self, line):
        """Exit the command line"""
        return True
    
    def do_greet(self, line):
        """Prints Greeting"""
        print('Hello dear')

    def do_Student_age(self, line):
        """ Prints age"""
        john = Person()
        john.print_age()



if __name__ == "__main__":
    AirBnBCMD().cmdloop()
