def parse(web_address):
    if "0" <= web_address[-1] <= "9" or "A" <= web_address[-1] <= "Z" or "a" <= web_address[-1] <= "z":
        web_address = web_address[web_address.find("name"):]
    else:
        web_address = web_address[web_address.find("name"):-1]

    if len(web_address) > 1:
        res_dict = dict((a.strip(), b.strip())
                    for a, b in (element.split("=", 1)
                                for element in web_address.split("&")))
    else: res_dict = {}
    return res_dict

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=John') == {'name': 'John'}


def parse_cookie(web_cookie):
    if len(web_cookie) != 0 and ("0" <= web_cookie[-1] <= "9" or "A" <= web_cookie[-1] <= "Z" or "a" <= web_cookie[-1] <= "z"):
        web_cookie = web_cookie[web_cookie.find("name"):]
    else:
        web_cookie = web_cookie[web_cookie.find("name"):-1]

    if len(web_cookie) > 1:
        res_dict = dict((a.strip(), b.strip())
                    for a, b in (element.split("=", 1)
                                for element in web_cookie.split(";")))
    else: res_dict = {}
    return res_dict


if __name__ == '__main__':
    assert parse_cookie('name=John;') == {'name': 'John'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=John;age=28;') == {'name': 'John', 'age': '28'}
    assert parse_cookie('name=John=User;age=28;') == {'name': 'John=User', 'age': '28'}