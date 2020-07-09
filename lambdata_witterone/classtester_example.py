# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 12:52:12 2020

@author: Ronin
"""

import unittest
from oop_examples import SocialMediaUser
from random import randint


class SocialMediaUser_test (unittest.TestCase):
    
    def test_name(self):
        user1 = SocialMediaUser('Jane')
        user2 = SocialMediaUser('Joe')
        self.assertEqual(user1.name, 'Jane')
        self.assertEqual(user2.name, 'Joe')
    
    def test_default_upvotes(self):
        """Test that the default upvotes of a new user is 0."""
        user1 = SocialMediaUser('Jane')
        self.assertEqual(user1.upvotes, 0)
        
    def test_unpopular(self):
        """Test that a user with <=100 upvotes is not popular."""
        user1 = SocialMediaUser('Joe')
        for _ in range(randint(1, 100)):
            user1.receive_upvote()
        self.assertEqual(user1.is_popular(), False)
        
    def test_popular(self):
        """Test that a user with >100 upvotes is popular."""
        user1 = SocialMediaUser('Jane')
        for _ in range(randint(101, 1000)):
            user1.receive_upvote()
        self.assertEqual(user1.is_popular(), True)

if __name__ == '__main__':
    unittest.main()