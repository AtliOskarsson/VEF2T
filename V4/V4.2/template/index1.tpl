% include('template/header.tpl', title='{{ title }}')
<a href="{{ link }}">{{ linktext }}</a>
<h1>{{ title }}</h1>
<p>{{ text }}</p>
<img src="{{ mynd1 }}">
% include('template/footer.tpl', info = '{{ contact }}')