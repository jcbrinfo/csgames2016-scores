"""
Convert data collected as web pages in the `en` directory to CSV (RFC 4180)
files written in the `csv` directory.

Compatible with Python 3.

Synopsis
--------
python3 to-csv.py {year}
"""

import csv
import os
import os.path
import re
from sys import argv, stderr
from xml.dom.minidom import parseString

IN_EXT = ".html"
OUT_EXT = ".csv"

class WebPage(object):
	"""
	Parser for an input web page. Skips the non-XML lines pass the rest
	`to xml.dom.minidom.parse`. Also fix boolean attributes, some ampersands and
	unclosed `<div>`s and `<td>`s.

	Usable only once `__enter__` is called (using `with`).
	"""

	UNCLOSED_TD_RE = re.compile("<td>([0-9]+)<td>")

	def __init__(self, path):
		self.path = path
		"""
		str
			path to the input file
		"""

		self.document = None
		"""
		xml.dom.Document
			actual parsed document
		"""

	def __enter__(self):
		with open(self.path) as in_file:
			lines = in_file.readlines()
		lines = lines[:2] + lines[43:-2] + ["</div></div>"] + lines[-2:]
		for i in range(len(lines)):
			lines[i] = lines[i].replace(" selected>", " selected=\"\">")
			lines[i] = lines[i].replace(" & ", " &amp; ")
			lines[i] = re.sub(self.UNCLOSED_TD_RE, r"<td>\1</td><td>", lines[i])
		self.document = parseString("".join(lines))
		return self

	def __exit__(self, type, value, trace):
		pass

	def get_table_data(self):
		"""
		Yield each `<tr>` that has `<td>` elements as a list of strings.
		"""
		for tr in self.document.getElementsByTagName("tr"):
			cells = tr.getElementsByTagName("td")
			if cells:
				for cell in cells:
					yield list(get_inner_text(cell) for cell in cells)

def get_inner_text(element):
	"""
	Get the inner text of the specified XML element.
	"""
	buffer = []
	for node in element.childNodes:
		if node.nodeType == node.TEXT_NODE:
			buffer.append(node.data)
		elif node.nodeType == node.ELEMENT_NODE:
			buffer.append(get_inner_text(node))
	return "".join(buffer)

def run(year):
	"""
	Run the program with the specified year.
	"""

	project_dir = os.path.dirname(os.path.realpath(__file__))
	in_dir = os.path.join(project_dir, year, "en/")
	out_dir = os.path.join(project_dir, year, "csv/")

	if not os.path.isdir(out_dir):
		os.mkdir(out_dir)

	for filename in os.listdir(in_dir):
		in_file_path = os.path.join(in_dir, filename)
		if os.path.isfile(in_file_path) and filename.endswith(IN_EXT):
			stderr.write("Extracting data from " + in_file_path + "…")
			out_file_path = os.path.join(
				out_dir,
				filename[:-len(IN_EXT)] + OUT_EXT
			)
			with open(out_file_path, "w", newline="") as out_file:
				writer = csv.writer(out_file)
				with WebPage(in_file_path) as page:
					for row in page.get_table_data():
						writer.writerow(row)
			stderr.write(" Done.\n")

if __name__ == "__main__":
	year = argv[1]
	run(year)
