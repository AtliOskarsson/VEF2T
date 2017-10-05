<!DOCTYPE html>
<html>
<head>
	<title>Login</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="CSS/styles.css">
</head>
<body>
	<h1>Login</h1>
	<form action = "/check", method="post">
		<label>Notendanafn:</label><br>
		<input type="text" name="notendanafn" value="admin"><br>
		<label>Lykilorð:</label><br>
		<input type="password" name="password" value="admin"><br>
		<input type="submit" name="login" value="Innskrá">
	</form>
</body>
</html>