import backend.get_content_func as get_content_func
import random


def get_x_posts(page_number = 0,post_limit=6, search_body = "", search_title="" , user_id = -1):
    
    all_posts = get_content_func.get_post()
    result = []
    
    if search_body != "":
        result += [post for post in all_posts if search_body in post["body"]]

    if search_title != "":
        result += [post for post in all_posts if search_title in post["title"]]
    
    if user_id != -1:
        result += [post for post in all_posts if post["userId"] == user_id]

    if (search_body == "" and search_title=="" and user_id == -1):
        result += all_posts

    return result[page_number*post_limit:page_number*post_limit+post_limit]


def get_x_random_photos (number_of_photos):
    all_photos = get_content_func.get_photos()
    
    result = []
    for i in range(number_of_photos):
        result.append(all_photos[random.randint(0, len(all_photos))]["url"]) 
    
    return result
