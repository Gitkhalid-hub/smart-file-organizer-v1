# THE FILE CLASSIFIER.

class FileClassifier:
	def classify(self, file_path):
		# defined category rules
		category_rules = {
		 "documents" : [".pdf", ".docx", ".txt"],
		 "images" : [".jpg", ".jpeg", ".png"],
		 "code" : [".py", ".js"],
		 }
		
		extension = file_path.suffix
		
		for category_name, extensions in category_rules.items():
			if extension in extensions:
				return category_name
		return "others"