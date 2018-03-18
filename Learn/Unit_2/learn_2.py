# 第二章 CSV文件
# comma-separated value 逗号分隔值

#=======读写CSV文件=========================================================
# 
#----------------------------------------------------------------
# input_file = 'supplier_data.csv'
# output_file = 'output_1.csv'
# with open(input_file,'r',newline='') as filereader:
# 	with open(output_file,'w',newline='') as filewriter:
# 		header = filereader.readline()
# 		header = header.strip()
# 		header_list = header.split(',')
# 		print(header_list)
# 		filewriter.write(','.join(map(str,header_list))+'\n')
# 		# map() 将str()应用于 header_list中每个元素 确保每个元素都是字符串
# 		# join() 在header_list中每个值之间插一个逗号 将列表转换为一个字符串
# 		for row in filereader:
# 			row = row.strip()
# 			row_list = row.split(',')
# 			print(row_list)
# 			filewriter.write(','.join(map(str,row_list))+'\n')
#----------------------------------------------------------------


#======pandas 处理CSV==========================================================
# pd.read_csv()  data_frame.to_csv()
#----------------------------------------------------------------
# import pandas as pd

# input_file = 'supplier_data.csv'
# output_file = 'output_pandas.csv'
# data_frame = pd.read_csv(input_file) # 数据框
# print(data_frame)
# data_frame.to_csv(output_file, index=False)
#----------------------------------------------------------------


#======读写CSV文件（二）==========================================================
# Python内置csv模块 csv.reader() csv.writer() .writerow()
#----------------------------------------------------------------
# import csv

# input_file = 'supplier_data.csv'
# output_file = 'output_2.csv'
# with open(input_file,'r',newline='') as csv_in_file:
# 	with open(output_file,'w',newline='') as csv_out_file:
# 		filereader = csv.reader(csv_in_file,delimiter=',',quotechar='"')
# 		filewriter = csv.writer(csv_out_file,delimiter=',') # delimiter 分隔符
# 		for row_list in filereader:
# 			print(row_list)
# 			filewriter.writerow(row_list)
# #----------------------------------------------------------------


#======筛选行==========================================================
# for row in filereader:
	# if value in row meets some business rule or set of rules:
	# 	do something
	# else:
	# 	do something
#----------------------------------------------------------------

#----------------------------------------------------------------


#======筛选行中的值满足某个条件==========================================================
# python csv
#----------------------------------------------------------------
# import csv

# input_file = 'supplier_data.csv'
# output_file = 'output_3.csv'
# with open(input_file,'r',newline='') as csv_in_file: # 如果不指定newline='',则每写入一行将有一空行被写入。
# 	with open(output_file,'w',newline='') as csv_out_file:
# 		filereader = csv.reader(csv_in_file)
# 		filewriter = csv.writer(csv_out_file)
# 		header = next(filereader) # next() 读取文件的第一行
# 		filewriter.writerow(header)
# 		for row_list in filereader:
# 			suppiler = str(row_list[0]).strip()
# 			cost = str(row_list[3].strip('$').replace(',',''))
# 			if suppiler == 'Suppiler Z' or float(cost) > 600.0:
# 				filewriter.writerow(row_list)
#----------------------------------------------------------------


#=======筛选行中的值满足某个条件=========================================================
# pandas .loc() 设置筛选条件
#----------------------------------------------------------------
# import pandas as pd

# input_file = 'supplier_data.csv'
# output_file = 'output_pandas_3.csv'

# data_frame = pd.read_csv(input_file)
# # data_frame['Cost'] = data_frame['Cost'].str.strip('$').str.replace(',','').astype(float) # 直接改变['Cost']的内容
# cost = data_frame['Cost'].str.strip('$').str.replace(',','').astype(float) # 保留原始格式
# data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name'].str.contains('Z'))|(cost >600.0),:]
# print(data_frame_value_meets_condition)
# data_frame_value_meets_condition.to_csv(output_file,index=False)
#----------------------------------------------------------------


#=======筛选行中的值属于某个集合=========================================================
# python csv
#----------------------------------------------------------------
# import csv

# input_file = 'supplier_data.csv'
# output_file = 'output_4.csv'
# important_dates = ['1/20/14', '1/30/14']
# with open(input_file,'r',newline='') as csv_in_file: # 如果不指定newline='',则每写入一行将有一空行被写入。
# 	with open(output_file,'w',newline='') as csv_out_file:
# 		filereader = csv.reader(csv_in_file)
# 		filewriter = csv.writer(csv_out_file)
# 		header = next(filereader) # next() 读取文件的第一行
# 		filewriter.writerow(header)
# 		for row_list in filereader:
# 			a_data = row_list[4]
# 			if a_data in important_dates:
# 				filewriter.writerow(row_list)
#----------------------------------------------------------------


#========筛选行中的值属于某个集合========================================================
# pandas isin()
#----------------------------------------------------------------
# import pandas as pd

# input_file = 'supplier_data.csv'
# output_file = 'output_pandas_4.csv'

# data_frame = pd.read_csv(input_file)
# important_dates = ['1/20/14', '1/30/14']
# data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin(important_dates),:]
# print(data_frame_value_in_set)
# data_frame_value_in_set.to_csv(output_file,index=False)
#----------------------------------------------------------------


#=======行中的值匹配于某个模式\正则表达式=========================================================
# python csv
#----------------------------------------------------------------
# import csv
# import re

