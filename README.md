```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Generating the files
```
python -m grpc_tools.protoc -I./pb --python_out=. --grpc_python_out=. ./pb/profile.proto
```
