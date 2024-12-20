# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCrudnotepad():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_crudnotepad(self):
    self.driver.get("http://127.0.0.1:5000/login?next=%2Fnotepad")
    self.driver.set_window_size(1854, 1011)
    self.driver.find_element(By.ID, "email").send_keys("user1@example.com")
    self.driver.find_element(By.ID, "password").send_keys("1234")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.LINK_TEXT, "My notepads").click()
    self.driver.find_element(By.LINK_TEXT, "Create New Notepad").click()
    self.driver.find_element(By.ID, "title").click()
    self.driver.find_element(By.ID, "title").send_keys("n1")
    self.driver.find_element(By.ID, "body").click()
    self.driver.find_element(By.ID, "body").send_keys("n1")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.LINK_TEXT, "n1").click()
    self.driver.find_element(By.LINK_TEXT, "Edit").click()
    self.driver.find_element(By.ID, "title").click()
    self.driver.find_element(By.ID, "title").send_keys("n1 modified")
    self.driver.find_element(By.ID, "body").click()
    self.driver.find_element(By.ID, "body").send_keys("n1 modified")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-danger").click()
  
