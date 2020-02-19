import requests
import json
import sys
import unittest
baseurl = 'https://api.github.com/users'

def getrepositoryname(username,url):
    print('UserName:',username)
    resp = requests.get(url,username)
    #print(resp.text)
    json = resp.json()
    for i in range(0, len(json)):
        print("Project Name:", json[i]['url'])
    print('Total number of commits',len(json))

class TestIsgitcommitscount(unittest.TestCase):

    def test_all_parameters(self):
        self.assertTrue('richkempinski'.isalpha())
        self.assertFalse('https://api.github.com/repos/richkempinski/hellogitworld/commits'.isalpha())

    def test_url_correct(self):
        url='https://api.github.com/repos/richkempinski/hellogitworld/commits'
        self.assertTrue(url.rfind('/'))

    def test_repository_name_alpha(self):
        self.assertTrue('helloworld'.isalpha())
        self.assertFalse('hello-world8'.isalnum())

    def test_corect_parameters(self):
        username =''
        url =''
        self.assertIsNotNone(username,True)
        self.assertIsNotNone(url, True)

if __name__ == '__main__':
    print('Begin')
    #username ='richkempinski'
    username=input('Enter the UserID:')
    reponame = input('Enter the Repository Name:')
    #reponame ='helloworld'
    url = 'https://api.github.com/repos/'+username+'/'+reponame+'/commits'
    getrepositoryname(username,url)
    unittest.main()
