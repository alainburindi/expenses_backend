create_user = '''mutation{{
            createUser(email: "{email}", username: "{username}",
             password: "{password}"){{
                message
                user{{
                    email
                    username
                }}
            }}
        }} '''

login_user = '''
mutation{{
  loginUser(email: "{email}", username:"{username}", password:"{password}"){{
    message
    authToken
    }}
  }}
'''

login_empty_email_and_username = '''
mutation{
  loginUser(password:"password234"){
    message
    authToken
    }
  }
'''

get_logged_in_user = '''
query{
  me{
    email
    username
    isActive
  }
}
'''
