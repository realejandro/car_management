from flask import jsonify

##Create a function to select the admin in base of the email or username
def assign_user_role(data):
    if data["role"] != "admin":
        return jsonify({
            "error": "the user cannot modify role"
        })
    
    

##Create a function to reduce the controller (route) of register a user
def permited_roles(data):
    if data["role"] not in ["admin", "buyer", "sales"]:
        return None, f"The role {data["role"]} doesn't exist"
    
    return data["role"], None


