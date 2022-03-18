class Loading:
    __bar = "█" 
    def ProgressBar(self, title, timeout):
        timeout = timeout / 100
        for l in range(101):
            time.sleep(timeout)
            print(f"\r{title}\t{self.__bar} {l}%", end="", flush=True)
            if l % 5 == 0:
                self.__bar += "█"
