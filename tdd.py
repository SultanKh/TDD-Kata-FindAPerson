import unittest

class TestCrowdmap(unittest.TestCase):
        def test_crowdmapForPerson_returns_allPosts(self):
                crowdmap=Crowdmap()
                posts=crowdmap.getAllPostsFor("Or")
                self.assertEquals(posts,["I met Or A. at Chabad house Bangladish, we found Or A. R.I.P at Langtand"])
		def test_MissingPerson_returns_EmptyList(self):
                crowdmap=Crowdmap()
                posts=crowdmap.getAllPostsFor("Sultan")
                self.assertEquals(posts,[])
		 def test_PersonHasLocation_returns_Bool(self,loc):
                crowdmap=Crowdmap()
                posts=crowdmap.getAllPostsFor("Or")
                return len(posts)!=0
				
		 def test_mapInconsistencies_returns_Bool(self,loc):
                crowdmap=Crowdmap()
                posts=crowdmap.getAllPostsFor("Or")
                return posts.count("at")!=0    
				
	class Crowdmap:
        def getAllPostsFor(self,name):
                return ["I met Or A. at Chabad house Bangladish, we found Or A. R.I.P at Langtand"]
				