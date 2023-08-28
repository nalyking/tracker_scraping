#%%
from bs4 import BeautifulSoup
from gerador_url import generation_url

import requests

#%%
class Tracker():
    
    def __init__(self, user_name, hashtag, competitive:bool=False, premier:bool=False):
        self.user_name = user_name
        self.hashtag = hashtag
        self.competitive = competitive
        self.premier = premier
        self.url= self.get_url()
        self.doc = self.get_request()
        
    def run(self,):
        user_name= self.get_user_name()
        top_maps= self.get_top_maps()
        top_agents = self.get_user_top_agents()
        return {
            "user_name": user_name,
            "top_maps": top_maps,
            "top_agents": top_agents,
        }

    def get_url(self,):
        return generation_url(self.user_name, self.hashtag, self.competitive, self.premier)
    
    def get_request(self,):
        result= requests.get(self.url).text
        return BeautifulSoup(result, "html.parser")

    def get_top_maps(self,):
        maps= self.doc.find(["div"], class_= "top-maps__maps-header")
        info_maps= list(maps.next_siblings)

        top_maps= []
        for info_map in info_maps:
            maps_name= info_map.find(class_="name")
            rating_map= info_map.find(class_="value")
            win_count= info_map.find(class_="label")
            
            dict_maps= {
                "maps_name": maps_name.string,
                "win_rating": {
                    "rate_porcent":rating_map.string,
                    "win_count":win_count.string
                }
            }
            top_maps.append(dict_maps)
        return top_maps

    def get_user_name(self,):
        name= self.doc.find(["span"], class_="trn-ign__username")
        hash_tag= self.doc.find(["span"], class_="trn-ign__discriminator")
        head_shoot= self.doc.find_all(["span"], class_="value")
        kast_porcent= self.doc.find_all(["span"], class_="value")
        rank= self.doc.find(["span"], class_="stat__value")
        user_info= []
        dict_user= {
            "user_name": name.string,
            "hash_tag_user": hash_tag.string,
            "user_hs_porcent": head_shoot[5].string,
            "KAST": kast_porcent[8].string,
            "Rank": rank.string
        }
        user_info.append(dict_user)
        return user_info

    def get_user_top_agents(self,):
        top_agents= self.doc.find_all(["div"], class_="value")

        agent= top_agents[10]
        agent_win_rate= top_agents[12]
        agent_two= top_agents[17]
        agent_win_rate_two= top_agents[19]
        agent_tree= top_agents[24]
        agent_win_rate_tree= top_agents[26]

        any_list= []
        top3_agents_user= {
            "agent1": agent.string,
            "agent1_win_rate": agent_win_rate.string,
            "agent2": agent_two.string,
            "agent2_win_rate": agent_win_rate_two.string,
            "agent3": agent_tree.string,
            "agent3_win_rate": agent_win_rate_tree.string
        }
        any_list.append(top3_agents_user)
        return any_list


#%%

    

#%%