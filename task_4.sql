USE alx_book_store;
SELECT COLUMN_NAME, COLUMN_TYPE
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
AND TABLE_NAME = 'Books';
