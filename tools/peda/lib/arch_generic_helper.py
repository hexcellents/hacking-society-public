import os
from utils import *
import config

class arch_generic_helper(object):
	def __init__(self, archname, bitness):
		self.archname = archname
		self.bitness = bitness
		self.gen_conditions_expand()
		self.gen_compare_instrs()
		self.gen_call_instrs()
		self.gen_jump_instrs()
		self.gen_return_regexes()
		self.gen_syscall_instrs()

	def is_flags_register(self, reg):
		return reg == self.flags_register

	#initial generators
	def gen_conditions_expand(self):
		f_list = [ i for i in self.flags_names.values() ]
		for cond in self.conditions.keys():
			for f in f_list:
				if f in self.conditions[cond]:
					self.conditions[cond] = self.conditions[cond].replace(f, 'flags["' + f + '"]')

	def gen_compare_instrs(self):
		for cond in self.conditions.keys():
			for compare in self.compare_base:
				self.compare_instrs.append(compare + cond)

	def gen_syscall_instrs(self):
		for cond in self.conditions.keys():
			for syscall in self.syscall_base:
				self.syscall_instrs.append(syscall + cond)


	#getters
	def get_register_list(self, bitness=None):
		lst = []
		for i in self.registers.values():
			for t in i:
				if isinstance(t, basestring):
					lst.append(t)
				else:
					lst.append(t[0])
		return lst

	def get_register_altname(self, reg):
		for t_list in self.registers.values():
			for t in t_list:
				if isinstance(t, tuple):
					if t[0] == reg:
						return t[1]
		return None

	def get_register_content(self, reg, val):
		if self.is_flags_register(reg):
			return self.pretty_print_flags(val)
		return val

	def get_flags_register_name(self):
		return self.flags_register

	def get_returnval_expr(self):
		return self.returnval_expr

	def get_compare_instrs(self):
		return self.compare_instrs

	def get_call_instrs(self):
		return self.call_instrs

	def get_jump_instrs(self):
		return self.jump_instrs

	def get_condjump_instrs(self):
        	return [i for i in self.jump_instrs if not(i in self.jump_uncond) ]

	def get_return_regexes(self):
		return self.return_regexes

	def get_syscall_instrs(self):
		return self.syscall_instrs

	def get_gdb_setup_cmds(self):
		return self.gdb_setup_cmds
