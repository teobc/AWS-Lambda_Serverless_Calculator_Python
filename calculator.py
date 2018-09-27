import json
import logging

def lambda_handler(event, context):
  # Show the incoming event in the debug log
    print("Event received by Lambda function: " + json.dumps(event, indent=2))
  
    # TODO implement
    response_success = calci(event,context)
    return response_success
    # return {
    #     # "statusCode": 200,
    #     # "body": json.dumps('Hello from Lambda!'),
    #     "result": response_success
    # }
    
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def add(event, context):
    logger.info("Event logged the following ", event)
    final={}
    final=event['queryStringParameters']
    a =float(final['a'])
    b=float(final['b'])
    c=a+b
    res = "the result is " +str(c)  
    response_success={ 
            "statusCode": 200,
            "body": json.dumps(res)
            }
    return response_success

def subtract(event, context):
    logger.info("Event logged the following ", event)
    final={}
    final=event['queryStringParameters']
    a =float(final['a'])
    b=float(final['b'])
    c=a-b
    res = "the result is " +str(c)
    response_success={
            "statusCode": 200,
            "body": json.dumps(res)
            }
    return response_success

def multiply(event, context):
    logger.info("Event logged the following ", event)
    final={}
    final=event['queryStringParameters']
    a =float(final['a'])
    b=float(final['b'])
    c=a*b
    res = "the result is " +str(c)
    response_success={
            "statusCode": 200,
            "body": json.dumps(res)
            }
    return response_success


def divide(event, context):
    logger.info("Event logged the following ", event)
    final={}
    final=event['queryStringParameters']
    a =float(final['a'])
    b=float(final['b'])
    c=a/b
    res = "the result is " +str(c)
    response_success={
            "statusCode": 200,
            "body": json.dumps(res)
            }
    return response_success


def calci(event,context):
    logger.info("Event logged the following:",event)
    if bool(event) ==True:
        logger.info("the events dict is not empty")
      

    res_error ={
        "statusCode": 404,
        "body": json.dumps("resource not found in input")
    }
    # dict1={}
    # dict1=event['queryStringParameters']
    # a = (dict1['a'])
    # b = (dict1['b'])
    # op = (dict1['op'])
    a = event['a']
    b = event['b']
    op = event['op']

    logger.info('the value of a is %s ', a)    
    logger.info('the value of b is %s', b)
    logger.info('the op is %s', op)
    a = float(a)
    b=float(b)


    c=0
    if op=='+':
        c=a+b
    if op=='-':
        c=a-b
    if op=='/':
        if b==0:
            c="Division by 0"
            return {"statusCode":200,"body": "Division by 0"}
        c=(a/b)
    if op=='*':
        c=a*b
    res = "Calculate: " +str(a) + " " +str(op) + " " +str(b) + ", the result is " +str(c)  
    response_success={ 
            "statusCode": 200,
            "body": json.dumps(res)
            }


    logger.debug( "response from calci is %s ", res)

    return response_success

# import json
# import logging

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)


# def add(event, context):
#     logger.info("Event logged the following ", event)
#     final={}
#     final=event['queryStringParameters']
#     a =float(final['a'])
#     b=float(final['b'])
#     c=a+b
#     res = "the result is " +str(c)  
#     response_success={ 
#             "statusCode": 200,
#             "body": json.dumps(res)
#             }
#     return response_success

# def subtract(event, context):
#     logger.info("Event logged the following ", event)
#     final={}
#     final=event['queryStringParameters']
#     a =float(final['a'])
#     b=float(final['b'])
#     c=a-b
#     res = "the result is " +str(c)
#     response_success={
#             "statusCode": 200,
#             "body": json.dumps(res)
#             }
#     return response_success

# def multiply(event, context):
#     logger.info("Event logged the following ", event)
#     final={}
#     final=event['queryStringParameters']
#     a =float(final['a'])
#     b=float(final['b'])
#     c=a*b
#     res = "the result is " +str(c)
#     response_success={
#             "statusCode": 200,
#             "body": json.dumps(res)
#             }
#     return response_success


# def divide(event, context):
#     logger.info("Event logged the following ", event)
#     final={}
#     final=event['queryStringParameters']
#     a =float(final['a'])
#     b=float(final['b'])
#     c=a/b
#     res = "the result is " +str(c)
#     response_success={
#             "statusCode": 200,
#             "body": json.dumps(res)
#             }
#     return response_success

# '''
# def calci(event,context):
#     logger.info("Event logged the following:",event)
#     if bool(event) ==True:
#         logger.info("the events dict is not empty")
      

#     res_error ={
#         "statusCode": 404,
#         "body": json.dumps("resource not found in input")
#     }
#     dict1={}
#     dict1=event['queryStringParameters']
#     a = (dict1['a'])
#     logger.info('the value of a is %s ', a)
#     b = (dict1['b'])
#     op = (dict1['op'])
#     logger.info('the value of b is %s', b)
#     logger.info('the op is %s', op)
#     a = float(a)
#     b=float(b)


#     c=0
#     if op=='+':
#         c=a+b
#     if op=='-':
#         c=a-b
#     if op=='/':
#         if b==0:
#             c="Division by 0"
#             return {"statusCode":200,"body": "Division by 0"}
#         c=(a/b)
#     if op=='*':
#         c=a*b
#     res = "the result is " +str(c)  
#     response_success={ 
#             "statusCode": 200,
#             "body": json.dumps(res)
#             }


#     logger.debug( "response from calci is %s ", res)

#     return response_success
# '''
