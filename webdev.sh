#Author: Thomas Dost


if (( "$#" == 0 )) 
	then 
		
		echo "Pls enter a project name"
		read -p "Enter: " name
		name=${name}
	else
		name=${1}
fi
#echo $name
mkdir $name
cd $name

mkdir html
mkdir javascript

echo "
<!-- 
*Author: 	Thomas Dost
*Purpose:	
*Date:
*Changelog:	
*Todo:
-->



<!DOCTYPE html>
<html lang=\"de\">
  <head>
    <meta charset=\"utf-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <script type=\"text/javascript\" src=\"../javascript/index.js\"></script>
    <title>Titel</title>
  </head>
  <body>
  </body>
</html>
" >> html/index.html


echo "\
alert(\"Hello World\")\
" >> javascript/index.js


