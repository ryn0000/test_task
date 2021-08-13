from flask import Flask,render_template,Blueprint,url_for,request
import logging
import requests
import json
from json import dumps
import redis



##MKAD coordinates
X1_add=37.329
X2_add=37.895
Y1_add=55.917
Y2_add=55.503

## get targer cordinates and check inside of mkad or out of mkad
## and writes the results to the result0.log file
while True:
    
    x= float(input("Coordinate X:"))
    y= float(input("Coordinate y:"))

    if x>X1_add and x<X2_add:
        if y>Y2_add and y<Y1_add:
            

            logging.basicConfig(filename="result0.log",format='%(message)s')

            logger= logging.getLogger()

            logger.setLevel(logging.DEBUG)
            
            logger.info(f"{x} , {y} location inside the MKAD")
            
            print("CHECK LOG FILE")

    else:
        break





app= Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    
    data={'cordiX':x,'cordiY':y}

    return render_template('index.html',data=data)



## get distance result from javascript 
## and writes the results to the result0.log file
@app.route('/dis',methods=['POST', 'GET'])
def dis():
    
    information= request.data
    distance= str(information)
    print("********************\n\n\n")
    print(f"{x} {y} to MKAD  {distance}\n\n\n")
    print("CHECK LOG FILE")
    print("********************\n\n\n\n")


    logging.basicConfig(filename="result0.log",format='%(message)s')

    logger= logging.getLogger()
    
    logger.setLevel(logging.DEBUG)
    if x<X1_add or x>X2_add:
        if y<Y2_add or y>Y1_add:  
            logger.info(f"{x} {y} to MKAD  {distance} ")
    

  
 
    return "1"
  
   






if __name__=='__main__':

    app.run(host="0.0.0.0")
   



