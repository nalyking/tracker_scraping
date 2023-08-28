class Tv():

    def __init__(self,):
        self.canal= int(input('CANAL: '))
        self.volume= int(input('VOLUME: '))
    

    def show_volume(self,):
        return self.volume


    def show_channel(self,):
        return self.canal

canal= Tv()
show_canal= Tv.show_channel
print(show_canal)
show_volume= Tv.show_volume
print(show_volume)