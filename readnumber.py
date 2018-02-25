#!/usr/bin/env python3

def main(args):
	def readnumber(number):
		onenumber = {'0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn',
		'5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín'}
		str_number = str(number)
		length = len(str_number)
		
		def twonumber(number):
			if number == '00':
				return ''
			elif number[0] == '0':
				return onenumber[number[1]]
			elif number == '10':
				return 'mười'
			elif number == '15':
				return 'mười lăm'
			elif number[0] == '1':
				return 'mười ' + onenumber[number[1]]
			else:
				out = onenumber[number[0]] + ' mươi'
				if number[1] == '1':
					out = out + ' mốt'
				elif number[1] == '5':
					out = out + ' lăm'
				elif number[1] != '0':
					out = out + ' ' + onenumber[number[1]]
				return out
		
		def threenumber_sub(number):
			out = onenumber[number[0]] + ' trăm'
			if number[1] == '0' and number[2] != '0':
				out = out + ' lẻ ' + onenumber[number[2]]
			else:
				out = out + ' ' + twonumber(number[1:3])
			return out
		
		def threenumber(number, unit):
			if unit != 0:
				if number == '000':
					return ''
				else:
					out = threenumber_sub(number)
					unit_system = {2: ' nghìn ', 3: ''}
					out = out + unit_system[unit]
			else:
				length = len(number)
				if length == 3:
					if number[0] == '0':
						out = twonumber(number[1:3])
					else:
						out = threenumber_sub(number)
				elif length == 2:
					out = twonumber(number)
				else:
					out = onenumber[number]
			return out
			
		def ninenumber(number):
			number_temp = int(number)
			if number_temp == 0:
				return ''
			else:
				length = len(str(number_temp))
				rank = (length - 1/2) // 3
				if rank == 0:
					out = threenumber(number,0)
				elif rank == 1:
					out = threenumber(number[0:-3],0) + ' nghìn ' + threenumber(number[-3:],3)
				else:
					out = threenumber(number[0:-6],0) + ' triệu ' + threenumber(number[-6:-3],2) + threenumber(number[-3:], 3)
				return out
		
		def moreninenumber(number):
			number_temp = number
			out = ''
			med = ''
			while len(number_temp) > 9:
				tag = number_temp[-9:]
				int_tag = int(tag)
				if int_tag > 0 and int_tag < 100:
					doc = threenumber_sub(tag[-3:])
				else:
					doc = ninenumber(str(int_tag))
				med = med + ' tỷ'
				out = med + ' ' + doc + out
				number_temp = number_temp[0:-9]
			out = ninenumber(number_temp) + out
			return out
		
		if length <=3:
			out = threenumber(str_number,0)
		elif length <= 9:
			out = ninenumber(str_number)
		else:
			out = moreninenumber(str_number)
		if out[-1] == ' ':
			out = out[0:-1]
		out = out.replace('  ',' ')
		out = out[0].upper() + out[1:] + '.'
		return out
			
	import tkinter
	root = tkinter.Tk()
	root.title('Đọc số')
	label1 = tkinter.Label(text = 'Nhập số')
	label1.grid(row = 0)
	entry = tkinter.Entry()
	entry.grid(row = 0, column = 1, sticky = 'W')
	def execute(*arg):
		number = int(entry.get())
		out = readnumber(number)
		result['state'] = tkinter.NORMAL
		result.delete(0.0, tkinter.END)
		result.insert(0.0,out)
		result['state'] = tkinter.DISABLED
	root.bind('<Return>', execute)
	button = tkinter.Button(text = 'Đọc số', command = execute)
	button.grid(row = 0, column = 2, sticky = 'W')
	label2 = tkinter.Label(text = 'Kết quả')
	label2.grid(columnspan = 3)
	result = tkinter.Text(height = 10, width = 40, wrap = tkinter.WORD,
	font = ('Times_New_Roman',10), state = tkinter.DISABLED)
	result.grid(columnspan = 3)
	root.mainloop()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
