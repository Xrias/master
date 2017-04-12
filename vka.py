import vk
import time

'''Делит some_list на подсписки по 25 штук в каждом для execute'''
def divide_by_25(some_list):     
    help_list = []
    for i in range((len(some_list) //25) + 1):
        help_list.append(some_list[i*25: min((i+1)*25, len(some_list))])
    return help_list

'''Функция для удаления из списка удаленных\забаненых пользователей, работает медленно, добавить execute было бы неплохо'''
def kill_deactivated(some_list, api):  
    help_list = some_list.copy()
    for i in range(len(some_list)):
        if 'deactivated' in api.users.get(user_ids = some_list[i], fields = 'deactivated')[0].keys():
            help_list.remove(some_list[i])
        time.sleep(0.33)
    return help_list 


def main():  
    session = vk.Session(access_token='850ab720812e05e120743409bb7b1f0b84927a48128d089897e6db34a61079e8b6afe661b80116f1c5de4')
    api = vk.API(session)  
    if 'deactivated' not in api.users.get(user_ids = '48690241', fields = 'deactivated')[0].keys():
        time.sleep(0.33)
        my_friends = divide_by_25(api.friends.get(user_id = '48690241'))
    friends_of_my_friends = []
    code = 'return['
    for i in my_friends:
        for ip in i:
            code = code + 'API.friends.get({user_id:' + str(ip) + '}),'
        code = code + '];'
        friends_of_my_friends = friends_of_my_friends + (api.execute (code = code))      
        code = 'return[' 
    return 0


main()