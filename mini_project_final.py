#START

#movie data file
movie=open('C:\\Users\\USER\\Desktop\\movies.txt','r')
data=movie.read()

#rating data file
rating=open('C:\\Users\\USER\\Desktop\\rating.txt','r')
rate=rating.read()

#rating elements
list_for_ratings=['Movie_id','Rating']

#movies attributes
list_for_movies=['Movie_id','Movie_name','Genre','Year']

#used set() to retrive only unique values
Genre=set()
Year=set()

#empty list of datal1, moviedata, ratingdata
temporary_list2=[]
data_list=[]


#operations on movie txt file
temporary_list=data.split("\n")
for i in range(len(temporary_list)):
               temporary_list2.append(temporary_list[i].split(","))
               
for j in range(len(temporary_list2)):
               data_list.append(dict(zip(list_for_movies,temporary_list2[j])))
               
for i in range(len(temporary_list2)):
               data_list[i]["Genre"]=temporary_list2[i][2].split("|")
               

#operations on rating txt file
               
rate_list=[]
temporary_list2.clear()

temporary_list=rate.split("\n")

for i in range(len(temporary_list)):
    temporary_list2.append(temporary_list[i].split(","))
    
for j in range(len(temporary_list2)):
    rate_list.append({list_for_ratings[i]:float(temporary_list2[j][i]) for i in range(len(list_for_ratings))})
    
              
movie.close() #access is terminated
rating.close()  #access is terminated


#Set1 for Genre

for i in range(len(data_list)):
        Genre.update(x for x in data_list[i]["Genre"])
#print(genre)

        
#set2 for year
        
for i in range(len(data_list)):
        Year.update(x for x in [data_list[i]["Year"]])


'''Things to do,

1.count of movies for each genre.
2.count of movies for each genre having rating greater than 4.
3.count of movies that was released after 2000 having genre as sci-fi and rating >3.5
4.find the top movie of each genre.
5.find top movie in each year.

'''

#1st
count1=0
print("====(1):-Count Movie For Each Genre-:(1)====\n")
for each in Genre:
    for i in range(len(data_list)):
        if each in data_list[i]["Genre"]:
            count1+=1       
    print(each,":",count1 )
    count1=0

print("                                                        ")
#2nd
count2=0
print("====(2):-Count Of Movie For Each Genre Having Rating Greater Than '4'-:(2)====\n")
for each in Genre:
    for i in range(len(data_list)):
        if each in data_list[i]["Genre"]:
            if rate_list[i]["Rating"]>4:
                count2+=1
    if count2!=0:
        print(each, ":", count2)
        count2=0

print("                                                        ")

#3rd
count3=0
print('====(3):-count of movies that was released after 2000 having genre as sci-fi and rating >3.5-:(3)=====\n')
for each in Genre:
    for i in range(len(data_list)):
        if int(data_list[i]["Year"])>2000:
            if each in data_list[i]["Genre"]:
                if rate_list[i]["Rating"]>3.5:
                    count3+=1
    if count3>0:
        print(each, ":",count3)
        count3=0       

print("                                                        ")

#4th
top=0
print("====(4):-Top Movie For Each Genre-:(4)====\n")
for each in Genre:
    for i in range(len(data_list)):
        if each in data_list[i]["Genre"]:
            if rate_list[i]["Rating"]>top:
                top=rate_list[i]["Rating"]
                m_name=data_list[i]["Movie_name"]
    if top!=0:
        print("The best",each,"Movie is :",m_name)
        top=0
        m_name=0

print("                                                        ")

#5th        
hits=0
print("====(5):-Top Movies In Each Year-:(5)====\n")
for each in Year:
    for i in range(len(data_list)):
        if each in str(data_list[i]['Year']):
            if rate_list[i]["Rating"]>hits:
                hits=rate_list[i]["Rating"]
                m_names=data_list[i]["Movie_name"]
    if hits!=0:
        print("Top movie of",each,"was :",m_names)
        hits=0
        m_names=0        

#END
