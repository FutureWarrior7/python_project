import pandas as pd
import matplotlib.pyplot as plt
from datetime import date


def addnewbook():
	bookid=int(input("Enter a bookid: "))
	title=input("Enter title:")
	author=input("Enter author:")
	publisher=input("Enter publisher:")
	cost=int(input("Enter cost:"))
	category=input("Enter category:")
	bdf=pd.read_csv(r"#location\\book.csv")
	n=bdf["bookid"].count()
	bdf.at[n]=[bookid,title,author,publisher,cost,category]
	bdf.to_csv(r"#location\\book.csv",index=False)
	print("Book added")
	print(bdf)


def delete_book():
	bookid=float(input("Enter a bookid"))
	bdf=pd.read_csv(r"#location\\book.csv")
	bdf=bdf.drop(bdf[bdf["bookid"]==bookid].index)
	bdf.to_csv(r"#location\\book.csv",index=False)
	print("Book deleted")
	print(bdf)

def search_book():
	title=input("Emter title:")
	bdf=pd.read_csv(r"#location\\book.csv")
	df=bdf.loc[bdf["title"]==title]
	if df.empty:
		print("no book found")
	else:
		print("Book details are : ")
		print(df)

def showbooks():
	bdf=pd.read_csv(r"#location\\book.csv")
	print(bdf)

def addNewMember():
	mid=int(input("Enter mem id:"))
	mname=input("Enter mem name: ")
	phno=int(input("Enter phn no: "))
	numberofbooksissued=0
	mdf=pd.read_csv(r"#location\\member.csv")
	n=mdf["mid"].count()
	mdf.at[n]=[mid,mname,phno,numberofbooksissued]
	mdf.to_csv(r"#location\\member.csv",index=False)
	print("member added ")
	print(mdf)
	
def searchMember():
	mname=input("Enter mem name: ")
	bdf=pd.read_csv(r"#location\\member.csv")
	df=bdf.loc[bdf["mname"]==mname]
	if df.empty:
		print("No member found")
	else:
		print("Member details are: ")
		print(df)

def deleteMember():
	mid=float(input("Enter member id: "))
	bdf=pd.read_csv(r"#location\\member.csv")
	bdf=bdf.drop(bdf[bdf["mid"]==mid].index)
	bdf.to_csv(r"#location\\member.csv",index=False)
	print("member deleted successfully")
	print(bdf)
	
def showMembers():
	bdf=pd.read_csv(r"#location\\member.csv")
	print(bdf)

def issuebooks():
	book_name=input("Enter a book name: ")
	bdf=pd.read_csv(r"#location\\book.csv")
	bdf=bdf.loc[bdf["title"]==book_name]
	if bdf.empty:
		print("No book found")
		return
	m_name=input("Entet member name: ")
	mdf=pd.read_csv(r"#location\\member.csv")
	mdf=mdf.loc[mdf["m_name"]==m_name]
	if mdf.empty:
		print("No such member")
		return
	
	dateofissue=int(input("Enter date : "))
	numberofissuedbooks=int(input("Enter no. of books issued: "))
	bdf=pd.read_csv(r"#location\\issuebooks.csv")
	n=bdf["book_name"].count()
	bdf.at[n]=[book_name,m_name,date.today(),numberofissuedbooks,""]
	bdf.to_csv(r"#location\\issuebooks.csv",index=False)
	print("book issued")
	print(bdf)

def returnbook():
	m_name=input("Enter member name: ")
	book_name=input("Enter book name: ")
	idf=pd.read_csv(r"#location\\issuebooks.csv")
	idf=idf.loc[idf["book_name"]==book_name]
	if idf.empty:
		print("Book is not issued")
	else:
		idf.loc[idf["m_name"]==m_name]
		if idf.empty:
			print("This book is not issued to the member")
		else:
			print("Book can be returned")
			ans=input("Are you sure to return: ")
			if ans.lower()=="yes":
				idf=pd.read_csv(r"#location\\issuebooks.csv")
				idf=idf.drop(idf[idf["book_name"]==book_name].index)
				idf.to_csv(r"#location\\issuebooks.csv",index=False)
				print("Book returned")
			else:
				print("Return operation cancelled")

def showissuedbooks():
	idf=pd.read_csv(r"#location\\issuebooks.csv")
	print(idf)

def deleteissuedbooks():
	book_name=input("Enter a book name: ")
	bdf=pd.read_csv(r"#location\\issuebooks.csv")
	bdf=bdf.drop(bdf[bdf["book_name"]==book_name].index)
	bdf.to_csv(r"#location\\issuebooks.csv",index=False)
	print("Deleted issued book successfully")
	print(bdf)

def showCharts():
	print("Press 1 for books and cost")
	print("Press 2 for the number of books issued by Members")
	ch=int(input("Enter a choice: "))
	if ch==1:
		df=pd.read_csv(r"#location\\book.csv")
		df=df[["title","cost"]]
		df.plot("title","cost",kind='bar')
		plt.xlabel("title--->")
		plt.ylabel("cost--->")
		plt.show()
	else:
			df=pd.read_csv(r"#location\\issuebooks.csv")
			df=df[["numberofbooksissued","mname"]]
			df.plot(kind="bar",color="red")
			plt.show()

def login():
	uname=input("Enter username : ")
	pwd=int(input("Enter password: "))
	df=pd.read_csv(r"#location\\user.csv")
	df=df.loc[df["username"]==uname]
	if df.empty:
		print("Invalid username given")
		return False
	else:
		df=df.loc[df["password"]==pwd]
		if df.empty:
			print("Invalid password")
			return False
		else:
			print("Username and password matched successfully")
			return True
def showmenu():
	print("NATIONAL LIBRARY ASSOSIATION")
	print("1-add new book")
	print("2-search for book")
	print("3-delete book")
	print("4-show all book")
	print("5-add new member")
	print("6-search member")
	print("7-delete member")
	print("8-show all member")
	print("9-issue a book")
	print("10-return a book")
	print("11-show all issued books")
	print("12-delete issued book")
	print("13-to view charts")
	print("14-to exit")
	choice=int(input("Enter: "))
	return choice
if login():
	while True:
		ch=showmenu()
		if ch==1:
			addnewbook()
		elif ch==2:
			search_book()
		elif ch==3:
			delete_book()
		elif ch==4:
			showbooks()
		elif ch==5:
			addNewMember()
		elif ch==6:
			searchMember()
		elif ch==7:
			deleteMember()
		elif ch==8:
			showMembers()
		elif ch==9:
			issuebooks()
		elif ch==10:
			returnbook()
		elif ch==11:
			showissuedbooks()
		elif ch==12:
			deleteissuedbooks()
		elif ch==13:
			showCharts()
		elif ch==14:
			break
		else:
			print("Invalid")
print("Thank You")