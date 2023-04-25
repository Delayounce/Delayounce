import json
import requests


def write_status_code_to_console (status_code):
    match status_code:
        case 200:
            print("jest ok")
        case 400:
            print("Bad request")
        case 401:
            print("Unauthorized")
        case 403:
            print("Forbidden")
        case 404:
            print("Not found")

    if status_code != 200:
        print(" Error: status code:", status_code)
        exit(-1)
# -=   end of write_status_code_to_console   =-


def get_post():

    '''
    -= posts JSONS contains =-
    'userId'
    'id'
    'title'
    'body'

    '''
    myAPIrequest = requests.get('https://jsonplaceholder.typicode.com/posts/')
    content = myAPIrequest.content
    write_status_code_to_console(myAPIrequest.status_code)
    
    posts_JSON = json.loads(content)

    return posts_JSON

def get_albums():

    '''
    -= albums JSONS contains =-
    'userId'
    'id'
    'title'

    '''
    myAPIrequest = requests.get('https://jsonplaceholder.typicode.com/albums')
    content = myAPIrequest.content
    write_status_code_to_console(myAPIrequest.status_code)
    
    albums_JSON = json.loads(content)

    return albums_JSON
    
def get_photos():

    '''
    -= photos JSONS contains =-
    'albumId'
    'id'
    'url'
    'thumbnailUrl'

    '''
    myAPIrequest = requests.get('https://jsonplaceholder.typicode.com/photos')
    content = myAPIrequest.content
    write_status_code_to_console(myAPIrequest.status_code)
    
    photos_JSON = json.loads(content)

    return photos_JSON

def get_users():

    '''
    -= photos JSONS contains =-
    'id'
    'name'
    'username'
    'email'
    'address'
        {
        'street'
        'suite'
        'city'
        'zipcode'
        'geo'
        {
            'lat'
            'lng'
        }
        }
    'phone'
    'website'
    'company'
    {
    'name'
    'catchPhrase'
    'bs'
    }

    '''
    myAPIrequest = requests.get('https://jsonplaceholder.typicode.com/users')
    content = myAPIrequest.content
    write_status_code_to_console(myAPIrequest.status_code)
    
    users_JSON = json.loads(content)

    return users_JSON

def get_comments():

    '''
    -= photos JSONS contains =-
    'postId'
    'id'
    'name'
    'email'
    'body'

    '''
    myAPIrequest = requests.get('https://jsonplaceholder.typicode.com/comments')
    content = myAPIrequest.content
    write_status_code_to_console(myAPIrequest.status_code)
    
    comments_JSON = json.loads(content)

    return comments_JSON



'''
#-= example of how to use the JSON to get the element you want =-
print(json_data[1]['title'])


'''
