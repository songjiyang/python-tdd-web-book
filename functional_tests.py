from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
		header_test = self.brower.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_test)

		#应用邀请她输入一个代办事项
		inputbox = self.brower.find_element_by_id('id_new_item')
		self.assertEqual(
				inputbox.get_attribute('placeholder'),
				'Enter a to-do item'
			)

		#她在一个文本框输入了"Buy peacoak fethers"(购买孔雀羽毛)
		#伊迪斯的爱好是使用假蝇做饵钓鱼
		inputbox.send_keys('Buy peacock feathers')

		#他按回车键之后，页面更新了
		#代办事项表格中显示了"1: Buy peacock feathers"
		inputbox.send_keys(Keys.ENTER)
		table = self.brower.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
				any(row.text == '1: Buy peacock fethers' for row in rows),
				"New to-do item dit not appear in table"
			)

		#页面中又显示了一个文本框，可以输入其他的代办事项
		#她输入了"Use peacock feathers to make a fly"(使用孔雀羽毛做假蝇)
		#伊迪斯做事很有条理

		#页面再次更新，她的清单中显示了这两个代办事项

		#伊迪斯想知道这个网站是否会记住她的清单
		#她看到网站为她生成了一个唯一的URL
		#而且页面中有一些文字解说这个功能

		#她访问那个URL,发现她的代办事项还在

		#她很满意，去睡觉了
		self.fail('Finish the test!')
if __name__ == '__main__':
	unittest.main()