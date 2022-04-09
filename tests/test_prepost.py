import unittest

import sys
sys.path.insert(0, '../')

from prepost import PreCond, PostCond


class TestPre(unittest.TestCase):

	# print('sssss')
	def test_equals_precondition_fail(self):              
		@PreCond.equals( {'fruit':'xx'} )
		def func_test(*, fruit, size):
			print(f"fruit={fruit} and size={size}")

		self.assertRaises(Exception, func_test, fruit='apple', size='1kg' )

	def test_equals_precondition_success(self):              
		@PreCond.equals( {'fruit':'apple'} )
		def func_test(*, fruit, size):
			print(f"fruit={fruit} and size={size}")

		func_test( fruit='apple', size='1kg')

	def test_not_null_precondition_success(self):              
		@PreCond.not_null( ['fruit'] )
		def func_test(*, fruit, size):
			print(f"fruit={fruit} and size={size}")

		func_test( fruit='apple', size='1kg')

	def test_not_null_precondition_fail(self):              
		@PreCond.not_null( ['fruit', 'size'] )
		def func_test(*, fruit, size):
			print(f"fruit={fruit} and size={size}")

		self.assertRaises(Exception, func_test, fruit='apple' )



class TestPost(unittest.TestCase):
	def test_post_not_null(self):              
		@PostCond.not_null()
		def func_test(*, fruit, size):
			print(f"fruit={fruit} and size={size}")

		self.assertRaises(Exception, func_test, fruit='apple', size='1kg' )
