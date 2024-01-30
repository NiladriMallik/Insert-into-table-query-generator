These python files are for generating "INSERT INTO TABLE tableName VALUES" SQL statements by reading data from a file, the extension of which the user has to specify. These files use the os and pandas libraries.

[InsertIntoTableScriptGenerator.py](https://github.com/NiladriMallik/Insert-into-table-query-generator/blob/main/InsertIntoTableScriptGenerator.py) generates SQL query of only one file, the first file with the input file extension.

[InsertIntoTableScriptGenerator_2_0.py](https://github.com/NiladriMallik/Insert-into-table-query-generator/blob/main/InsertIntoTableScriptGenerator_2_0.py) generates SQL queries of all the different files with the input file extension. A different SQL file is generated for each file.
