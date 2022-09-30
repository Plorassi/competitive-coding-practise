class Solution:
	def validWordAbbreviation(self, word: str, abbr: str) -> bool:
		num = ""
		i = 0
		for char in abbr:
			if char.isdigit():
				if not num and char == "0":
					return False
				num += char
			else:
				if num:
					i += int(num)
					num = ""

				if i >= len(word) or char != word[i]:
					return False

				i += 1

		i += int(num) if num else 0
		
		return i == len(word)

