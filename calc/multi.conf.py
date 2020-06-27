SGIScriptAlias /multi /usr/local/sw1/multi.py
WSGIPythonPath /usr/local/sw1

<Directory "/usr/local/sw1">
        AllowOverride None
        Order deny,allow
        Require all granted
</Directory>