# input_file = 'supplier_data.csv'
# output_file = 'output_5.csv'
# # ?P<my_pattern_group> 捕获了名为<my_p_g>的组中匹配了的子字符串 不知道这句目前有什么用
# # ^001-.*	^:只在字符串开头搜索模式	.:匹配任何字符,除了换行符	*:重复前面的字符0次或更多次
# # 即 .* 组合 表示除换行符意外的任何字符出现
# # 参数 re.I 正则表达式进行大小写敏感匹配
# pattern = re.compile(r'(?P<my_pattern_group>^001-.*)',re.I)
# with open(input_file,'r',newline='') as csv_in_file: 
# 	with open(output_file,'w',newline='') as csv_out_file:
# 		filereader = csv.reader(csv_in_file)
# 		filewriter = csv.writer(csv_out_file)
# 		header = next(filereader) 
# 		filewriter.writerow(header)
# 		for row_list in filereader:
# 			invoice_number = row_list[1]
# 			if pattern.search(invoice_number):
# 				filewriter.writerow(row_list)
# 				print(row_list)
#----------------------------------------------------------------


#========行中的值匹配于某个模式\正则表达式========================================================
# pandas startswith() 进行搜索数据
#----------------------------------------------------------------
# import pandas as pd

# input_file = 'supplier_data.csv'
# output_file = 'output_pandas_5.csv'

# data_frame = pd.read_csv(input_file)
# data_frame_value_matches_pattern = data_frame.loc[data_frame['Invoice Number'].str.startswith("001-"),:]
# data_frame_value_matches_pattern.to_csv(output_file,index=False)
# print(data_frame_value_matches_pattern)
#----------------------------------------------------------------


#======选取特定的列==========================================================
# 1.使用列索引值
# 2.使用列标题
#----------------------------------------------------------------

#----------------------------------------------------------------


#======列索引值==========================================================
# python
#----------------------------------------------------------------
# import csv

# input_file = 'supplier_data.csv'
# output_file = 'output_6.csv'
# my_columns = [0,3]
# with open(input_file,'r',newline='') as csv_in_file: 
# 	with open(output_file,'w',newline='') as csv_out_file:
# 		filereader = csv.reader(csv_in_file)
# 		filewriter = csv.writer(csv_out_file)
# 		for row_list in filereader:
# 			row_list_ouput = []
# 			for index_value in my_columns:
# 				row_list_ouput.append(row_list[index_value])
#			filewriter.writerow(row_list_ouput)	
# 			print(row_list_ouput)
#----------------------------------------------------------------


#========列索引值========================================================
# pandas iloc[] 根据索引位置选取列
#----------------------------------------------------------------
# import pandas as pd

# input_file = 'supplier_data.csv'
# output_file = 'output_pandas_6.csv'

# data_frame = pd.read_csv(input_file)
# data_frame_column_by_index = data_frame.iloc[:,[0,3]]
# data_frame_column_by_index.to_csv(output_file,index=False)
# print(data_frame_column_by_index)
#----------------------------------------------------------------


#========列标题========================================================
# python 思想:通过标题行的关键词 得到索引值
#----------------------------------------------------------------
# import csv

# input_file = 'supplier_data.csv'
# output_file = 'output_7.csv'
# my_columns = ['Invoice Number','Purchase Date']
# my_columns_index = []
# with open(input_file,'r',newline='') as csv_in_file: 
# 	with open(output_file,'w',newline='') as csv_out_file:
# 		filereader = csv.reader(csv_in_file)
# 		filewriter = csv.writer(csv_out_file)
# 		header = next(filereader,None)
# 		for index_value in range(len(header)):
# 			if header[index_value] in my_columns:
# 				my_columns_index.append(index_value) # 得到索引值
# 		filewriter.writerow(my_columns)
# 		print(my_columns)		
# 		for row_list in filereader:
# 			row_list_ouput = []
# 			for index_value in my_columns_index:
# 				row_list_ouput.append(row_list[index_value])
# 			filewriter.writerow(row_list_ouput)	
# 			print(row_list_ouput)
#----------------------------------------------------------------


#========列标题========================================================
# pandas lic[] 选取列
#----------------------------------------------------------------
# import pandas as pd

# input_file = 'supplier_data.csv'
# output_file = 'output_pandas_7.csv'

# data_frame = pd.read_csv(input_file)
# data_frame_column_by_name = data_frame.loc[:,['Invoice Number','Purchase Date']]
# data_frame_column_by_name.to_csv(output_file,index=False)
# print(data_frame_column_by_name)
#----------------------------------------------------------------


#=======选取连续的行=========================================================
# python 	row_counter 来跟踪行编号
#----------------------------------------------------------------
# import csv

# input_file = 'supplier_data_unnecessary_header_footer.csv'
# output_file = 'output_8.csv'
# row_counter = 0 
# with open(input_file,'r',newline='') as csv_in_file: 
# 	with open(output_file,'w',newline='') as csv_out_file:
# 		filereader = csv.reader(csv_in_file)
# 		filewriter = csv.writer(csv_out_file)
# 		for row in filereader:
# 			if row_counter >=3 and row_counter <=15:
# 				filewriter.writerow([value.strip() for value in row])	
# 				print(row_counter,[value.strip() for value in row])
# 			row_counter += 1
#----------------------------------------------------------------


#=======选取连续的行=========================================================
# pandas drop() 根据索引的行、列标题来丢弃行或列
#		 iloc[] 根据行索引选取一个单独的行作为列索引
# 		 reindex() 为数据框重新生成索引
#----------------------------------------------------------------
# import pandas as pd

# input_file = 'supplier_data_unnecessary_header_footer.csv'
# output_file = 'output_pandas_8.csv'

# data_frame = pd.read_csv(input_file, header=None) # 不读取header
# data_frame = data_frame.drop([0,1,2,16,17,18])
# data_frame.columns = data_frame.iloc[0] # 
# data_frame = data_frame.reindex(data_frame.index.drop(3))
# data_frame.to_csv(output_file,index=False)
# print(data_frame)
#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------