import time

class Loading:
    __bar  = '█'
    def ProgressBar(self, title, timeout):
        """
        Parameters :
            - title : Title of the progress bar
            - timeout : Timeout of the progress bar (second)
        """
        timeout = timeout / 100
        for l in range(101):
            print(f'\r{title} {l}%\t{self.__bar}', flush=True, end="")
            if l % 5 == 0:
                self.__bar += '█'
            time.sleep(timeout)
        print()
