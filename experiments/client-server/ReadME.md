## How to install

1. create a conda virtual environment
```conda create --name  csci680 --file requirements.txt```

2. activate the environment
```conda activate csci680```

3. start the server. Go to the server directory and run
```python3 app.py```

4. How to upload a file to server
```curl -F file=@<file path> http://127.0.0.1:5000/upload```

5. create a directory called downloads in the client directory

6. How to download a file from server
```curl -o downloads/<file name> http://127.0.0.1:5000/download/<file name>```