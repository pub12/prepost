import unittest

import sys
sys.path.insert(0, '../')

from prepost import PreCond, PostCond


class TestPre(unittest.TestCase):

	# print('sssss')
	def test_0010_equals_precondition_fail(self):              
		@PreCond.equals( fruit='xx' )
		def func_test(*, fruit, size):
			print(f"fruit={fruit} and size={size}")

		self.assertRaises(Exception, func_test, fruit='apple', size='1kg' )

	def test_0020_equals_precondition_success(self):              
		@PreCond.equals( fruit= 'apple' )
		def func_test(*, fruit, size):
			print(f"fruit={fruit} and size={size}")

		func_test( fruit='apple', size='1kg')


	def test_0030_equals_precondition_success_2(self):              
		@PreCond.equals( fruit= 'apple', size='1kg' )
		def func_test(*, fruit, size):
			print(f"fruit={fruit} and size={size}")

		func_test( fruit='apple', size='1kg')


	def test_0040_not_null_precondition_success(self):              
		@PreCond.not_null( ['fruit'] )
		def func_test(*, fruit, size):
			print(f"fruit={fruit} and size={size}")

		func_test( fruit='apple', size='1kg')

	def test_0041_not_null_precondition_fail(self):              
		@PreCond.not_null( ['fruit', 'size'] )
		def func_test(*, fruit, size):
			print(f"fruit={fruit} and size={size}")

		self.assertRaises(Exception, func_test, fruit='apple' )


	def test_0050_pre_dict_fields(self):              
		@PreCond.dict_has_fields( fruit_dict=['apple', 'banana']  )
		def func_test(*, fruit_dict):
			print(f"{fruit_dict}")

		self.assertRaises(Exception, func_test, fruit_dict={'apple':'1kg'} )

	def test_0060_minimum_not_null_fail(self):
		@PreCond.minimum_not_null( 1 )
		def func_test(*, fruit=None, avacado=None):
			print(f"{fruit}")

		self.assertRaises(Exception, func_test)

	def test_0070_minimum_not_success_1(self):
		@PreCond.minimum_not_null( 1 )
		def func_test(*, fruit=None, avacado=None):
			print(f"{fruit}")

		func_test( fruit="apple")

	def test_0080_minimum_not_success_2(self):
		@PreCond.minimum_not_null( 1 )
		def func_test(*, fruit=None, avacado=None):
			print(f"{fruit}")

		func_test( avacado="large")

	def test_0090_minimum_not_success_3(self):
		@PreCond.minimum_not_null( 1 )
		def func_test(*, fruit=None, avacado=None):
			print(f"{fruit}")

		func_test( fruit="apple", avacado="large")

	def test_0091_maches_pattern_kwargs(self):
		@PreCond.matches_pattern( fruit='^[a-zA-Z]+$')
		def func_test(*, fruit=None, avacado=None):
			print(f"{fruit}")

		func_test( fruit="apple")
		self.assertRaises(Exception, func_test, fruit="apple1")
		self.assertRaises(Exception, func_test, "apple1")

	def test_0092_maches_pattern_pos(self):
		@PreCond.matches_pattern( fruit='^[a-zA-Z]+$')
		def func_test( fruit):
			print(f"{fruit}")

		func_test( "apple")
		self.assertRaises(Exception, func_test, "apple1")
		



class TestPost(unittest.TestCase):
	def test_0100_post_not_null(self):              
		@PostCond.not_null()
		def func_test(*, fruit, size):
			print(f"fruit={fruit} and size={size}")

		self.assertRaises(Exception, func_test, fruit='apple', size='1kg' )
