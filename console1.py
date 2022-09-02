# Configure Cmd attributes
# 'prompt' can be set to string to be printed each time the user is
#+ asked for a new command
# 'intro' is the "welcome" message printed at the start of the program.
# When printing help, the 'doc_header', 'misc_header', 'undoc-header'
#+ and ''ruler' attributes are used to format the output

import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor."""

    prompt = 'Type_Command: '  # this appears instead of the default '(Cmd)'
    intro = "Simple command processor example."

    doc_header = 'doc_header'  # header appears when you type 'help'
    misc_header = 'misc_header' # "            "          "
    undoc_header = 'undoc_header' #  "         "           "

    ruler = '_'   # makes a line rule under doc_header

    def do_prompt(self, line):   # 'line' is just a variable( argument/parameter)
        """ Change the interactive prompt"""
        self.prompt = line + ': '  # Changes the default prompt

    def do_greet(self, person):
        """greet person"""
        if person:
            print("Hi,", person)
        else:
            print("Hi")

    def do_EOF(self, line):
        """ Type EOF to exit"""
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
