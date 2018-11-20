
class MaskHelper:

	def check_match(self, arb_id, can_id, mask):
		incoming = arb_id & mask
		target = can_id & mask

		print("arb_id & mask: {}\ncan_id & mask: {}".format(incoming, target))