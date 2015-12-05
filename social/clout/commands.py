import cmd
from clout.main import Clout


class CloutCli(cmd.Cmd):
    clout = Clout()

    def do_clout(self, person=None):
        """
        Print the clout of the person if provided, else all the people.
        :param person:
        """
        print self.clout.clout(person=person)

    def default(self, line):
        """
        Handles follower following followee.
        Format: <follower name> follows <followee name>
        :param line:
        """
        try:
            args = line.split(" follows ")
            follower = args[0]
            followee = args[1]
            follows = self.clout.follow(follower, followee)

            if follows:
                print "OK!"
            else:
                print "Nope!"

        except IndexError:
            print ("That is not a valid command.\nEnter format: "
                   "<follower name> follows <followee name>")
        return

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    CloutCli().cmdloop()