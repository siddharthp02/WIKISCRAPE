import requests,bs4
base_url = 'https://en.wikipedia.org/wiki/{}'
flag = True
count = 0
while(flag):
    search = input("Enter search")
    search = search.split()
    search = "_".join(search)
    print(base_url.format(search))


    try:
        res = requests.get(base_url.format(search))
    #     res = requests.get("https://en.wikipedia.org/wiki/isac")
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)


# res = requests.get("https://en.wikipedia.org/wiki/Isaac_Newton")
# res = requests.get("https://en.wikipedia.org/wiki/Great_Famine_(Ireland)")
# res = requests.get(base_url.format(search))
    soup = bs4.BeautifulSoup(res.text)

  
    if(len(soup.select(".toctext")) == 0):
        print("Invalid link")
    else:
        flag = False
        
for pos,item in enumerate(soup.select(".toctext"),1):
    if(item.text == "External links"):
        break
    count+=1
    print(pos," : ",item.text)

#choose item
exit = True
while(exit):
    flag = True
    while(flag):
        n = input("Enter the subtopic you want\n")
        if(n.isdigit()):
            if(int(n) <= count and int(n) >0):
                flag = False
                n = int(n)
            else:
                print("lmao")
        else:
            print("lmao")

    headlines = soup.select(".mw-headline")

    first_link = soup.find_all(class_ = "mw-headline")[n-1]


    #find all elements of type that come after
    ans = first_link.find_all_next(["p","span","li"])

    #output
    print("\n\n")

    #check whether firstlink.parent is h3 or h2
    #if parents is h2, then print all paragraphs and h3 until the next h2.
    #if parents is h3, then print all paragraphs until next h2 or h3
    print(first_link.text)
    print()


    if(first_link.parent.name == "h3" or first_link.parent.name == "h4"):
        for item in ans:
            if(item != first_link.find_next(class_ = "mw-headline")):
                print(item.text)
            else:
                break

    elif(first_link.parent.name == "h2"):
        for item in ans:
            if(item.parent != first_link.find_next("h2")):
                if((item.name == "span" and item in headlines) or item.name == "p" or (item.name == "li" and (item.parent.parent.name == "div"))):
                    print(item.text)
                else:
                    pass
            else:
                break
    ans = True
    while(ans):
        ans = input("Search again? 1 for yes, 0 for no.")
        if(ans!= "1" and ans!="0"):
            print("Invalid input, enter again.")
        else:
            if(ans == "1"):
                pass
            else:
                exit = False
            ans = False
            