import backend.get_content_func as get_content_func

def get_x_posts(number_of_posts = 6, search_body = "", search_title="" , user_id = -1):
    
    all_posts = get_content_func.get_post()
    result = ""
    
    if search_body != "":
        result = [post for post in all_posts if search_body in post["body"]]

    if search_title != "":
        result = [post for post in all_posts if search_title in post["title"]]
    
    if user_id != -1:
        result = [post for post in all_posts if post["userId"] == user_id]

    return result