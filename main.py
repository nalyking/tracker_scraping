#%%
from web_scrap_tracker import Tracker 

class Main():

    def __init__(self,):
        pass
        
    def __new__(self,):
        return self.initiate(self,)

    def initiate(self,):
        user_name= str(input(''))
        hashtag= str(input(''))
        options= str(input('Escolha uma das opções entre [ 1 / 2 / 3 ]:\n 1. Competitivo\n 2. Premier\n 3. Ambos'))
        
        if options == "1":
            return Tracker(user_name= user_name, hashtag= hashtag, competitive= True).run()
        elif options == "2":
            return Tracker(user_name= user_name, hashtag= hashtag, premier= True).run()
        elif options == "3":
            competitive= Tracker(user_name= user_name, hashtag= hashtag, competitive= True).run()
            premier= Tracker(user_name= user_name, hashtag= hashtag, premier= True).run()
            return {
                "competitive": competitive,
                "premier": premier,
            }

        else:
            return print('Nenhuma das opções foi escolhida.')
#%%
if __name__ == "__main__":
   principal= Main()
   print(principal)

#%%