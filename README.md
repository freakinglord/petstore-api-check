# petstore-api-check
API automated check over PET store https://petstore.swagger.io

## Prerequisites  
- Install Python 3
- Install pip


## Instructions on how to add to integration testing to TeamCity
1) Create a build and add this repo to VCS registry. 
2) create a build step and select CommandLine 
3) in script block, run the following:
    1) pip install -r requirements.txt
    2) pytest test-petstore-swagger-api.py
4) save the build step
5) run the build
6) once verified that build runs smoothly, set a VCS trigger, so it would trigger when there are changes to the repository. 