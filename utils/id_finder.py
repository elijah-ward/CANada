import pprint

pp = pprint.PrettyPrinter(indent=4)

class IdFinder:

	def __init__(self, mask, limit):
		self.mask = mask
		self.limit = limit

	def generate_ids(self):
		ids = {}

		for x in range(self.limit):
			candidate = self.mask & x
			if not candidate in ids:
				ids[candidate] = x

		pp.pprint(ids)


def main():

	id_finder = IdFinder(0x12345, 10000)
	id_finder.generate_ids()

if __name__ == "__main__": main()

