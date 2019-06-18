import pymysql
import xlrd

# import conversations

notes="""Do something to create table command every time client provides an excell sheet (Convert excell sheet to mysql-file (table) 
         For the first time inserting data keep the buffer no. of rows as 100 to improve the performance.
         Just read the file(Handle case when the user is logged in from different os too.)
"""

def improve_query(field):
    input_again = input()
    # Call again to improve query.
    sql(input_again, field)


def sql(user,field='name'):
    connection=pymysql.connect(host="localhost",user="Aditya",password="aditya956",database="aditya")
    cursor=connection.cursor()
    client_details=[]
    result=[]


    """We have a pre-defined table users.
        We only have 4 fields eid,name,phone,email.   Later update it.
        Below code works in this way---- 1st it asks name,if not clear phone,if not clear email,by now the end result is in front of us.
        But what if there are 100 fields?
    """
    #user variable gets updated after each call.(No point of asking the same question)
    client_details.append(user)
    question="Enter the "
    if field=='name':

        print(question+str(field))


        #sql="SELECT * FROM users where name LIKE " +''+user+";"
        sql_query="SELECT * "+" FROM Employee where Name='"+user+"';"
        #sql = "SELECT * FROM users;"


    elif field=='phone':
        print(question + str(field))
        sql_query = "SELECT Name" + " FROM Employee where Contact Number='" + user + "';"



    elif field=='email':
        print(question + str(field))
        sql_query = "SELECT Name" + " FROM Employee where Email ID='" + user + "';"

    question=question+str(field)
    print(sql_query)
    cursor.execute(sql_query)
    rows=cursor.fetchall()
    for row in rows:
        print(row)
        result.append(row)
    print(result)
    if result==[]:
        #No details can be fetched.
        print("Details are invalid")
        reply=""
        if field == 'name':
            reply="Enter the name more clearly"
            print(reply)
            #print("Enter the name more clearly")

        if field=='phone':
            reply="Enter the 10 digit phone number"
            print(reply)
            #print("Enter the 10 digit phone number")

        if field=='email':
            reply="Please provide the complete email-id"
            print(reply)
            #print("Please provide the complete email-id.")
        # conversations.conversation[question].append(reply)
        improve_query(field)
        # input_again = input()
        #     # Call again to improve query.
        # sql(input_again, field)

    elif len(result)>1:
        reply=""
        if field=='name':
            reply="Enter Phone Number"
            print(reply)
            #print("Enter Phone Number")
            field='phone'
        elif field =='phone':
            reply="Enter Email Id"
            print(reply)
            #print("Enter Email Id")
            field='email'
        conversations.conversation[question].append(reply)
        improve_query(field)
        # input_again=input()
        # #Call again to improve query.
        # sql(input_again,field)

    else:
        print(result[0][0])
        # print(conversations.conversation[question].append(result[0][0]))
    #print(conversations.conversation)
    # return conversations.conversation  #This returns all the conversations that we have back to logic.
    cursor.close()
    #connection.commit()
    connection.close()
    return result