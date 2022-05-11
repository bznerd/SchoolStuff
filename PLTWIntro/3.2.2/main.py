"""
Ben Campbell
Third Period
3.2.2 Social Media app
"""

#import Post module
import Post

#Take passed user and post archive and add a new post
def addPost(user, archive):
    archive.append(Post.Post(user, input("Enter your post message:\n")))

#Take passed user and archive and allow the user to select a post to delete
def removePost(user, archive):
    print("Posts are: ")
    #Loop and print all posts with their ids
    for post in archive:
        print(f"ID: {post.get_post_id()}, Post: {post}")
    #Get the id from the user
    postID = input("\nEnter ID of post you would like to delete: (-1 to cancel)\n")
    #Catch not a number
    if not postID.isnumeric():
        print("Enter a number please")
        return removePost(user, archive)
    postID = int(postID)
    #Catch id bounds
    if postID not in [post.get_post_id() for post in archive]:
        print("Invalid ID try again\n")
        return removePost(user, archive)
    #Convert ID to an index:
    index = [post.get_post_id() for post in archive].index(postID)
    #Cancel case
    if index == -1: return
    #Catch if user is removing another user's post
    elif user != archive[index].get_user_name():
        print("You cannot edit other users' posts\n")
        return
    #Remove post
    else: del archive[index]

#Take passed user and post archive and edit a post
def editPost(user, archive):
    print("Posts are: ")
    #Loop and print all posts with their ids
    for post in archive:
        print(f"ID: {post.get_post_id()}, Post: {post}")
    #Get the od from the user
    postID = input("\nEnter ID of post you would like to edit: (-1 to cancel)\n")
    #Catch not a number
    if not postID.isnumeric():
        print("Enter a number please")
        return editPost(user, archive)
    postID = int(postID)
    #Catch id bounds
    if postID not in [post.get_post_id() for post in archive]:
        print("Invalid ID try again\n")
        return editPost(user, archive)
    #Convert ID to an index:
    index = [post.get_post_id() for post in archive].index(postID)
    #Cancel case
    if index == -1: return
    #Catch if user is removing another user's post
    elif user != archive[index].get_user_name():
        print("You cannot edit other users' posts\n")
        return
    #Change post message to user input
    else:
        archive[index].message = input("Enter new message:\n")

#Change user name
def changeUser(user):
    user_in = input("Enter new user name (blank to cancel)")
    #If blank reset to the previous username
    if user_in == "": return user
    return user_in

#Print out list of posts from an archive
def printPosts(archive):
    print("\nPosts in archive are:")
    #Loop through archive printing posts
    for post in archive: print(post)

#Archive of posts
archive = []

#Welcome and set user name
print("Welcome to pyPost\n")
user = input("Enter a username:\n")
print(f"Welcome {user}\n")

#Loop program
while True:
    #Get user action each loop
    user_input = input("""\nWhat would you like to do?
"add" - Add a post to the archive
"remove" - Remove a post from the archive
"edit" - Edit a post made by you
"change user" - Change the user name associated with any future posts
"print" - Display the current up to date list of all posts
"quit" - End the program\n
""").lower().replace(" ","")

    #Case conditionals, runs appropriate function for user input (break for quit and nothing for invalid input)
    if user_input == "quit": break
    elif user_input == "add": addPost(user,archive)
    elif user_input == "remove": removePost(user, archive)
    elif user_input == "edit": editPost(user, archive)
    elif user_input == "changeuser": user = changeUser(user)
    elif user_input == "print": printPosts(archive)
    else: print("Not a valid option please try again")

#After user quits
print("Bye bye!")