BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `tbl_Authors` (
	`Author_ID`		INTEGER Primary KEY,
	`Author_NAME`	TEXT NOT NULL
);
CREATE INDEX ind_Authors_Author_ID ON tbl_Authors(Author_ID)
CREATE TABLE IF NOT EXISTS `tbl_Books` (
	`Book_ID`		INTEGER Primary KEY,
	`Book_NAME`		TEXT NOT NULL,
	`Author_ID` 	INTEGER NOT NULL,
	`Ỳear` 			TEXT NOT NULL,
	FOREIGN KEY(Author_ID) REFERENCES tbl_Authors(Author_ID)
);
CREATE INDEX ind_Books_Book_ID ON tbl_Books(Book_ID)
CREATE TABLE IF NOT EXISTS `tbl_Sentences` (
	`Sentence_ID`	INTEGER PRIMARY KEY,
	`Book_ID`		INTEGER NOT NULL,
	`Sentence`		TEXT NOT NULL,
	FOREIGN KEY(Book_ID) REFERENCES tbl_Books(Book_ID)
);
CREATE INDEX ind_Sentences_Sentence_ID ON tbl_Sentences(Sentence_ID)
COMMIT;
