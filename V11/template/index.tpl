<!DOCTYPE html>
<html>
<head>
	<title>BILAR!!</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="CSS/styles.css">
</head>
<body>
	<form>
		%for x in posts["bilar_listi"]
			<input type="radio" name="skranginanumer" value="x[{'skranginanumer'}]">
		%end
	</form>
</body>
</html>