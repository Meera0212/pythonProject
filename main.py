# Pythn code to send GET/POST requst to any URL
import requests
if __name__ == '__main__':

    # sending a get request and saving a response as a res object
    res = requests.get('http://rtfactz.co.uk/helloworld')
    # extracting response content
    print(res.content)
    # extracting response text
    print(res.text)

    data = "Hello world!"
    # sending post request with string " Hello world!" and saving response as res1 object
    res1 = requests.post('http://rtfactz.co.uk/helloworld', data=data)
    # extracting response text
    print(res1.text)

