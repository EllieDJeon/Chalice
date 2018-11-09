# Create a new api

## Set up the virtualenv . 
```
virtualenv venv --python=python3
deactivate
source venv/bin/activate
pip list
pip install chalice
pip install boto3
pip install numpy
pip install pandas
cp requirements.txt cp_requirements.txt
pip freeze > requirements.txt
chalice deploy --no-autogen-policy
```

## Api list . 
### 1. Get a id token .
This api will get the **id token for the ES api**.  
```
cd /Users/dajeongjeon/Desktop/CarVi/environment_qa/test/microservice/chalice/qa-chalice  
chalice deploy --no-autogen-policy 
```

### 2. Get a address from location . 
This api will get the **exact address** from latitude and longitude info.  
```
cd /Users/dajeongjeon/Desktop/CarVi/environment_loc/test/microservice/chalice2/test70-chalice  
chalice deploy --no-autogen-policy 
```
