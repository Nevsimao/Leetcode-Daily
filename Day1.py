DVDcollection = [None]*5

class DVD:
    def __init__(self, name, releaseYear, director):
        self.name = name
        self.releaseYear = str(releaseYear)
        self.director = director
    
incrediblesDVD = DVD('The Incredibles', 2004, 'Brad Bird')
findingDoryDVD = DVD('Finding Dory', 2016, 'Andrew Stanton')
lionKingDVD = DVD('The Lion King', 2019, 'Jon Favreau')
starWarsDVD = DVD("Star Wars", 1977, "George Lucas")

new0DVD = (incrediblesDVD.name, incrediblesDVD.releaseYear, incrediblesDVD.director)
new1DVD = (findingDoryDVD.name, findingDoryDVD.releaseYear, findingDoryDVD.director)
new2DVD = (lionKingDVD.name, lionKingDVD.releaseYear, lionKingDVD.director)
new3DVD = (starWarsDVD.name, starWarsDVD.releaseYear, starWarsDVD.director)

DVDcollection[0] = new0DVD
DVDcollection[1] = new1DVD
DVDcollection[2] = new2DVD
DVDcollection[2] = new3DVD

print(DVDcollection[2])
