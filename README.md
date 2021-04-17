
# samplebackend

##### Project Installation Script

```
cd path/to/project/folder
./install.sh
```

##### Project Migration Script

```
cd path/to/project/folder
./migrate.sh
```

The script will install all required packages from pip and do server migration.

##### Packages installed from script

- django ( 2.2 )
- djangorestframework ( 3.10.3 )
- django-cors-headers ( 3.4.0 )
- python-json-logger ( 0.1.11 )
- requests
     
##### Running Server

```
python manage.py runserver
```

##### Make sure python environment is properly configured with python 3.7+. 
##### Working over pycharm is preferred

# Project Structure
#### Python Packages:

- `src`: This will be application for backend project samplebackend. i.e All models, controllers and views will be stores inside src folder.
- `src/lib`: Libraries for custom exception handler, custom response, authentication class and loggin class will be stored inside src/lib folder.
- `src/models`: The python package will hold all Models related to project.
- `src/views`: The python package will hold all Views related to project.
- `src/controllers`: The python package will hold all Controllers related to project.
- `logs`: API logs store location

#### Project Files :
    
- `src/lib/customexceptionhandler.py`: The module is responsible for handling exceptions.
- `src/lib/customresponse.py`: The module is responsible for returning JSON Response.
- `src/lib/loggingmixin.py`: The class is responsible for handling API Logs.
- `src/lib/authentication.py`: Authentication class 
- `src/lib/permissions.py`: Permission class
- `src/views/statusview.py`: Sample view showing api status, can be excessed using http://localhost:8000/
- `src/views/helpers.py`: Helper functions will be stored here
- `requirements`: Python Package Requirements file.


## API's

### Status API
`GET`: `http://localhost:8000/`

##### Response
```
{
  "status": true,
  "payload": true,
  "message": "Server Is Up and Running"
}
```

## ClientLogin API
`POST`: `http://localhost:8000/v1/login/`

#### Headers
{ Content-type: application/json }


#### Request Data
```
{
    "email": "User Email",
    "password": "User Password"
}
```

#### Response
```json
{
  "status": true,
  "payload": [
    {
      "_id": 1,
      "name": "NAME",
      "email": "EMAIL",
      "token": "GENERATED_USER_TOKEN",
      "_created": "2021-03-14 12:32:59.998882",
      "_updated": "2021-03-14 12:32:59.998909"
    }
  ],
  "message": "Login Api view"
}
```
#### Error Missing Key

```
# Response
{
  "status": false,
  "payload": null,
  "message": "Missing Key 'KEY_NAME' in request data",
  "error": {
    "code": 400
  }
}
```
#### Error Email Does Not Exits ( Email is not present in DB while trying to login )

```
{
  "status": false,
  "payload": null,
  "message": "Email Does not exits",
  "error": {
    "code": 400
  }
}
```
#### Error Password didn't Match

```
{
  "status": false,
  "payload": null,
  "message": "Invalid Password!",
  "error": {
    "code": 400
  }
}
```

## ClientSignup API
`POST`: `http://localhost:8000/v1/signup/`

#### Headers
`{ Content-type: application/json }`

#### Request Data
```
{
  "email": "EMAIL",
  "password": "PASSWORD",
  "name": "NAME",
  "type": "TYPE"
}
```

#### Response
```json
{
  "status": true,
  "payload": [
    {
      "_id": 1,
      "name": "NAME",
      "email": "EMAIL",
      "token": "GENERATED_USER_TOKEN",
      "_created": "2021-03-14 12:32:59.998882",
      "_updated": "2021-03-14 12:32:59.998909"
    }
  ],
  "message": "Signup Api view"
}
```
#### Error Missing Key

```
# Response
{
  "status": false,
  "payload": null,
  "message": "Missing Key 'KEY_NAME' in request data",
  "error": {
    "code": 400
  }
}
```
#### Error User Already Exits ( Email is already present in DB while trying to signup )

```
{
  "status": false,
  "payload": null,
  "message": "User already exits, Try login in",
  "error": {
    "code": 400
  }
}
```
