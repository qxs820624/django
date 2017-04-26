
#coding: utf-8

''' 
设置单元格样式 
'''
import xlwt, xlrd
from openpyxl import Workbook, load_workbook
from openpyxl.compat import range
# 列的数字转换为字母
from openpyxl.utils import get_column_letter

def set_style(name,height,bold=False): 
	style = xlwt.XFStyle() # 初始化样式 

	font = xlwt.Font() # 为样式创建字体 
	font.name = name # 'Times New Roman' 
	font.bold = bold 
	font.color_index = 4
	font.height = height 

	# borders= xlwt.Borders() 
	# borders.left= 6 
	# borders.right= 6 
	# borders.top= 6 
	# borders.bottom= 6 

	style.font = font 
	# style.borders = borders 

	return style 
