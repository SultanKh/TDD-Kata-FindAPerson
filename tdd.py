import unittest

class TestCrowdmap(unittest.TestCase):
        def test_crowdmapForPerson_returns_allPosts(self):
                crowdmap=Crowdmap()
                posts=crowdmap.getAllPostsFor("Or")
                self.assertEquals(posts,["I met Or A. at Chabad house Bangladish, we found Or A. R.I.P at Langtand"])
