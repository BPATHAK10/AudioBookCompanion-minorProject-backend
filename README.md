# KATHAK backend

The backend server for the application is implemented using the Flask micro-framework
in Python. When the server is started, the configuration for the trained model is loaded
from a config file. Before listening to requests from the designated port, the server loads
the model using the configuration and stores it as a global variable. This prevents the
loading of the model from the disk to the memory of the GPU for each request. Al-
though this method reserves a certain portion of the memory of GPU constantly, this
seems to be the right option because it saves memory allocation and deallocation time
for the model for each request to the server. Then the server listens to the requests and
sends responses in the form of API. Every time a new data is sent for prediction, the
server replaces the data to be predicted in the model and recomputes the results.

## Technologies Used
### Flask

## Database
### SQL Alchemy

The database stores the User as well as Texts table entries. The user is a customer of the
application and Texts are the data inputs from the customer in the database. For creating and operating on database, SQLAlchemy has been used. It is a Structured Query Language(SQL) that provides easy functions to operate directly on records on the table.
