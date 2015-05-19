import unittest
from crowdMap import Crowdmap

class TestCrowdmap(unittest.TestCase):
        def test_crowdmapForPerson_returns_allPosts(self):
                crowdmap=Crowdmap()
                posts=crowdmap.getAllPostsFor("Or")
                self.assertEquals(["I met Or A. at Chabad house Bangladish, we found Or A. R.I.P at Langtand"],posts)
		def test_MissingPerson_returns_EmptyList(self):
                crowdmap=Crowdmap()
                posts=crowdmap.getAllPostsFor("Sultan")
                self.assertEquals(posts,[])
		def test_PersonHasLocation_returns_Bool(self,loc):
                crowdmap=Crowdmap()
                posts=crowdmap.getAllPostsFor("Or")
                return len(posts)!=0
				
		def test_mapInconsistencies_returns_Bool(self):
                crowdmap=Crowdmap()
                posts=self.crowdmap.mapInconsistenciesExist("Or")
                self.assertTrue(mapInconsiste)
				
	class Crowdmap:
        def getAllPostsFor(self,name):
                return ["I met Or A. at Chabad house Bangladish, we found Or A. R.I.P at Langtand"]
	
	class Locations():
		def __init__(self):
			self.Locations=['Bangladish','Langtand']
	
	if __name__ == '__main__':
        unittest.main()