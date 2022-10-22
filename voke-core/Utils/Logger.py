class Logger:
    def log(self, c, output):
        ansi = ""
        reset = "\033[0;37m"
        if (c == "red"):
            a = "\033[0;31m"
        elif (c == "blue"):
            a = "\033[0;34m"
        elif (c == "purple"):
            a = "\033[0;35m"
        elif (c == "yellow"):
            a = "\033[0;33m"
        elif (c == "cyan"):
            a = "\033[0;36m"
        elif (c == "green"):
            a = "\033[0;32m"
        elif (c == "white"):
            a = "\033[0;37m"

        
        print(a + output + reset)
	