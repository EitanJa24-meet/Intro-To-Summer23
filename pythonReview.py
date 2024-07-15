def create_youtubevideo (title, description):
 	youtubevideo= {"title": title, "description":description, "likes": 0, "dislikes": 0, "comments":{}}
 	return youtubevideo

def like(youtubevideo):
	youtubevideo["likes"] +=1
	return youtubevideo

def dislike(youtubevideo):

	youtubevideo["dislikes"] +=1
	return youtubevideo

def add_comment(youtubevideo, username, comment_text):
	if "comments" not in youtubevideo:
		youtubevideo["comments"] = {}
	youtubevideo["comments"][username] = comment_text
	return youtubevideo

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
