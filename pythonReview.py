# main function for the video's details
def create_youtubevideo (title, description):
 	youtubevideo= {"title": title, "description":description, "likes": 0, "dislikes": 0, "comments":{}}
 	return youtubevideo

# adds to the like counter - function
def like(youtubevideo):
	youtubevideo["likes"] +=1
	return youtubevideo

# adds to the dislike counter - function
def dislike(youtubevideo):

	youtubevideo["dislikes"] +=1
	return youtubevideo

# adds a comment - function
def add_comment(youtubevideo, username, comment_text):
	# finds the comment and indside the comments dictionary it checks for a key and adds it if it isnt there and adds the value
	youtubevideo["comments"][username] = comment_text
	return youtubevideo

# testing - Omar's youtube video
Abu_Khaleds_yt_vid = create_youtubevideo("How To", "today we learn how to")
while Abu_Khaleds_yt_vid["likes"] < 495:
	Abu_Khaleds_yt_vid = like(Abu_Khaleds_yt_vid)

Abu_Khaleds_yt_vid = dislike(Abu_Khaleds_yt_vid)
Abu_Khaleds_yt_vid = add_comment(Abu_Khaleds_yt_vid, "Abu Sami", "I Disliked, because i am abu sami (Amir)")
Abu_Khaleds_yt_vid = add_comment(Abu_Khaleds_yt_vid, "Abu Eli", "Great Video bro, i loved it")

print(Abu_Khaleds_yt_vid["title"], "\n")
print("The amount of likes is:", Abu_Khaleds_yt_vid["likes"])
print("The amount of dislikes is:", Abu_Khaleds_yt_vid["dislikes"])
print("The commets are:", Abu_Khaleds_yt_vid["comments"])
