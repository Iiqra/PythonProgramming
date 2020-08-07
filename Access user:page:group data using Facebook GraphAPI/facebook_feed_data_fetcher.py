import requests, json

my_access_token = "acces_token_you_have_generated_from_graphapi"
my_group_id = "your_required_group_id"
graph_api_base_url = 'https://graph.facebook.com/v7.0/'
required_page = '/feed'


group_name_param = (
    ('field', 'name'),
    ('access_token', my_access_token),
)

group_object_response = requests.get(graph_api_base_url + my_group_id + '//' , params= group_name_param)

# IA -  response content comes in bytes, so we  need to decode it. Later you can use as you want!  
print ('The Group name response is {0}'.format(str(group_object_response.content, 'utf-8')))


fields_to_fetch = ['name', 'picture', 'created_time', 'message'] 
feed_params = (
    ('fields', fields_to_fetch),
    ('limit', '1000'),
    ('access_token', my_access_token),
)

feed_response = requests.get(graph_api_base_url + my_group_id + required_page, params=feed_params)
# IA - knowing types of objects time to time helps you to iterate 'em accordingly 
print(type(feed_response.text))


# IA - followin is to deserialize our text in response object to python object. 
data = json.loads(feed_response.text)


for post in data['data']:
    print (post)
print (type(data['data']))
print('Exit')