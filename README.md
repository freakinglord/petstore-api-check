# petstore-api-check
API automated check over PET store https://petstore.swagger.io

## Prerequisites  
- Python 3


## Instructions on how to add to integration testing to TeamCity
1) Create a build and add this repo to VCS registry.
2) create a build step and select CommandLine 
3) in script block, run the following:
    1) pip install -r requirements.txt
    2) pytest test-petstore-swagger-api.py
4) save the build step
5) run the build