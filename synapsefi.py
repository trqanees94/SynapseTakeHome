from synapse_pay_rest import Client
from synapse_pay_rest import User
from synapse_pay_rest import Node

args = {
    'client_id': 'client_id_FS65iP1RkqcXp3f0ILDHjAE7ztZla0YsJvMGBbVw', # your client id
    'client_secret': 'client_secret_7pNnVyhdXsSqTGmBgtE6r32Mb8AkZfuRa1JoYHlK', # your client secret
    'fingerprint': '58d14daf6e43ace0889d3993aab7b1b1',
    'ip_address': '127.0.0.1', # user's IP
    'development_mode': True, # (optional) default False
    'logging': False # (optional) logs to stdout if True
}


def getUserData():
    options = {
        'page': 1,
        'per_page': 20,
        'query': 'Tariq Anees' # name/email substring
    }

    client = Client(**args)
    user = User.by_id(client, '5bae65f98cf5e9007c2525d9', full_dehydrate='yes')
    userInfo = user.base_documents[0]


    name = userInfo.name
    email = userInfo.email
    permissionScope = userInfo.entity_scope

    # userDict = {'name': name, 'email': email }
    userList = [name, email, permissionScope]
    # userList = [name, email]
    return userList

def createUser():
    args1 = {
    'email': 'hello@synapsepay.com',
    'phone_number': '555-555-5555',
    'legal_name': 'Hello McHello',
    'note': ':)',  # optional
    'supp_id': '123abc',  # optional
    'is_business': True,
    'cip_tag': 1
}

    user = User.create(client, **args1)

def getNodes():

    options = {
    'page': 1,
    'per_page': 20
    }
    client = Client(**args)
    user = User.by_id(client, '5bae65f98cf5e9007c2525d9', full_dehydrate='yes')

    nodes = Node.all(user, **options)
    node1 = Node.by_id(user, '5baefc0c60050500b4ff02bb')
    node2 = Node.by_id(user, '5baefc269a835600a3df3dbc')
    node3 = Node.by_id(user, '5baefba971fd1b00e40de3e3')

    node1Info = node1.nickname
    node2Info = node2.nickname
    node3Info = node3.nickname

    node1Bal = node1.balance
    node2Bal  = node2.balance
    node3Bal  = node3.balance

    nodeList = [[node1Info, node1Bal], [node2Info, node2Bal], [node3Info, node3Bal]]

    return nodeList
