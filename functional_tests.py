from selenium import webdriver
import unittest

class NewVistorTest(unittest.TestCase):
	"""docstring for NewVistorTest"""
	def setUp(self):
		self.brower = webdriver.Chrome()	
		self.brower.implicitly_wait(3)		

	def tearDown(self):
		self.brower.quit()

	def test_can_start_a_list_and_retrive_it_later(self):
		self.brower.get('http://localhost:8000')
		#头部和标题都包含"To-Do"这个词
		self.assertIn('To-Do',self.brower.title)
		self.fail('Finish the test!')

		#应用邀请她输入一个代办事项


		#她在一个文本框输入了"Buy peacoak fethers"(购买孔雀羽毛)
		#伊迪斯的爱好是使用假蝇做饵钓鱼

		#他按回车键之后，页面更新了
		#代办事项表格中显示了"1: Buy peacock feathers"

		#页面中又显示了一个文本框，可以输入其他的代办事项
		#她输入了"Use peacock feathers to make a fly"(使用孔雀羽毛做假蝇)
		#伊迪斯做事很有条理


		#页面再次更新，她的清单中显示了这两个代办事项

		#伊迪斯想知道这个网站是否会记住她的清单
		#她看到网站为她生成了一个唯一的URL
		#而且页面中有一些文字解说这个功能

		#她访问那个URL,发现她的代办事项还在

		#她很满意，去睡觉了

if __name__ == '__main__':
	unittest.main()