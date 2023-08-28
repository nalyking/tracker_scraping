#%% 

def generation_url(user_name:str, hashtag:str, competitive:bool=False, premier:bool=False,):
  url_base = "https://tracker.gg/valorant/profile/riot/"
  if competitive:
    container = "competitive"
  elif premier:
    container = "premier"
  end_url_base = "/overview?playlist="
  treated_user_name = user_name.strip().replace(' ','%20')
  treated_hashtag = hashtag.strip().replace('#','%23')
  final_url = url_base + treated_user_name + treated_hashtag + end_url_base + container
  return final_url


#%%
