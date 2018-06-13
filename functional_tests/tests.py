from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from django.test import LiveServerTestCase

class NewVistorTest(LiveServerTestCase):
	"""docstring for NewVistorTest"""
	def setUp(self):
		self.brower = webdriver.Chrome()	
		self.brower.implicitly_wait(3)		

	def tearDown(self):
		self.brower.quit()

	def check_for_row_in_list_table(self,row_text):
		table = self.brower.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])

	def test_can_start_a_list_and_retrive_it_later(self):
		self.brower.get(self.live_server_url)
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
		edith_list_url = self.brower.current_url
		self.assertRegex(edith_list_url,'/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		#页面中又显示了一个文本框，可以输入其他的代办事项
		#她输入了"Use peacock feathers to make a fly"(使用孔雀羽毛做假蝇)
		inputbox = self.brower.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		#页面再次更新，她的清单中显示了这两个代办事项                                               
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
		
		#现在一个叫弗朗西斯的新用户访问了网站

		##我们使用了一个新的浏览器会话
		##确保伊迪斯的信息不会从cookie中泄露出来
		self.brower.quit()
		self.brower = webdriver.Chrome()

		#弗朗西斯访问首页
		#页面看不到伊迪斯的清单
		self.brower.get(self.live_server_url)
		page_text = self.brower.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers',page_text)
		self.assertNotIn('make a fly',page_text)

		#弗朗西斯输入一个新代办事项
		#他不像伊迪斯那样兴趣盎然
		inputbox = self.brower.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)

		#弗朗西斯获得了他的唯一URL
		francis_list_url = self.brower.current_url
		self.assertRegex(francis_list_url,'/lists/.+')
		self.assertNotEqual(francis_list_url,edith_list_url)

		#这个页面还是没有伊迪斯的清单
		page_text = self.brower.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers',page_text)
		self.assertIn('Buy milk',page_text)

		#两个人都很满意，去睡觉了

