from flask import Flask, request

from utils import generate_password

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/password")
def password():
    length = request.args.get('length', '10')

    if length.isdigit():
        length = int(length)
        max_length = 200

        if length > max_length:
            return f'Length should be less then {max_length}'

        return generate_password(length)

    return f'Invalid length value: {length}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)


'''
http://127.0.0.1:5001/hello?name=John&age=20

http:// 127.0.0.1 :5001 /hello

1. Protocol
http/s

ftp

smtp 

2. IP address

IPv4
127.0.0.1

x.x.x.x

[0-255].[0-255].[0-255].[0-255]
0.0.0.0
255.255.255.255
23.34.21
35.35.37.38.21
32.256.12.10

127.0.0.1

IPv6

3. PORT

5001

0-65535

http - 80
https - 443
ssh - 22

4. PATH

/hello

5. Query parameters 

?name=John&age=20

'''
