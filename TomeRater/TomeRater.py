########################################
class User(object):
	def __init__(self, name, email):
		self.books = {};
		self.name = name;
		self.email = email;

	def get_email(self):
		return self.email;

	def change_email(self, new_email):
		self.email = new_email;
		print("Email for user {name} has been updated to {email}".format(name=self.name, email=self.email));

	def __repr__(self):
		return "User: {name}, email: {email}, books read: {books_read}".format(name=self.name, email=self.email, books_read=len(self.books));

	def __eq__(self, other_user):
		return (self.name == other_user.name and self.email == other_user.email);
		
	def read_book(self, book, rating = None):
		self.books[book] = rating;
		
	def get_average_rating(self):
		sum = 0;
		length = 0;
		for book in self.books:
			# Check if the book has been rated:
			if(self.books[book] != None):
				length += 1; 
				sum += self.books[book];
		if(length==0):
			return 0;
		else:
			return sum/length;
########################################
class Book(object):
	def __init__(self, title, isbn):
		self.title = title;
		self.isbn = isbn;
		self.ratings = [];

	def get_title(self):
		return self.title;

	def get_isbn(self):
		return self.isbn;

	def set_isbn(self, new_isbn):
		self.isbn = new_isbn;
		print("ISBN for book {title} has been updated to {isbn}".format(title=self.title, isbn=self.isbn));
		
	def add_rating(self, rating):
		if(rating != None and rating>=0 and rating<=4):
			self.ratings.append(rating)
		else:
			print("Invalid Rating");

	def __repr__(self):
		return "Book: {title}, ISBN: {isbn}, ratings added: {rating_count}".format(title=self.title, isbn=self.isbn, rating_count=len(self.ratings));

	def __eq__(self, other_book):
		return (self.title == other_book.title and self.isbn == other_book.isbn);
		
	def __hash__(self):
		return hash((self.title, self.isbn));
	
	def get_average_rating(self):
		sum = 0;
		length = len(self.ratings)
		for rating in self.ratings:
			sum += rating;
		if(length==0):
			return 0;
		else:
			return sum/length;
########################################
class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn);
		self.author = author;
		
	def get_author(self):
		return self.author;

	def __repr__(self):
		return "{title} by {author}".format(title=self.title, author=self.author);
########################################
class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn);
		self.subject = subject;
		self.level = level;
		
	def subject(self):
		return self.subject;

	def get_isbn(level):
		return self.level;
		
	def __repr__(self):
		return "{title}, a {level} manual on by {subject}".format(title=self.title, level=self.level, subject=self.subject);
########################################
class TomeRater(object):
	def __init__(self):	
		self.users = {};
		self.books = {};
	
	def create_book(self, title, isbn):
		return Book(title, isbn);
		
	def create_novel(self, title, author, isbn):
		return Fiction(title, author, isbn);
		
	def create_non_fiction(self, title, subject, level, isbn):
		return Non_Fiction(title, subject, level, isbn);
		
	def add_book_to_user(self, book, email, rating = None):
		if(email in self.users):
			self.users[email].read_book(book, rating);
			if(rating != None):
				book.add_rating(rating);			
			if(self.books.get(book) == None):
				self.books[book] = 1;
			else:
				self.books[book] += 1;
		else:
			print("No user with email {email}!".format(email=email))
			
	def add_user(self, name, email, user_books = None):
		self.users[email] = User(name, email);
		if(user_books != None):
			for book in user_books:
				self.add_book_to_user(book, email);
			
	def print_catalog(self):
		for book in self.books:
			print(book);
			
	def print_users(self):
		for user in self.users.values():
			print(user);
			
	def get_most_read_book(self):
		max_read_count = 0
		max_read_book = None;
		for book in self.books:
			#print(book.title+": "+str(self.books[book]));
			if (max_read_count < self.books[book]):
				max_read_count = self.books[book]
				max_read_book = book;
		return max_read_book;
		
	def get_highest_rated_book(self):
		max_rating = 0
		max_rated_book = None;
		for book in self.books:
			rating = book.get_average_rating();
			#print(book.title+": "+str(rating));
			if (max_rating<rating):
				max_rating = rating;
				max_rated_book = book;
		return max_rated_book;
		
	def get_most_positive_user(self):
		max_rating = 0
		max_pos_user = None;
		for user in self.users.values():
			rating = user.get_average_rating();
			#print(user.name+": "+str(rating));
			if (max_rating<rating):
				max_rating = rating;
				max_pos_user = user;
		return max_pos_user;
########################################