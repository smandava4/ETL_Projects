To run the project: 
    python backend.py

Project Details: 
    Its a simple project that uses twitter api to get the user information ,
    (its a free tier app so only 3 api are accessible)
    Post a tweet into your account 
    Delete the tweet we just posted 

To delete:
    Copy the tweet id displayed on the screen use it as tweet id in the delete post 


API accesible:
    POST /2/tweets
    GET /2/users/me
    DELETE /2/tweets/:id

Authentication: 
    Uses the config files to pass the keys,token,secrets to create a client object and authenticates the user 

Backend:
    python --> Flask server
Front-end: 
    HTML 
    CSS 
    JS

Note: Since its a free tier api only our account is accessible via the api 